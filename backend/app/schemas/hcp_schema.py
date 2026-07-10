from pydantic import BaseModel
from typing import Optional


class HCPCreate(BaseModel):
    name: str
    specialization: str
    hospital: str
    city: str


class HCPResponse(BaseModel):
    id: int
    name: str
    specialization: str
    hospital: str
    city: str

    class Config:
        from_attributes = True