@echo off

REM ✅ Activate your virtual environment
call C:\Users\mahaj\PycharmProjects\pythonselenium\venv\Scripts\activate.bat

REM ✅ Run pytest with full absolute paths
python -m pytest -v -s ^
--html=C:\Users\mahaj\PycharmProjects\pythonselenium\OrangeHRMFramework\Reports\orangereport.html ^
C:\Users\mahaj\PycharmProjects\pythonselenium\OrangeHRMFramework\TestFilesOrangeHRM\test_loginOrangeHRM.py --browser chrome

pause

