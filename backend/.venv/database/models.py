import uuid
from datetime import datetime

from sqlalchemy import (
    String,
    Integer,
    Boolean,
    DateTime,
    ForeignKey,
)

from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.connection import Base


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)

    name: Mapped[str] = mapped_column(String(255))

    description: Mapped[str | None]

    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    documents = relationship("Document", back_populates="project")


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)

    project_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("projects.id")
    )

    filename: Mapped[str]

    filepath: Mapped[str]

    pages: Mapped[int]

    chunks: Mapped[int]

    is_scanned: Mapped[bool] = mapped_column(default=False)

    status: Mapped[str] = mapped_column(default="INDEXING")

    uploaded_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    project = relationship("Project", back_populates="documents")


class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)

    project_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("projects.id")
    )

    role: Mapped[str]

    content: Mapped[str]

    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)

    email: Mapped[str] = mapped_column(unique=True)

    name: Mapped[str]

    picture: Mapped[str | None]