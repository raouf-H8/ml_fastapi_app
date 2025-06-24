
# 🧠 Projet Dong – API FastAPI avec modèle ML et PostgreSQL

![Tests](https://github.com/raouf-H8/ml_fastapi_app/actions/workflows/test.yml/badge.svg)

Une API FastAPI déployée avec Docker, connectée à une base PostgreSQL, et intégrée à un pipeline CI avec GitHub Actions.

## 🚀 Fonctionnalités

- CRUD sur des utilisateurs via SQLAlchemy
- Fonctionnalité de reconnaissance d'entités nommées
- Prédiction via un modèle machine learning (chargé depuis `model.pkl`)
- Base de données initialisée automatiquement (`init.sql`)
- Reverse proxy via Nginx
- Tests unitaires & d’intégration automatisés (Pytest)
- Visualisation DB via PGAdmin (à venir)

## Deploiement piloté par GitHub Actions (via CI/CD + webhook) sur Render

          [GitHub commit]
                 ↓
            [GitHub Actions]
                 ↓
        ┌────────┴─────────┐
    [Tests passent ?]   →   [Non]  → STOP ❌
         ↓ Oui
          [Appel webhook Render]
         ↓
    [Déploiement Render]
         ↓
        ✅ En ligne


## 🧱 Architecture

projet_dong/

├── app/

│ ├── main.py ← contient uniquement l'instanciation de l'API, les routes, et l'orchestration.
│ ├── nlp_models ← contient les dossiers des modèles nlp pour la detection d'entitees nommees

│ ├── models.py ← Modèle SQLAlchemy

│ ├── database.py ← contient la configuration technique de la BDD (engine, SessionLocal, DATABASE_URL)

│ ├── __init__.py ← fichier vide indiquant que le dossier /app est un package

│ └── init_db.py ← Initialisation DB

├── model.pkl ← Modèle ML serialisé

├── requirements.txt

├── Dockerfile

├── docker-compose.yml

├── init.sql ← Script d'init SQL

├── tests/
├── __init__.py
│ ├── test_unit.py

│ └── test_integration.py

├── nginx/

│ └── default.conf

└── .github/

│ └── workflows/

│ │ └── test.yml ← Pipeline GitHub Actions
