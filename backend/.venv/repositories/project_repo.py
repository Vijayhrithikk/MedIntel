from uuid import UUID

from sqlalchemy.orm import Session

from database.models import Project


class ProjectRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self,name: str,description: str | None = None) -> Project:

        project = Project(
            name=name,
            description=description,
        )

        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)

        return project

    def list(self) -> list[Project]:

        return (
            self.db.query(Project)
            .order_by(Project.created_at.desc())
            .all()
        )

    def get(self,project_id: UUID) -> Project | None:

        return (
            self.db.query(Project)
            .filter(Project.id == project_id)
            .first()
        )

    def delete(self,project_id: UUID) -> bool:

        project = self.get(project_id)

        if not project:
            return False

        self.db.delete(project)
        self.db.commit()

        return True