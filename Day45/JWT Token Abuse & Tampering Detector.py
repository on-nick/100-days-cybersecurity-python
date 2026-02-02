import base64
import json
import time

SUSPICIOUS_ALGOS = ["none"]
REUSED_TOKEN_LIMIT = 3
TIME_WINDOW = 60

token_usage = {}

def decode_part(part):
    padding = '=' * (-len(part) % 4)
    return json.loads(base64.urlsafe_b64decode(part + padding))

print("JWT Abuse Detection Engine Started")

while True:
    token = input("\nJWT Token: ").strip()
    now = time.time()

    try:
        header_b64, payload_b64, signature = token.split(".")
        header = decode_part(header_b64)
        payload = decode_part(payload_b64)
    except:
        print("[ERROR] Invalid JWT format")
        continue

    if header.get("alg") in SUSPICIOUS_ALGOS:
        print("[ALERT] Insecure JWT algorithm detected")

    jti = payload.get("jti", token)
    token_usage.setdefault(jti, []).append(now)

    token_usage[jti] = [t for t in token_usage[jti] if now - t <= TIME_WINDOW]

    if len(token_usage[jti]) >= REUSED_TOKEN_LIMIT:
        print("[CRITICAL] JWT replay attack detected")
        break

    if payload.get("exp") and payload["exp"] < now:
        print("[ALERT] Expired JWT token used")

    print("Token analyzed successfully")
