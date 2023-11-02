FROM python:3.12

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

RUN chmod +x /app/run_server.sh

CMD ["sh", "/app/run_server.sh"]