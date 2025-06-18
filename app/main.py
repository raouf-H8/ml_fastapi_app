from fastapi import FastAPI
from app.init_db import init_db
from app.models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

from app.models import Base
from app.database import engine  # ou session, selon ton code
import os
import joblib

Base.metadata.create_all(bind=engine)

model = joblib.load("model.pkl")  # ou "./model.pkl" selon ton dossier de travail

DATABASE_URL = os.environ.get("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

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