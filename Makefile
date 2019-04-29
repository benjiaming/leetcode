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

all: clean
ifndef PIP_VERSION
	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
	python get-pip.py --user
endif
	$(PIP) install --user virtualenv
	$(VIRTUALENV) venv
	. venv/bin/activate
	$(PIP) install -r requirements.txt


clean:
	@rm -rf venv

test:
	pytest
