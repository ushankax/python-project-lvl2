configure:
	@poetry install
lint:
	@poetry run flake8 gendiff

check: selfcheck test lint
