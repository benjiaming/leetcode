PIP_VERSION := $(shell pip --version 2>/dev/null)
LOCAL_PIP := ~/.local/bin/pip
LOCAL_VIRTUALENV := ~/.local/bin/virtualenv


all: clean
# TODO: refactor
ifndef PIP_VERSION
	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
	python get-pip.py --user
	$(LOCAL_PIP) install --user virtualenv
	$(LOCAL_VIRTUALENV) venv
	. venv/bin/activate
	$(LOCAL_PIP) install -r requirements.txt --user
else
	pip install --user virtualenv
	virtualenv venv
	. venv/bin/activate
	pip install -r requirements.txt
endif

clean:
	@rm -rf venv

test:
	pytest
