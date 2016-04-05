#!/bin/bash

# Leonard
# My CI thing

# Good code?
echo "== PEP8 check =="
flake8 koinenlp/*py test.py

if [ $? -ne 0 ] ; then
    echo "* PEP8 check failed"
    exit 1
fi

# Run tests
echo "== Tests =="
coverage run --source koinenlp test.py
if [ $? -ne 0 ] ; then
    echo "* Tests failed"
    exit 1
fi

# Coverage check
echo "== Test coverage =="
coverage report --fail-under 100
if [ $? -ne 0 ] ; then
    echo "* Coverage fail"
    exit 1
fi

# What branch?
echo "== Current branch =="
git branch
exit 0
