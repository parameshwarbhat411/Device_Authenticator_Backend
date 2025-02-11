from fastapi import FastAPI
from models import VerifyRequest
from services.auth_service import AuthService
from slowapi import Limiter
from slowapi.util import get_remote_address

# limiter = Limiter(key_func=get_remote_address)

app = FastAPI()


@app.post("/api/auth/verify")
async def verify_email_and_device(request: VerifyRequest):
    """Endpoint to verify email and device, and generate a token."""
    token = AuthService.verify_email_and_device(request.email, request.device_id)
    return {"token": token}

# @app.post("/api/auth/submit")
# async def submit_token(request: SubmitRequest):
#     """Endpoint to submit and validate the verification token."""
#     return AuthService.submit_verification_token(request.token)
