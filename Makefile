dev-build:
	docker-compose --file docker-compose.dev.yml build

dev:
	docker-compose --file docker-compose.dev.yml up

dev-down:
	docker-compose --file docker-compose.dev.yml down

make-migrations:
	docker-compose --file docker-compose.dev.yml exec web_app pipenv run py app/manage.py makemigrations

migrate:
	docker-compose --file docker-compose.dev.yml exec web_app pipenv run py app/manage.py migrate

seed:
	docker-compose --file docker-compose.dev.yml exec web_app pipenv run py app/manage.py loaddata dump.json

dump:
	docker-compose --file docker-compose.dev.yml exec web_app pipenv run py app/manage.py dumpdata --indent 4 > app/dump.json
