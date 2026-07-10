from pydantic import BaseModel
from datetime import date, time
from typing import Optional


class InteractionCreate(BaseModel):
    hcp_id: int
    interaction_date: date
    interaction_time: time
    interaction_type: str
    attendees: Optional[str] = None
    topics_discussed: Optional[str] = None
    summary: Optional[str] = None
    sentiment: Optional[str] = None
    outcomes: Optional[str] = None
    follow_up: Optional[str] = None


class InteractionResponse(BaseModel):
    id: int
    hcp_id: int
    interaction_date: date
    interaction_time: time
    interaction_type: str
    attendees: Optional[str]
    topics_discussed: Optional[str]
    summary: Optional[str]
    sentiment: Optional[str]
    outcomes: Optional[str]
    follow_up: Optional[str]

    class Config:
        from_attributes = True