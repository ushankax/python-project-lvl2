install:
	@poetry install

lint:
	@poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck lint

test:
    poetry run pytest --cov=gendiff tests/ --cov-report xml

.PHONY: install lint selfcheck check build