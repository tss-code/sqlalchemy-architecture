RUN = docker-compose -f compose.yaml up
ALEMBIC_UPGRADE = alembic upgrade head
ALEMBIC_REVISION = alembic revision --autogenerate -m

run-app:
    $(RUN)