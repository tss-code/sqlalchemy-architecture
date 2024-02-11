BUILD_ENV = docker build -t sql-alchemy:dev -f docker/Dockerfile .
RUN_ENV = docker run -it sql-alchemy:dev /bin/bash

RUN = docker-compose -f compose.yaml up

build-env:
    $(BUILD_ENV)

run-env:
    $(RUN_ENV)

start-env:
    $(BUILD_ENV)
    $(RUN_ENV)

run:
    $(RUN)
