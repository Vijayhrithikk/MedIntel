from fastapi import APIRouter
from pydantic import BaseModel

from services.chat_service import ChatService

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


class ChatRequest(BaseModel):
    question: str


@router.post("/")
def chat(request: ChatRequest):

    service = ChatService()

    return service.ask(request.question)