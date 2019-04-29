PIP_VERSION := $(shell pip --version 2>/dev/null)
ifdef PIP_VERSION
PIP := pip
VIRTUALENV := virtualenv
PYTEST := pytest
else
LOCAL_PATH := ~/.local/bin
PIP := $(LOCAL_PATH)/pip
VIRTUALENV := $(LOCAL_PATH)/virtualenv
PYTEST := $(LOCAL_PATH)/pytest
endif

all: clean circleci
	$(PIP) install --user virtualenv
	$(VIRTUALENV) venv
	. venv/bin/activate
	$(PIP) install --user -r requirements.txt

circleci:
ifndef PIP_VERSION
	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
	python get-pip.py --user
endif

clean:
	@rm -rf venv

test:
	$(PYTEST)
