FROM nousresearch/hermes-agent:latest

# Create hermes config with API server enabled on 0.0.0.0
RUN mkdir -p /home/agent/.hermes && \
    echo 'gateway:' > /home/agent/.hermes/config.yaml && \
    echo '  api_server:' >> /home/agent/.hermes/config.yaml && \
    echo '    enabled: true' >> /home/agent/.hermes/config.yaml && \
    echo '    host: 0.0.0.0' >> /home/agent/.hermes/config.yaml && \
    echo '    port: 10000' >> /home/agent/.hermes/config.yaml && \
    echo 'approvals:' >> /home/agent/.hermes/config.yaml && \
    echo '  mode: off' >> /home/agent/.hermes/config.yaml && \
    echo 'memory:' >> /home/agent/.hermes/config.yaml && \
    echo '  memory_enabled: true' >> /home/agent/.hermes/config.yaml && \
    echo '  user_profile_enabled: true' >> /home/agent/.hermes/config.yaml

# Set environment
ENV HERMES_HOME=/home/agent/.hermes
ENV API_SERVER_ENABLED=true
ENV API_SERVER_PORT=10000
ENV GATEWAY_ALLOW_ALL_USERS=true
ENV PORT=10000

EXPOSE 10000

CMD ["hermes", "gateway", "run"]
