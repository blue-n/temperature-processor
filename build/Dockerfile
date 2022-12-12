FROM python:3.7-slim-bullseye

WORKDIR /app/src

COPY requirements.txt /app

RUN pip install -r ../requirements.txt

COPY . /app

CMD ["python", "main.py"]
