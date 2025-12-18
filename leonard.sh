#!/bin/bash

# Leonard
# My CI thing

# Good code?
echo "== Lint =="
uv run ruff check

if [ $? -ne 0 ] ; then
    echo "* ruff check failed"
    exit 1
fi

# Format
echo "== Format =="
uv run ruff format

# Run tests
echo "== Tests =="
pushd tests
uv run coverage run --source koinenlp test.py
if [ $? -ne 0 ] ; then
    echo "* Tests failed"
    exit 1
fi

# Coverage check
echo "== Test coverage =="
uv run coverage report --fail-under 100
if [ $? -ne 0 ] ; then
    echo "* Coverage fail"
    exit 1
fi
popd

# What branch?
echo "== Current branch =="
git branch
exit 0
