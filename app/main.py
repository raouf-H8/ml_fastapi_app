# contient uniquement l'instanciation de l'API, les routes, et l'orchestration.

from fastapi import FastAPI
from app.init_db import init_db
from app.models import User
from pydantic import BaseModel

from app.models import Base
from app.database import engine, SessionLocal  
import os
import joblib

Base.metadata.create_all(bind=engine) #sert à créer automatiquement les tables dans ta base de données à partir de tes modèles SQLAlchemy declaré avec base

model = joblib.load("model.pkl")  

app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()

@app.get("/users")
def get_users():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return [{"id": u.id, "name": u.name} for u in users]

class UserCreate(BaseModel):
    name: str

@app.post("/users")
def create_user(user: UserCreate):
    db = SessionLocal()
    new_user = User(name=user.name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()
    return {"id": new_user.id, "name": new_user.name}

class PredictInput(BaseModel):
    x1: float
    x2: float

@app.post("/predict")
def predict(input: PredictInput):
    X = [[input.x1, input.x2]]
    y_pred = model.predict(X)[0]
    return {"prediction": int(y_pred)}

from copy import deepcopy
from typing import List
from enum import Enum
import spacy

# définition et chargement du modele de données de reconnaissance d'entitées nommées en et fr
def load_models():
    """
    load the models from disk
    and put them in a dictionary

    Returns:
        dict: loaded models
    """
    models = {
        "en_sm": spacy.load("app/nlp_models/en_sm"),
        "fr_sm": spacy.load("app/nlp_models/fr_sm"),
    }
    print("models loaded from disk")
    return models


models = load_models()


class ModelLanguage(str, Enum):
    fr = "fr"
    en = "en"


class ModelSize(str, Enum):
    sm = "sm"
    md = "md"
    lg = "lg"


class UserRequestIn(BaseModel):
    text: str
    model_language: ModelLanguage = ModelLanguage.en
    model_size: ModelSize = ModelSize.sm


class EntityOut(BaseModel):
    start: int
    end: int
    type: str
    text: str


class EntitiesOut(BaseModel):
    entities: List[EntityOut]
    anonymized_text: str


@app.post("/entities", response_model=EntitiesOut)
def extract_entities(user_request: UserRequestIn):
    text = user_request.text
    language = user_request.model_language
    model_size = user_request.model_size

    model_key = language + "_" + model_size

    model = models[model_key]
    doc = model(text)

    entities = [
        {
            "start": ent.start_char,
            "end": ent.end_char,
            "type": ent.label_,
            "text": ent.text,
        }
        for ent in doc.ents
    ]

    anonymized_text = list(deepcopy(text))

    for entity in entities:
        start = entity["start"]
        end = entity["end"]
        anonymized_text[start:end] = "X" * (end - start)

    anonymized_text = "".join(anonymized_text)
    return {"entities": entities, "anonymized_text": anonymized_text}
