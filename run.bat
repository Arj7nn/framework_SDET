@echo off

REM ✅ Step 1: Activate virtual environment
call C:\Users\mahaj\PycharmProjects\pythonselenium\venv\Scripts\activate.bat

REM ✅ Step 2: Run pytest with your provided correct paths
python -m pytest -v -s --html=OrangeHRMFramework\Reports\orangereport.html OrangeHRMFramework\TestFilesOrangeHRM\test_loginOrangeHRM.py --browser chrome

pause

