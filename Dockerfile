FROM python:3.9-buster

ENV PYTHONUNBUFFERED=1

RUN pip install aiohttp

WORKDIR /app

COPY . /app

EXPOSE 8080

CMD ["python", "main.py"]
