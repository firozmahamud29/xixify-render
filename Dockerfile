FROM nousresearch/hermes-agent:latest

# Don't override CMD — let s6-overlay manage services
# Just set environment variables and config

ENV API_SERVER_ENABLED=true
ENV API_SERVER_PORT=10000
ENV API_SERVER_HOST=0.0.0.0
ENV GATEWAY_ALLOW_ALL_USERS=true
ENV PORT=10000
ENV HERMES_DASHBOARD=true

# Create hermes config with API server enabled on 0.0.0.0
RUN mkdir -p /home/agent/.hermes && \
    printf 'gateway:\n  api_server:\n    enabled: true\n    host: 0.0.0.0\n    port: 10000\napprovals:\n  mode: off\nmemory:\n  memory_enabled: true\n  user_profile_enabled: true\n' > /home/agent/.hermes/config.yaml && \
    chown -R hermes:hermes /home/agent/.hermes

EXPOSE 10000
