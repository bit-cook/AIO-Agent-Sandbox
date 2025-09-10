#! /usr/bin/env bash

set -e

python -m build
twine upload dist/*
