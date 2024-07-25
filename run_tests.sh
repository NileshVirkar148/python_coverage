#!/bin/bash

# Run tests with coverage
coverage run --source=app -m unittest discover -s tests

# Generate coverage report
coverage report

# Generate lcov report
coverage lcov
