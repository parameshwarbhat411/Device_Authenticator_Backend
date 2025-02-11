import secrets
from database import store_token
from config import Config
from datetime import datetime, timedelta


class TokenFactory:
    """ Factory for generating and storing verification tokens """

    @staticmethod
    def generate_token() -> str:
        return secrets.token_urlsafe(32)

    @staticmethod
    def create_and_persist_token(email: str, device_id: str) -> str:
        """Generates and Stores token with expiration time"""
        token = TokenFactory.generate_token()
        expires_at = datetime.now() + timedelta(minutes=Config.TOKEN_EXPIRATION_MINUTES)
        store_token(token, email, device_id, expires_at)
        return token
