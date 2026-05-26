from pydantic import BaseModel


class RegisterRequestDTO(BaseModel):
    name: str
    supplier_cnpj: str
    bucket_name: str = "transaction-retention-demo"
    payment_queue: str | None = None
    aux_queue: str
    general_queue: str
    order_queue: str
    auth_queue: str
    ingestion_queue: str
    pp_order_queue: str
    pp_invoice_queue: str
    job_runne_name: str
    use_protheus: bool
