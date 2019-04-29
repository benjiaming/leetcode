PIP_VERSION := $(shell pip --version 2>/dev/null)
PATH := $(PATH):~/.local/bin/

all: clean
ifndef PIP_VERSION
	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
	python get-pip.py --user
	find ~ -name pip
endif
	echo "PATH is $(PATH)"
	~/.local/bin/pip install --user virtualenv
	virtualenv venv
	. venv/bin/activate
	~/.local/bin/pip install -r requirements.txt

clean:
	@rm -rf venv

test:
	pytest
