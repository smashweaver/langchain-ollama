.PHONY: init, lis, run

init:
	@poetry install

list:
	@poetry install --dry-run --sync --no-ansi

run:
	@poetry run python app.py
