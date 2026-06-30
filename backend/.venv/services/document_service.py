from uuid import UUID

from repositories.document_repo import DocumentRepository


class DocumentService:

    def __init__(self, repository: DocumentRepository):
        self.repository = repository

    def create_document(
        self,
        project_id: UUID,
        filename: str,
        filepath: str,
    ):

        return self.repository.create(
            project_id,
            filename,
            filepath,
        )

    def mark_ready(
        self,
        document_id: UUID,
        pages: int,
        chunks: int,
        is_scanned: bool,
    ):

        return self.repository.update_status(
            document_id=document_id,
            status="READY",
            pages=pages,
            chunks=chunks,
            is_scanned=is_scanned,
        )

    def mark_failed(self,document_id: UUID):

        return self.repository.update_status(
            document_id=document_id,
            status="FAILED",
        )

    def list_documents(self,project_id: UUID):

        return self.repository.get_by_project(project_id)