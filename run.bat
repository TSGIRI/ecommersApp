@echo off
cd C:\Users\Admin\PycharmProjects\ecommersApp
call .venv\Scripts\activate
python -m pytest -s -v --html=Reports/report.html --browser chrome
pause