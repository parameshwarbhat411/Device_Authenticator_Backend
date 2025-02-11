from typing import Dict
from fastapi import HTTPException, status
from database import get_token, delete_token
from services.token_factory import TokenFactory
from datetime import datetime


class AuthService:
    """Service class to handle authentication logic."""

    @staticmethod
    def verify_email_and_device(email: str, device_id: str) -> str:
        """Verifies the email and device, then generates a token."""
        return TokenFactory.create_and_persist_token(email, device_id)

    # @staticmethod
    # def submit_verification_token(token: str) -> Dict:
    #     """Validates the token and returns the associated email."""
    #     token_data = get_token(token)
    #
    #     if not token_data:
    #         raise HTTPException(
    #             status_code=status.HTTP_400_BAD_REQUEST,
    #             detail="Invalid or expired token.",
    #         )
    #
    #     if token_data["expires_at"] < datetime.now():
    #         delete_token(token)
    #         raise HTTPException(
    #             status_code=status.HTTP_400_BAD_REQUEST,
    #             detail="Token has expired.",
    #         )
    #
    #     # Clean up the token after use
    #     delete_token(token)
    #     return {"email": token_data["email"]}
