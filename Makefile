# Makefile pour faciliter le développement

# Lance tous les conteneurs
up:
	docker-compose up -d

# Arrête tous les conteneurs
down:
	docker-compose down

# Reconstruit l’image de l'API (si Dockerfile changé)
build:
	docker-compose build

# Lancer les tests
test:
	docker-compose run --rm test

# Regarder les logs
logs:
	docker-compose logs -f

# Accès shell au conteneur api
shell:
	docker exec -it projet_dong-api-1 sh

#testdev sur la plateforme de devcontainer
testd:
	pytest tests/