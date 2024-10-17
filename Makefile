
build:
	- docker compose build

test: 
	- docker compose up -d db
	- docker compose run test
	- docker compose down 
# Regra alternativa
# docker compose exec web python manage.py test

ci: build test