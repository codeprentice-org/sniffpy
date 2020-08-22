
ROOT_DIR:=(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
REQUIREMENTS=requirements.txt
# Detects which OS is being used
# Only relevant for virtual environment creation
ifeq ($(OS), Windows_NT)
	SYSTEM_PYTHON=py
else
	SYSTEM_PYTHON=python3
endif

VENV_ROOT=venv
VENV_BIN=$(VENV_ROOT)/bin
VENV_PIP=$(VENV_BIN)/pip3
VENV_PYTHON=$(VENV_BIN)/python

virtualenv:
	@echo "Making virtual environment..."
	@$(SYSTEM_PYTHON) -m venv venv
	@echo "Installing all dependencies..."
	$(VENV_PIP) install --upgrade pip
	$(VENV_PIP) install -r $(REQUIREMENTS)

all:  uninstall install

install: virtualenv
	@echo "Installing sniffpy in the system"
	@$(VENV_PIP) install -e .
	@echo " "	
	@echo "/////////////////////////////////////// "
	@echo " "
	@echo "   _____       _  __  __              "
	@echo "  / ____|     (_)/ _|/ _|             "
	@echo " | (___  _ __  _| |_| |_ _ __  _   _  "
	@echo "  \___ \| '_ \| |  _|  _| '_ \| | | | "
	@echo "  ____) | | | | | | | | | |_) | |_| | "
	@echo " |_____/|_| |_|_|_| |_| | .__/ \__, | "
	@echo "                        | |     __/ | "
	@echo "                        |_|    |___/  "
	@echo " "
	@echo "/////////////////////////////////////// "
	@echo " "
	@echo " "		


uninstall:
	@echo "Uninstalling sniffpy in the system"
	$(VENV_PIP) uninstall sniffpy
	@echo "Succesfully uninstalled sniffpy"

stylecheck: base_stylecheck test_stylecheck
	@echo "Done with stylecheck"

base_stylecheck:
	@echo "Checking codebase coding style"
	@$(VENV_BIN)/pylint -v sniffpy
	@echo " "
	@echo " "
	@echo " " 

test_stylecheck:
	@echo "Checking coding style of tests" 
	@$(VENV_BIN)/pylint --rcfile .pylintrctest tests
	@echo " "
	@echo " "
	@echo " " 

test: FORCE
	$(VENV_BIN)/py.test

FORCE: ;
