from uuid import UUID

from pydantic import BaseModel


class DocumentResponse(BaseModel):

    id: UUID
    filename: str
    pages: int
    chunks: int
    status: str

    model_config = {
        "from_attributes": True
    }