# Essas funções fornecem um conjunto de comandos úteis para gerenciar o ambiente de desenvolvimento usando o Docker Compose.

# network_existe := $(shell docker network ls -f name=host-databases-nosql-network -q)

# make-network:
# 	@if [ "$(network_existe)" = "" ]; then \
# 		echo "Criando a rede name=host-databases-nosql-network..."; \
# 	docker network create name=host-databases-nosql-network; \
# 	else \
# 		echo "A rede name=host-databases-nosql-network já existe."; \
# 	fi

# docker-dev-up: make-network

# MONGO
# Inicia os contêineres definidos em modo detached.
docker-mongo-up:
	docker-compose -f docker-compose-mongo.yaml up -d
	
# Constrói e inicia os contêineres definidos em modo detached.	
docker-mongo-build:
	docker-compose -f docker-compose-mongo.yaml up --build -d

# Exibe os logs dos contêineres definidos com um limite de 100 linhas.
docker-mongo-logs:
	docker-compose -f docker-compose-mongo.yaml logs -f --tail=100

# Executa os targets `docker-mongo-build` e `docker-mongo-logs` sequencialmente.
docker-mongo-build-logs: docker-mongo-build docker-mongo-logs

# Para a execução dos contêineres definidos.
docker-mongo-stop:
	docker-compose -f docker-compose-mongo.yaml stop

# Para e remove os contêineres, redes e volumes definidos.
docker-mongo-down:
	docker-compose -f docker-compose-mongo.yaml down
