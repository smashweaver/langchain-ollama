.PHONY: init, start, run

init:
	@poetry shell
	@poetry install --no-root

run: 
	@python ./app.py


start: init, run
