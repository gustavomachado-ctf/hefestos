from app.dto.job_runner import JobRunnerDTO
from app.model.job_runner import JobRunnerModel


class JobRunnerPresenter:
    """Apresentação dos dados dos registros."""

    @staticmethod
    def present(model: JobRunnerModel) -> JobRunnerDTO:
        return JobRunnerDTO(**model.model_dump())
