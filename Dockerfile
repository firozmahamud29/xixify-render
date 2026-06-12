FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends curl git ffmpeg ripgrep && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir hermes-agent[web]

RUN mkdir -p /root/.hermes

RUN printf 'gateway:
  api_server:
    enabled: true
    host: 0.0.0.0
    port: 10000
    key: xixify-agent-2026
approvals:
  mode: off
memory:
  memory_enabled: true
  user_profile_enabled: true
model:
  provider: openrouter
' > /root/.hermes/config.yaml

EXPOSE 10000

CMD ["hermes", "gateway", "run"]
