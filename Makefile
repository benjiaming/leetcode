PIP := pip
VIRTUALENV := python3 -m venv
PYTEST := venv/bin/pytest

all: clean venv

clean:
	@rm -rf venv

venv:
	$(VIRTUALENV) venv
	. venv/bin/activate && $(PIP) install -r requirements.txt


test:
	. venv/bin/activate
	mkdir -p test-reports/
	$(PYTEST) --junitxml=test-reports/junit.xml
