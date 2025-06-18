
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

projet_dong/_
├── app/_
│ ├── main.py ← API FastAPI_
│ ├── models.py ← Modèle SQLAlchemy_
│ └── init_db.py ← Initialisation DB_
├── model.pkl ← Modèle ML serialisé_
├── requirements.txt_
├── Dockerfile_
├── docker-compose.yml_
├── init.sql ← Script d'init SQL_
├── tests/_
│ ├── test_unit.py_
│ └── test_integration.py_
├── nginx/_
│ └── default.conf_
└── .github/_
└── workflows/_
└── test.yml ← Pipeline GitHub Actions_
