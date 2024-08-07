# Makefile for kom_python_logging

# Variables
PACKAGE_NAME = kom_python_logging
PYTHON = pipenv run python3
PIPENV = pipenv
TEST_DIR = tests

# Help target
.PHONY: help
help:
	@echo "Makefile for $(PACKAGE_NAME)"
	@echo ""
	@echo "Usage:"
	@echo "  make <target>"
	@echo ""
	@echo "Targets:"
	@echo "  help                Display this help message"
	@echo "  install             Install package and dependencies"
	@echo "  uninstall           Uninstall the package"
	@echo "  test                Run unit tests"
	@echo "  clean               Remove temporary files and build artifacts"
	@echo "  lint                Run linter (flake8)"
	@echo "  format              Format code (black)"
	@echo "  build               Build the package"
	@echo "  release             Release the package to GitHub Packages"
	@echo ""

# Install package and dependencies
.PHONY: install
install:
	$(PIPENV) install --dev

# Uninstall package
.PHONY: uninstall
uninstall:
	$(PIPENV) --rm

# Run unit tests
.PHONY: test
test:
	$(PYTHON) -m pytest $(TEST_DIR)

# Clean temporary files and build artifacts
.PHONY: clean
clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -rf {} +
	rm -rf build dist *.egg-info

# Run linter (flake8)
.PHONY: lint
lint:
	$(PIPENV) run flake8 src $(TEST_DIR)

# Format code (black)
.PHONY: format
format:
	$(PIPENV) run black src $(TEST_DIR)

# Build the package
.PHONY: build
build:
	$(PYTHON) setup.py sdist bdist_wheel

# Release the package to GitHub Packages
.PHONY: release
release: build
	$(PIPENV) run twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
