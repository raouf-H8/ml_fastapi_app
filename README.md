
# 🧠 Projet Dong – API FastAPI avec modèle ML et PostgreSQL

![Tests](https://github.com/raouf-H8/ml_fastapi_app/actions/workflows/test.yml/badge.svg)

Une API FastAPI déployée avec Docker, connectée à une base PostgreSQL, et intégrée à un pipeline CI avec GitHub Actions.

## 🚀 Fonctionnalités

- CRUD sur des utilisateurs via SQLAlchemy
- Prédiction via un modèle machine learning (chargé depuis `model.pkl`)
- Base de données initialisée automatiquement (`init.sql`)
- Reverse proxy via Nginx
- Tests unitaires & d’intégration automatisés (Pytest)
- Visualisation DB via PGAdmin (à venir)

## 🧱 Architecture

projet_dong/
├── app/
│ ├── main.py ← API FastAPI
│ ├── models.py ← Modèle SQLAlchemy
│ └── init_db.py ← Initialisation DB
├── model.pkl ← Modèle ML serialisé
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── init.sql ← Script d'init SQL
├── tests/
│ ├── test_unit.py
│ └── test_integration.py
├── nginx/
│ └── default.conf
└── .github/
└── workflows/
└── test.yml ← Pipeline GitHub Actions
