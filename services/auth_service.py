from services.token_factory import TokenFactory


class AuthService:
    """Service class to handle authentication logic."""

    @staticmethod
    def verify_email_and_generateToken(email: str, device_id: str) -> tuple:
        """Verifies the email and device, then generates a token."""
        return TokenFactory.create_and_persist_token(email, device_id)

    @staticmethod
    def validate_device_token(token: str, device_id: str) -> bool:
        return TokenFactory.validate_device_token(token, device_id)
