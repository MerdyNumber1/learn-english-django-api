dev-build:
	docker-compose --file docker-compose.dev.yml build

dev:
	docker-compose --file docker-compose.dev.yml up

dev-down:
	docker-compose --file docker-compose.dev.yml down
