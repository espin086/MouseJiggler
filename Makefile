PACKAGE_DIR=./

install:
	pip install .

clear-build:
	rm -r build dist rodents.egg-info	

build: 
	python -m build --sdist --wheel ${PACKAGE_DIR}

test:
	test pytest

deploy: build
	twine upload --repository pypi ./dist/*

.PHONY: help install clear-build build test deploy

help:
	@echo "Available commands:"
	@echo "  make install       Install the package"
	@echo "  make clear-build   Remove build artifacts"
	@echo "  make build         Build the package"
	@echo "  make test          Run tests"
	@echo "  make deploy        Deploy the package to PyPI"
