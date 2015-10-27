#!/bin/bash
set -e
echo "Running status code tests"
python tests.py
echo "Running doctest"
python -m doctest -v status.py
