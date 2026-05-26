from app.dto.register import RegisterDTO
from app.model.register import RegisterModel


class RegisterPresenter:
    """Apresentação dos dados dos registros."""

    @staticmethod
    def present(model: RegisterModel) -> RegisterDTO:
        return RegisterDTO(**model.model_dump())
