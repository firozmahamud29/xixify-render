#!/usr/bin/env python3
import os, sys, traceback

print("DEBUG: start.py running", flush=True)
print("DEBUG: Python version:", sys.version, flush=True)
print("DEBUG: CWD:", os.getcwd(), flush=True)
print("DEBUG: ENV keys:", list(os.environ.keys())[:20], flush=True)

api_key = os.environ.get("OPENROUTER_API_KEY", "")
print("DEBUG: API key present:", bool(api_key), flush=True)

try:
    os.makedirs("/root/.hermes", exist_ok=True)
    print("DEBUG: Created /root/.hermes", flush=True)

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
    print("DEBUG: Config written", flush=True)

    if api_key:
        with open("/root/.hermes/.env", "w") as f:
            f.write("OPENROUTER_API_KEY=*** + api_key + chr(10))
        print("DEBUG: .env written", flush=True)

    print("DEBUG: Starting hermes gateway run...", flush=True)
    os.execvp("hermes", ["hermes", "gateway", "run"])

except Exception as e:
    print("ERROR:", e, flush=True)
    traceback.print_exc()