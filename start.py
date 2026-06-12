#!/usr/bin/env python3
import os, subprocess

# Create config
os.makedirs('/root/.hermes', exist_ok=True)
config = "gateway:
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
"
with open('/root/.hermes/config.yaml', 'w') as f:
    f.write(config)

# Write API key from env var to .env file
api_key = os.environ.get('OPENROUTER_API_KEY', '')
if api_key:
    env_line = 'OPENROUTER_API_KEY=' + api_key
    with open('/root/.hermes/.env', 'w') as f:
        f.write(env_line + chr(10))
    print('API key written to .env')
else:
    print('WARNING: No OPENROUTER_API_KEY set')

# Start hermes gateway
print('Starting Hermes gateway...')
os.execvp('hermes', ['hermes', 'gateway', 'run'])
