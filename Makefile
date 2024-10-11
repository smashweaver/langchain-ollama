.PHONY: init, list, run, shell, diff

shell:
	@poetry shell

init: shell
	@poetry install

list:
	@poetry install --dry-run --sync --no-ansi

run:
	@poetry run python app.py

diff:
	@git --no-pager diff
