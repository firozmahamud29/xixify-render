#!/usr/bin/env python3
import os

print("Starting Xixify Agent...", flush=True)

os.makedirs("/root/.hermes", exist_ok=True)

config_lines = [
    "gateway:",
    "  api_server:",
    "    enabled: true",
    "    host: 0.0.0.0",
    "    port: 10000",
    "    key: xixify-agent-2026",
    "approvals:",
    "  mode: off",
    "memory:",
    "  memory_enabled: true",
    "  user_profile_enabled: true",
    "model:",
    "  provider: openrouter",
]

with open("/root/.hermes/config.yaml", "w") as f:
    f.write(chr(10).join(config_lines) + chr(10))

print("Config written. Starting gateway...", flush=True)
os.execvp("hermes", ["hermes", "gateway", "run"])