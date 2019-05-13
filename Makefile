PIP_VERSION := $(shell pip --version 2>/dev/null)
ifdef PIP_VERSION
PIP := pip
VIRTUALENV := virtualenv
PYTEST := pytest
else
LOCAL_PATH := ~/.local/bin
PIP := . venv/bin/activate && pip
VIRTUALENV := $(LOCAL_PATH)/virtualenv
PYTEST := $(LOCAL_PATH)/pytest
endif

all: clean
	$(PIP) install --user virtualenv
	$(VIRTUALENV) venv
	$(PIP) install --user -r requirements.txt

clean:
	@rm -rf venv

test:
	. venv/bin/activate
	mkdir -p test-reports/
	$(PYTEST) --junitxml=test-reports/junit.xml
