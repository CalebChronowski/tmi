FROM python:3.12
WORKDIR /app
COPY ./app /app
RUN pip install fastapi uvicorn sqlalchemy psycopg2
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]
