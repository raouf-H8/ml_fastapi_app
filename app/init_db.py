from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, User
import os

DATABASE_URL = os.environ.get("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    if db.query(User).count() == 0:  # insère uniquement si vide
        db.add_all([
            User(name="Alice"),
            User(name="Bob")
        ])
        db.commit()
    db.close()