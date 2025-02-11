from datetime import datetime
from typing import Dict, Optional

verification_token: Dict[str, Dict] = {}


def store_token(token: str, email: str, device_id: str, expires_at: datetime) -> None:
    verification_token[token] = {"email": email, "device_id": device_id, "expires_at": expires_at}


def get_token(token: str) -> Dict:
    if token in verification_token:
        return verification_token[token]


def delete_token(token: str) -> None:
    if token in verification_token:
        del verification_token[token]


def find_token_by_email_and_device(email: str, device_id: str) -> Optional[str]:
    """Finds a token for a given email and device ID."""
    for token, data in verification_token.items():
        if data["email"] == email and data["device_id"] == device_id:
            return token
    return None
