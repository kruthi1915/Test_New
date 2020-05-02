import pytest
from utils import utils as utils
def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",help="type in browser_name")


@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    browser=request.config.getoption("--browser")
    if browser=='chrome':
        driver = webdriver.Chrome(executable_path="C:/Users/kruthi.p/PycharmProjects/Test_New/drivers/chromedriver.exe")
        driver.get(utils.EOTS_URL)
        driver.find_element_by_id("details-button").click()
        driver.find_element_by_id("proceed-link").click()
    elif browser=='firefox':
        driver = webdriver.Firefox(executable_path="C:/Users/kruthi.p/PycharmProjects/Test_New/drivers/geckodriver.exe")
        driver.get(utils.EOTS_URL)


    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()
    driver.quit()