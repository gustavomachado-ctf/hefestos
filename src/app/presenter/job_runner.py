from app.dto.job_runner import JobRunnerDTO
from app.model.job_runner import JobRunnerModel


class JobRunnerPresenter:
    """Apresentação dos dados dos registros."""

    @staticmethod
    def present(models: list[JobRunnerModel]) -> list[JobRunnerDTO]:
        return [
            JobRunnerDTO(**model.model_dump())
            for model in models
        ]
