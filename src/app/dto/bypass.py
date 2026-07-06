from pydantic import BaseModel

from app.enums.bypass import BypassFieldsEnum


class ByPassDTO(BaseModel):
    """Dados para cadastro de desvio."""

    name: str
    """Nome do desvio (nome integração + campo utilizado no desvio)."""

    base_config_name: str | None = None
    """Nome da integração base a ser utilizada como referência."""

    config_name: str
    """Nome da configuração no Hecate."""

    field: BypassFieldsEnum
    """Campo de onde o desvio pode ser passado para a integração."""

    comparator: str = "ILIKE"
    """Comparador a ser utilizado no campo para verificar o valor."""

    value: str
    """flag do desvio que será verificada."""

    regexp_find: str | None = None
    """Eventual regex de validação."""
