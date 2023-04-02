from docxtpl import DocxTemplate


doc = DocxTemplate("modelo_certificado.docx")
context = {
    "nome": "xuxu",
    "ano": "2012",
}  # , 'numero_matricula', 'evento', 'ano', 'tipo_atividade', 'nome_da_atividade', 'tempo_duracao_atividade' }
doc.render(context)
doc.save("certificado_gerado.docx")
