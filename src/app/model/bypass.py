from sqlmodel import SQLModel, Field


class ByPassModel(SQLModel, table=True):
    """Modelo para cadastrar desvio."""

    name: str = Field(min_length=1, max_length=50, nullable=False)
    """Nome do desvio."""

    base_config_name: str | None = Field(default=None, nullable=True, max_length=50)
    """Nome da configuração base."""

    name_config_hecate: str = Field(min_length=1, max_length=50, nullable=False)
    """Nome da configuração no Hecate."""

    comparator: str = Field(min_length=1, max_length=50, nullable=False)
    """Comparador a ser utilizado no campo para verificar o valor."""

    deviation_flag: str = Field(min_length=1, max_length=50, nullable=False)
    """flag do desvio que será verificada."""
