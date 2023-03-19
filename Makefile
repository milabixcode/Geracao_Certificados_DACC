run :=poetry run

fmt:
	$(run) black .

run:
	$(run) python -m certificate_generator.gera_certificado

drive:
	$(run) python -m certificate_generator.drive