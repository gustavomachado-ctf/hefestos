from app.dto.bypass import ByPassDTO
from app.model.bypass import ByPassModel


class ByPassPresenter:
    """Apresentação dos dados dos desvios."""

    @staticmethod
    def present(models: list[ByPassModel]) -> list[ByPassDTO]:
        return [
            ByPassDTO(**model.model_dump())
            for model in models
        ]
