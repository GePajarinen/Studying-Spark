install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=hello --cov=greeting tests
	python -m pytest --nbval Notebook_for_testing.ipynb

format:
	black *.py

lint:
	pylint --disable=R, C hello.py

debugger:	
	python -m pytest -vv --pdb 

all: install format lint test
