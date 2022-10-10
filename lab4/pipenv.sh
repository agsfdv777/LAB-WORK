#!/usr/bin/env bash
pipenv --python 3.10
pipenv --venv
pipenv run python -V
pipenv install requests