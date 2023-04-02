run :=poetry run

fmt:
	$(run) black .

run:
	$(run) python -m certificate_generator

drive:
	$(run) python -m certificate_generator.drive