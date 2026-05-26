from app.dto.register import RegisterDTO
from app.presenter.register import RegisterPresenter
from app.repository.register import RegisterRepository


class RegisterService:
    """
    Centralizador de lógica e regras de negócio do projeto.
    """

    def __init__(self, repository: RegisterRepository) -> None:
        self.repository = repository
        self.presenter = RegisterPresenter()

    def get(self, config_name: str | None) -> RegisterDTO | None:
        if not (model := self.repository.get(config_name=config_name)):
            return None

        return self.presenter.present(model=model)
