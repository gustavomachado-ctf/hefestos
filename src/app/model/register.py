from sqlmodel import SQLModel, Field


class RegisterModel(SQLModel, table=True):
    """Modelo para cadastro de integração."""

    name: str = Field(min_length=1, max_length=100, nullable=False)
    """Nome da integração."""

    supplier_cnpj: str = Field(min_length=14, max_length=14, nullable=False)
    """CNPJ do fornecedor."""

    bucket_name: str = Field(min_length=1, max_length=100, nullable=False)
    """Bucket da integração."""

    payment_queue: str | None = Field(default=None, nullable=True, max_length=100)
    """Fila de pagamento."""

    aux_queue: str | None = Field(default=None, nullable=True, max_length=100)
    """Fila auxiliar."""

    general_queue: str | None = Field(default=None, nullable=True, max_length=100)
    """Fila geral."""

    order_queue: str | None = Field(default=None, nullable=True, max_length=100)
    """Fila de pedido."""

    auth_queue: str | None = Field(default=None, nullable=True, max_length=100)
    """Fila de autenticação."""

    ingestion_queue: str | None = Field(default=None, nullable=True, max_length=100)
    """Fila de ingestão."""

    pp_order_queue: str | None = Field(default=None, nullable=True, max_length=100)
    """Fila de pedido do Pedpreco."""

    pp_invoice_queue: str | None = Field(default=None, nullable=True, max_length=100)
    """Fila de retorno do Pedpreco."""

    job_runner_name: str | None = Field(default=None, nullable=True, max_length=100)
    """Nome do Job Runner criado para a integração."""

    use_protheus: bool = Field(default=True, nullable=False)
    """Sinalizar se a integração usa Protheus para conversão de DTOs."""
