FROM python:3.11-slim

WORKDIR api

COPY . .

RUN pip install -r requirements.txt

ENV FLASK_APP=app/main.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["flask", "run"]