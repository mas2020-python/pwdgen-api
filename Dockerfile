FROM python:3.10-slim-buster

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
WORKDIR /app/src
CMD [ "uvicorn", "main:app" , "--host=0.0.0.0", "--port=8080"]
