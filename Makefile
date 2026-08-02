.PHONY: validate readme

validate:
	python scripts/validate_catalog.py

readme:
	python scripts/generate_readme.py
