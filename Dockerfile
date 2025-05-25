
FROM python:3.9


WORKDIR /app


COPY requirements.txt requirements.txt
COPY . /app


RUN pip install -r requirements.txt

COPY . .

CMD uvicorn main:app --host=0.0.0.0