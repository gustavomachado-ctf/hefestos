from app.dto.bypass import ByPassDTO
from app.presenter.bypass import ByPassPresenter
from app.repository.bypass import ByPassRepository


class ByPassService:
    """
    Centralizador de lógica e regras de negócio do projeto.
    """

    def __init__(self, repository: ByPassRepository) -> None:
        self.repository = repository
        self.presenter = ByPassPresenter()

    def get_found_deviations(self, config_name: str | None) -> list[ByPassDTO] | None:
        if not (model := self.repository.get(config_name=config_name)):
            return None

        return self.presenter.present(models=model)

    def register_deviation(self, data: ByPassDTO) -> list[ByPassDTO] | None:
        if not (model := self.repository.create(data=data)):
            return None

        return self.presenter.present(models=model)
