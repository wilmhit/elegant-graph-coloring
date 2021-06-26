typecheck:
	pipenv run mypy graph_coloring/*.py

test:
	pipenv run pytest tests

black:
	pipenv run black  --line-length 99 .

isort:
	pipenv run isort graph_coloring
