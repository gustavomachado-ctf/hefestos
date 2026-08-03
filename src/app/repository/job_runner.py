from sqlmodel import Session, select

from app.dto.job_runner import JobRunnerDTO
from app.model.job_runner import JobRunnerModel


class JobRunnerRepository:
    """
    Serviço de banco de dados que utiliza o SQLModel e SQLAlchemy.
    """

    def __init__(self, session: Session) -> None:
        self.session = session

    def get(self, config_name: str | None) -> list[JobRunnerModel] | None:
        try:
            statement = select(JobRunnerModel)

            if config_name:
                statement = select(JobRunnerModel).where(JobRunnerModel.name == config_name)

            return self.session.exec(statement).all() or None

        except Exception:
            self.session.rollback()
            raise

    def create(self, data: JobRunnerDTO) -> list[JobRunnerModel] | None:
        try:
            model = JobRunnerModel(**data.model_dump())

            self.session.add(model)
            self.session.commit()
            self.session.refresh(model)

            return model or None

        except Exception:
            self.session.rollback()
            raise
