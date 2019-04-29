PIP_VERSION := $(shell pip --version 2>/dev/null)

all: clean
ifndef PIP_VERSION
	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
	sudo python get-pip.py --user
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
