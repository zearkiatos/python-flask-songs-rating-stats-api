activate:
	source run.sh; activate

install:
	source run.sh; install

run:
	source run.sh; run $(port)

docker-up:
	source run.sh; docker_up

docker-down:
	source run.sh; docker_down

run-docker:
ifeq ($(strip $(port)),)
	flask run -h 0.0.0.0
else
	flask run -p $(port) -h 0.0.0.0
endif

docker-dev-up:
	docker compose -f docker-compose.dev.yml up --build -d

docker-dev-down:
	docker compose -f docker-compose.dev.yml down

docker-db-up:
	docker compose -f docker-compose.db.yml up --build

docker-db-down:
	docker compose -f docker-compose.db.yml down

run-workers:
	celery -A flaskr.tasks worker -l info

run-flask-broker-docker:
ifeq ($(strip $(port)),)
	make run-workers; flask run -h 0.0.0.0
else
	make run-workers; flask run -p $(port) -h 0.0.0.0
endif
