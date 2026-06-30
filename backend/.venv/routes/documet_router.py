from pathlib import Path
from shutil import copyfileobj
from uuid import UUID

from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from database.connection import get_db

from repositories.document_repo import DocumentRepository

from services.document_service import DocumentService
from services.ingest import IngestionService

from schemas.document import DocumentResponse

router = APIRouter(
    prefix="/projects",
    tags=["Documents"],
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@router.get(
    "/{project_id}/documents",
    response_model=list[DocumentResponse],
)
def list_documents(
    project_id: UUID,
    db: Session = Depends(get_db),
):

    repository = DocumentRepository(db)
    service = DocumentService(repository)

    return service.list_documents(project_id)

@router.post("/{project_id}/upload")
async def upload_document(
    project_id: UUID,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):

    repository = DocumentRepository(db)

    document_service = DocumentService(repository)
    ingestion_service = IngestionService(repository)

    destination = UPLOAD_DIR / file.filename

    with destination.open("wb") as buffer:
        copyfileobj(file.file, buffer)

    document = document_service.create_document(
        project_id=project_id,
        filename=file.filename,
        filepath=str(destination),
    )

    result = ingestion_service.ingest(
        document_id=document.id,
        pdf_path=str(destination),
    )

    return {
        "document_id": document.id,
        **result,
    }