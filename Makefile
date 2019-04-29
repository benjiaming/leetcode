all: clean
	pip install --user virtualenv
	virtualenv venv
	. venv/bin/activate
	pip install -r requirements.txt

clean:
	@rm -rf venv

test:
	pytest
