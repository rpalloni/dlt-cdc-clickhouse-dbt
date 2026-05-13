COMPOSE = docker compose \
	-f docker/docker-compose-pg-cdc.yml \
	-f docker/docker-compose-clickhouse.yml \
	-f docker/docker-compose-storage.yml \
	--env-file docker/.env

network:
	docker network inspect data-network >/dev/null 2>&1 || docker network create data-network

up: network
	$(COMPOSE) up --build

down: 
	$(COMPOSE) down

destroy: 
	$(COMPOSE) down --remove-orphans -v