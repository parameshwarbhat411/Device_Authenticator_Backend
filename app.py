from fastapi import FastAPI, HTTPException
from starlette import status

from models import VerifyRequest
from services.auth_service import AuthService
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["Authorization", "Content-Type"],
)


@app.post("/api/auth/verify")
async def verify_email_and_generateToken(request: VerifyRequest):
    """Endpoint to verify email and device, and generate a token."""
    token, expires_at = AuthService.verify_email_and_generateToken(request.email, request.device_id)
    return {"token": token, "expires_at": expires_at}


@app.get("/api/protected")
def get_protected(token: str, device_id: str):
    """
    Example protected route that requires a valid, unexpired token
    *and* the matching device_id.
    """
    if not AuthService.validate_device_token(token, device_id):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token or device")

    return {"message": "You have accessed a protected resource!"}
