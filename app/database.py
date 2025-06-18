# contient la configuration technique de la BDD (engine, SessionLocal, DATABASE_URL)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.environ.get("DATABASE_URL") #le DATABASE_URL est défini dans le test.yml et docker-compose.yml
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
