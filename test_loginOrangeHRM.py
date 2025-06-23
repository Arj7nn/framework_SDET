import pytest


from PYTESTDEMO1.modules1.logger import get_logger
from OrangeHRMFramework.PageobjectOrangeHRM.OrangeHRMLogin import LoginPageOrange


class TestLogin:
    def test_login(self,setup):
        logger=get_logger()
        logger.info("launching browser")
        self.driver=setup
        logger.info("Naviagate to login page")
        user=LoginPageOrange(self.driver)
        logger.info("Enter the username and password")
        user.setusername("Admin")
        user.setpassword("admin123")
        logger.info("Login the page")
        user.clickbutton()

        expected_title="OrangeHRM"
        actual_title=self.driver.title
        try:
            assert expected_title==actual_title
            print("Test Passesd")
            logger.info("Test passes actual title matches expected title")
        except:
            print("test Failed")
            logger.error("Test failed actual title is not matching with expected")
# C:\Users\mahaj\PycharmProjects\pythonselenium\OrangeHRMFramework\TestFilesOrangeHRM\test_loginOrangeHRM.py
# pytest -v -s --html=PYTESTDEMO1\modules1\report.html PYTESTDEMO1\modules1\test_guru.py --browser chrome
