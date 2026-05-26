from pydantic import BaseModel


class RegisterRequestDTO(BaseModel):
    """Dados para cadastro de nova integração."""

    name: str
    """Nome da integração."""

    supplier_cnpj: str
    """CNPJ do fornecedor."""

    bucket_name: str = "transaction-retention-demo"
    """Bucket da integração."""

    payment_queue: str | None = None
    """Fila de pagamento."""

    aux_queue: str
    """Fila auxiliar."""

    general_queue: str
    """Fila geral."""

    order_queue: str
    """Fila de pedido."""

    auth_queue: str
    """Fila de autenticação."""

    ingestion_queue: str
    """Fila de ingestão."""

    pp_order_queue: str
    """Fila de pedido do Pedpreco."""

    pp_invoice_queue: str
    """Fila de retorno do Pedpreco."""

    job_runner_name: str | None = None
    """Nome do Job Runner criado para a integração."""

    use_protheus: bool
    """Sinalizar se a integração usa Protheus para conversão de DTOs."""
