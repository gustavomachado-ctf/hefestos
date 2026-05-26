from enum import StrEnum

from pydantic import BaseModel


class BypassFields(StrEnum):
    access_url = "URL_ACESSO"
    aux_code = "CODIGO_AUXILIAR"


class BypassRequestDTO(BaseModel):
    name: str
    base_config_name: str | None = None
    name_config_hecate: str
    bypass_field: BypassFields
    comparator: str = "ILIKE"
    value: str
