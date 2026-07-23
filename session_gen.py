import secrets

def generate_session_id():
    return "sid_" + secrets.token_hex(16)

print(f"Generated Session ID: {generate_session_id()}")
