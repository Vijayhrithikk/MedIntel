from uuid import UUID

from pydantic import BaseModel


class CreateProjectRequest(BaseModel):
    name: str


class ProjectResponse(BaseModel):
    id: UUID
    name: str
    description: str | None = None

    model_config = {
        "from_attributes": True
    }