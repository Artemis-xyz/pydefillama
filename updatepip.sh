#!/bin/bash
./clean.sh
python setup.py sdist bdist_wheel
twine upload --repository-url https://upload.pypi.org/legacy/ dist/* --verbose