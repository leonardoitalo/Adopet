build:
	- docker compose build

lint:
	-  docker compose exec web black .
	-  docker compose exec web flake8 .

test: 
	- docker compose up -d db
	- docker compose run test
	- docker compose down 
# Regra alternativa
# docker compose exec web python manage.py test

ci: build lint test