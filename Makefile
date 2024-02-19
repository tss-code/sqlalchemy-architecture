RUN=docker-compose -f compose.yaml up
ALEMBIC_UPGRADE = alembic upgrade head
ALEMBIC_REVISION = alembic revision --autogenerate -m

.PHONY: start-app
start-app: $(RUN)
