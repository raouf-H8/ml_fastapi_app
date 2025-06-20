# Script de bootstrap ou peuplement BDD

from app.models import Base, User
from app.database import engine, SessionLocal

def init_db():
    """
    Initialise la base de données :
    - Crée les tables si elles n'existent pas
    - Ajoute des utilisateurs par défaut si la table est vide
    """
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        if db.query(User).count() == 0:
            db.add_all([
                User(name="Alice"),
                User(name="Bob")
            ])
            db.commit()
    finally:
        db.close()