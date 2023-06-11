from docxtpl import DocxTemplate
import os

from certificate_generator.extractor import NormalFileExtractor
from certificate_generator.gera_certificado import model_to_template_context

doc = DocxTemplate("modelo_certificado.docx")
context = {
    "nome": "xuxu",
    "ano": "2012",
}  # , 'numero_matricula', 'evento', 'ano', 'tipo_atividade', 'nome_da_atividade', 'tempo_duracao_atividade' }
doc.render(context)
doc.save("certificado_gerado.docx")


certs_path = "certificates"
for file in os.listdir(certs_path):
    os.remove(f"{certs_path}/{file}")

extractor = NormalFileExtractor()
sheets_path = "spreadsheets"

for sheet in os.listdir(sheets_path):
    sheet_path = f"{sheets_path}/{sheet}"
    certs = extractor.extract(sheet_path, "022120004")

    for cert in certs:
        ctx = model_to_template_context(cert)
        doc.render(ctx)
        doc.save(f"{certs_path}/{cert.activity.name}-{cert.activity.event.year}.docx")
