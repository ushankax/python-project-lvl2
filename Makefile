configure:
	@poetry install
lint:
	@poetry run flake8 gendiff
selfcheck:
	@poetry check
check: selfcheck lint
