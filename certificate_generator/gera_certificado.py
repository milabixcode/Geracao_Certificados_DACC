from .entities import Certificate


def model_to_template_context(certificate: Certificate) -> dict:
    event = certificate.activity.event

    return {
        "nome": certificate.student.name,
        "numero_matricula": certificate.student.registration,
        "evento": event.name,
        "ano": event.year,
        "tipo_atividade": certificate.activity.kind,
        "nome_da_atividade": certificate.activity.name,
        "tempo_duracao_atividade": certificate.activity.hours_granted,
    }
