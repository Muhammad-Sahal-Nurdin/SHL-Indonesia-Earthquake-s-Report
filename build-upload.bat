@echo off
rmdir dist /S /Q
py -m build
py -m twine upload --repository pypi dist/*