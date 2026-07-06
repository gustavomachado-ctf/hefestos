from app.dto.register import RegisterDTO
from app.model.register import RegisterBaseModel


class RegisterPresenter:
    """Apresentação dos dados dos registros."""

    @staticmethod
    def present(models: list[RegisterBaseModel]) -> list[RegisterDTO]:
        return [
            RegisterDTO(**model.model_dump())
            for model in models
        ]
