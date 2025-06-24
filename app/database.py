# utilitaire qui contient la configuration technique de la BDD (engine, SessionLocal, DATABASE_URL)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

#update pour utiliser le .env et charger les var d'env
from dotenv import load_dotenv

# Ne charge le .env que si on n’est pas en CI
if not os.getenv("GITHUB_ACTIONS"):
    load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL") #le DATABASE_URL ETAIT ANCIENNEMENT défini dans le test.yml et docker-compose.yml 
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set.")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)