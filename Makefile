clean: clean-pyc clean-build

pypi: clean-build sdist upload

clean-pyc:
	@echo 'Clean pyc ...'
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +
	@find . -name '.pytest_cache' -exec rm -fr {} +

clean-build:
	@echo "Clean build ..."
	@rm -rf dist/
	@rm -rf build/
	@rm -rf *.egg-info/

sdist:
	@echo "Make sdist ..."
	python3 setup.py sdist bdist_wheel

upload:
	@echo "Upload to Pypi ..."
	python3 -m twine upload dist/*

push-git:
	@echo "push github ..."
	git push -u origin master