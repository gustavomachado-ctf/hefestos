from app.dto.register import RegisterDTO
from app.model.register import RegisterModel


class RegisterPresenter:

    @staticmethod
    def present(model: RegisterModel) -> RegisterDTO:
        return RegisterDTO(
            name=model.name,
            supplier_cnpj=model.supplier_cnpj,
            bucket_name=model.bucket_name,
            payment_queue=model.payment_queue,
            aux_queue=model.aux_queue,
            general_queue=model.general_queue,
            order_queue=model.order_queue,
            auth_queue=model.auth_queue,
            ingestion_queue=model.ingestion_queue,
            pp_order_queue=model.pp_order_queue,
            pp_invoice_queue=model.pp_invoice_queue,
            job_runner_name=model.job_runner_name,
            use_protheus=model.use_protheus,
        )
