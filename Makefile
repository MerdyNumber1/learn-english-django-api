dev-build:
	docker-compose --file docker-compose.dev.yml build --no-cache

dev:
	docker-compose --file docker-compose.dev.yml up

dev-down:
	docker-compose --file docker-compose.dev.yml down

make-migrations:
	docker-compose --file docker-compose.dev.yml exec web_app pipenv run python app/manage.py makemigrations

migrate:
	docker-compose --file docker-compose.yml exec web_app pipenv run python app/manage.py migrate

seed:
	docker-compose --file docker-compose.yml exec web_app pipenv run python app/manage.py loaddata data/web_app/dump.json

dump:
	docker-compose --file docker-compose.yml exec web_app pipenv run python app/manage.py dumpdata --indent 4 -e sessions -e admin -e contenttypes -e auth.Permission > data/web_app/dump.json

prod-build:
	docker-compose build --no-cache

prod:
	docker-compose up
