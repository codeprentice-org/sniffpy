
ROOT_DIR:=(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
REQUIREMENTS=requirements.txt

SYSTEM_PYTHON=python3

VENV_ROOT=venv
VENV_BIN=$(VENV_ROOT)/bin
VENV_PIP=$(VENV_BIN)/pip3
VENV_PYTHON=$(VENV_BIN)/python


virtualenv:
	@echo "Making virtual environment..."
	@python3 -m venv venv
	@echo "Installing all dependencies..."
	$(VENV_PIP) install --upgrade pip
	$(VENV_PIP) install -r $(REQUIREMENTS)


checkstyle:
	@echo "Checking style"
	@pylint -v  sniffpy
