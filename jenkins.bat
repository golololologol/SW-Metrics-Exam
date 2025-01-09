@echo off

echo Installing coverage...
pip install coverage

echo Running coverage...
coverage run -m unittest test_hypot.py
echo Coverage report:
coverage report -m
coverage erase

exit /b 0
