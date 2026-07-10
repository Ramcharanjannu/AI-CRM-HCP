from fastapi import APIRouter
from pydantic import BaseModel

from app.ai.agent import run_agent

router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)


class AIRequest(BaseModel):
    tool: str
    message: str


@router.post("/chat")
def ai_chat(request: AIRequest):

    response = run_agent(
        request.message,
        request.tool
    )

    return {
        "response": response
    }