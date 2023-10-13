PACKAGE_DIR=./

install:

clear-build:
	rm -r build dist rodents.egg-info	

build: 
	python -m build --sdist --wheel ${PACKAGE_DIR}

test:


deploy:
	twine upload --repository pypi ./dist/*
