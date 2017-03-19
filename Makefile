.PHONY: venv
venv:
	rm -rf venv
	virtualenv venv

.PHONY: dependencies
dependencies:
	@if [ ! -d venv ]; then virtualenv venv ; fi
	. venv/bin/activate && pip install -r requirements.txt

.PHONY: check-syntax
check-syntax:
	pep8 *.py
	pep8 app/*.py

.PHONY: run
run:
	@if [ ! -d venv ]; then \
		echo "venv dir not found. Please run 'make dependencies'";\
		exit 1;\
	fi
	. venv/bin/activate && python app.py

.PHONY: clean
clean:
	find . -name "*.pyc" ! -path "./venv/*" -print -delete
