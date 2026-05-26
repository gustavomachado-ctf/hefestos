from sqlmodel import SQLModel, Field


class JobRunnerModel(SQLModel, table=True):
    """Modelo para cadastro do job runner."""

    name: str = Field(min_length=1, max_length=50, nullable=False)
    """Nome do job runner."""

    task_definition_id: str = Field(min_length=1, max_length=100, nullable=False)
    """ID da definição de tarefa."""

    capacity_provider: str = Field(min_length=1, max_length=50, nullable=False)
    """Capacity provider utilizado."""

    container_name: str = Field(min_length=1, max_length=50, nullable=False)
    """Nome do container."""

    subnets: str = Field(min_length=1, max_length=100, nullable=False)
    """Subnets utilizadas."""

    security_group: str = Field(min_length=1, max_length=100, nullable=False)
    """Security group utilizado."""
