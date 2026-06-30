from uuid import UUID

from sqlalchemy.orm import Session

from database.models import Document


class DocumentRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        project_id: UUID,
        filename: str,
        filepath: str,
    ) -> Document:

        document = Document(
            project_id=project_id,
            filename=filename,
            filepath=filepath,
            status="INDEXING",
            pages=0,
            chunks=0,
            is_scanned=False,
        )

        self.db.add(document)
        self.db.commit()
        self.db.refresh(document)

        return document

    def update_status(
        self,
        document_id: UUID,
        status: str,
        pages: int = 0,
        chunks: int = 0,
        is_scanned: bool = False,
    ) -> Document:

        document = self.get_by_id(document_id)

        document.status = status
        document.pages = pages
        document.chunks = chunks
        document.is_scanned = is_scanned

        self.db.commit()
        self.db.refresh(document)

        return document

    def get_by_id(self, document_id: UUID):

        return (
            self.db.query(Document)
            .filter(Document.id == document_id)
            .first()
        )

    def get_by_project(self, project_id: UUID):

        return (
            self.db.query(Document)
            .filter(Document.project_id == project_id)
            .all()
        )