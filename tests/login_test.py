from selenium import webdriver
import allure
import pytest
from pages.loginpage import loginpage
from utils import utils as utils
import time

@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        try:
            driver= self.driver
            login=loginpage(driver)
            login.email(utils.USERNAME_ADMIN)
            login.password(utils.PASSWORD)
            login.login()
            x=driver.title
            print(x)
            assert x=="SISA "

        except AssertionError as error:
            print("assertion error occured")
            print(error)
            allure.attach(self.driver.get_screenshot_as_png(),name="screenshot",attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/kruthi.p/PycharmProjects/Test_New/screenshots/"+"name"+".PNG")
            raise





    def test_logout(self):
        driver=self.driver
        driver.find_element_by_xpath("//*[@id='mobile-profile-img']/li/a/img").click()
        driver.find_element_by_xpath("//*[@id='mobile-profile-img']/li/ul/li[6]").click()





