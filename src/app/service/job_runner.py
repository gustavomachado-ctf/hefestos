from app.dto.job_runner import JobRunnerDTO
from app.presenter.job_runner import JobRunnerPresenter
from app.repository.job_runner import JobRunnerRepository


class JobRunnerService:
    """
    Centralizador de lógica e regras de negócio do projeto.
    """

    def __init__(self, repository: JobRunnerRepository) -> None:
        self.repository = repository
        self.presenter = JobRunnerPresenter()

    def get_found_runners(self, config_name: str | None) -> JobRunnerDTO | None:
        if not (model := self.repository.get(config_name=config_name)):
            return None

        return self.presenter.present(model=model)

    def register_runner(self, data: JobRunnerDTO):
        if not (model := self.repository.create(data=data)):
            return None

        return self.presenter.present(model=model)
