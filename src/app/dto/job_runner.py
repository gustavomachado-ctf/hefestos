from pydantic import BaseModel


class JobRunnerDTO(BaseModel):
    """Dados para cadastro de Job Runner."""

    name: str
    """Nome do Job Runner (nome da integração por padrão)."""

    task_definition_id: str
    """ID da definição de tarefa (ID padrão + nome do projeto)."""

    cluster: str
    """Cluster utilizado pela integração."""

    capacity_provider: str = "FARGATE"
    """Capacity provider utilizado (FARGATE por padrão)."""

    container_name: str
    """Nome do container."""

    subnets: str
    """Subnets utilizadas."""

    security_groups: str
    """Security group utilizado."""

    assign_public_ip: bool
    """Se a integração utiliza IP público."""
