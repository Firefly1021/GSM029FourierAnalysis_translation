PYTHON ?= python
export PYTHONPATH := $(CURDIR)/src

.PHONY: status test lint inspect-template verify-template compile-template validate-project

status:
	$(PYTHON) -m mathbook status

test:
	$(PYTHON) -m unittest discover -s tests -v

lint:
	$(PYTHON) -m compileall -q src scripts tests
	$(PYTHON) -m mathbook validate-project

inspect-template:
	$(PYTHON) -m mathbook inspect-template

verify-template:
	$(PYTHON) -m mathbook verify-template

compile-template:
	$(PYTHON) -m mathbook compile-template

validate-project:
	$(PYTHON) -m mathbook validate-project

