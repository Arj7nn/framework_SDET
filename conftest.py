import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    # print("launching browser")
    # yield
    # print("closing browser")
    if browser=='chrome':
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.implicitly_wait(10)
        driver.maximize_window()
        return driver
    elif browser=='Edge':
        driver = webdriver.Edge()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.implicitly_wait(10)
        driver.maximize_window()
        return driver
    else:
        driver = webdriver.Firefox()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.implicitly_wait(10)
        driver.maximize_window()
        return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")



