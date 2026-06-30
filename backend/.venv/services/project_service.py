from uuid import UUID

from repositories.project_repo import ProjectRepository


class ProjectService:

    def __init__(self, repo: ProjectRepository):
        self.repo = repo

    def create_project(self,name: str,description: str | None = None):

        return self.repo.create(
            name,
            description,
        )

    def list_projects(self):

        return self.repo.list()

    def get_project(self,project_id: UUID):

        return self.repo.get(project_id)

    def delete_project(self,project_id: UUID):

        return self.repo.delete(project_id)