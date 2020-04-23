#!/bin/sh

pytest --pep8 -p no:warnings
pytest easy/*/tests --verbose
