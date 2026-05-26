from pydantic import BaseModel


class JobRunnerRequestDTO(BaseModel):
    """Dados para cadastro de Job Runner."""

    name: str
    """Nome do Job Runner (nome da integração por padrão)."""

    task_definition_id: str
    """ID da definição de tarefa (ID padrão + nome do projeto)."""

    capacity_provider: str = "FARGATE"
    """Capacity provider utilizado (FARGATE por padrão)."""

    container_name: str
    """Nome do container."""

    subnets: str
    """Subnets utilizadas."""

    security_group: str
    """Security group utilizado."""
