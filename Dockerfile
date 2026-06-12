FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl git ffmpeg ripgrep && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir hermes-agent[web]

RUN mkdir -p /root/.hermes

COPY start.py /start.py
RUN chmod +x /start.py

EXPOSE 10000

CMD ["python3", "/start.py"]
