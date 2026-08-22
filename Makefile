PYTHON ?= python
export PYTHONPATH := $(CURDIR)/src

.PHONY: test lint validate-project inspect-template verify-template compile-template \
	new-book start-book approve-sample translate-book resume finish-book status list-books isolate-worktree

test:
	$(PYTHON) -m unittest discover -s tests -v

lint:
	$(PYTHON) -m compileall -q src scripts tests

validate-project:
	$(PYTHON) -m mathbook validate-project

inspect-template:
	$(PYTHON) -m mathbook inspect-template

verify-template:
	$(PYTHON) -m mathbook verify-template

compile-template:
	$(PYTHON) -m mathbook compile-template

new-book:
	$(PYTHON) -m mathbook new-book $(BOOK) --source "$(SOURCE)"

start-book:
	$(PYTHON) -m mathbook start-book $(BOOK)

approve-sample:
	$(PYTHON) -m mathbook approve-sample $(BOOK)

translate-book:
	$(PYTHON) -m mathbook translate-book $(BOOK)

resume:
	$(PYTHON) -m mathbook resume $(BOOK)

finish-book:
	$(PYTHON) -m mathbook finish-book $(BOOK)

status:
	$(PYTHON) -m mathbook status $(BOOK)

list-books:
	$(PYTHON) -m mathbook list-books

isolate-worktree:
	$(PYTHON) -m mathbook isolate-worktree $(BOOK)
