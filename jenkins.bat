@echo off

echo Installing coverage, pylint, and flake8...
pip install coverage pylint flake8

echo Running coverage...
coverage run -m unittest test_hypot.py
echo Coverage report:
coverage report -m
coverage erase

echo Running pylint...
pylint hypot.py test_hypot.py

echo Running flake8...
flake8 hypot.py test_hypot.py

exit /b 0
