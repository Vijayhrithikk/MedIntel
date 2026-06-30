from uuid import UUID

from repositories.document_repo import DocumentRepository

from rag.pdf_parser import extract_text
from rag.chunker import chunk_text
from rag.vectorstore import vectorstore

from core.enums import DocumentStatus


class IngestionService:

    def __init__(self, document_repository: DocumentRepository):
        self.document_repository = document_repository

    def ingest(
        self,
        document_id: UUID,
        pdf_path: str,
    ):

        info = extract_text(pdf_path)

        chunks = chunk_text(info["text"])
        for chunk in chunks:
            chunk.metadata["document_id"] = str(document_id)

        vectorstore.add_documents(chunks)

        self.document_repository.update_status(
            document_id=document_id,
            status=DocumentStatus.READY.value,
            pages=info["pages"],
            chunks=len(chunks),
            is_scanned=info.get("is_scanned", False),
        )

        return {
            "status": "success",
            "pages": info["pages"],
            "chunks": len(chunks),
        }