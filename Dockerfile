FROM python:3.12-slim

#QoL lines for docker
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.main.txt .
RUN pip install --no-cache-dir -r requirements.main.txt

COPY scraper.py .
COPY main ./main

ENTRYPOINT ["python", "main/main.py"]
