from pydantic import BaseModel


class VerifyRequest(BaseModel):
    email: str
    device_id: str

