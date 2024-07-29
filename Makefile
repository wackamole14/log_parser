.PHONY: test

run:
	python log_parser.py $(file) $(start) $(end) $(host)

test:
	python -m unittest discover -s tests
