@echo off

REM Install all dependencies from requirements.txt
echo Installing dependencies...
pip install -r requirements.txt

REM Run coverage
echo Running coverage...
coverage run -m unittest test_hypot.py
echo Coverage report:
coverage report -m
coverage erase

REM Run pylint and flake8
echo Running pylint...
pylint hypot.py test_hypot.py

echo Running flake8...
flake8 hypot.py test_hypot.py

exit /b 0
