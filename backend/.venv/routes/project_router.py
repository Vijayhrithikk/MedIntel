from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.connection import get_db

from repositories.project_repo import ProjectRepository
from services.project_service import ProjectService

from schemas.project import (
    CreateProjectRequest,
    ProjectResponse,
)

router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)


def get_project_service(db: Session) -> ProjectService:
    repository = ProjectRepository(db)
    return ProjectService(repository)


@router.post("/", response_model=ProjectResponse)
def create_project(
    request: CreateProjectRequest,
    service: ProjectService = Depends(get_project_service),
):
    return service.create_project(request.name)


@router.get("/", response_model=list[ProjectResponse])
def list_projects(
    service: ProjectService = Depends(get_project_service),
):
    return service.list_projects()


@router.get("/{project_id}", response_model=ProjectResponse)
def get_project(
    project_id: UUID,
    service: ProjectService = Depends(get_project_service),
):

    project = service.get_project(project_id)

    if project is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )

    return project


@router.delete("/{project_id}")
def delete_project(
    project_id: UUID,
    service: ProjectService = Depends(get_project_service),
):

    deleted = service.delete_project(project_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )

    return {
        "message": "Project deleted successfully"
    }