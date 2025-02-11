from pydantic import BaseModel


class VerifyRequest(BaseModel):
    email: str
    device_id: str


class SubmitRequest(BaseModel):
    token: str
