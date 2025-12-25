import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import Login_Page
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

# execute the test cases with marker
# pytest -m "sanity"  --> runs all sanity test cases
# pytest -s -v -m "sanity" --html=Reports\report.html testCases/test_login_data_driven.py --browser chrome
class Test_001_Login:

    # Read the data from config file   (from utilities.readProperties import ReadConfig)
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    invalid_email = ReadConfig.getInvaliduseremail()
    logger = LogGen.log_gen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        #self.driver = webdriver.Chrome()
        self.logger.info("***************** Test_001_Login ********************")
        self.logger.info("***************** Verify Home Page Title ********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(5)
        act_title = self.driver.title
        if act_title == "Your Store":
            assert True
            self.driver.close()
            self.logger.info("***************** Home Page Title is Pass ********************")
        else:
            self.logger.error("***************** Home Page Title is Fail ********************")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_Valid_Login(self,setup):
        self.logger.info("***************** Verify Login Test ********************")
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(5)
        self.lp = Login_Page(self.driver)  # create a object for LoginPage
        self.lp.clickMyAccountLink()
        self.lp.clickLoginLink()
        self.lp.setEmail(self.useremail)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(2)
        act_title = self.driver.title
        if act_title == "My Account":
            assert True
            self.logger.info("***************** Login Test is Pass ********************")
            self.lp.clickLogout()
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_Valid_Login.png")
            self.driver.close()
            self.logger.info("***************** Login test is Fail ********************")
            assert False

    @pytest.mark.sanity
    def test_InValid_Login(self,setup):
        self.logger.info("***************** Verify invalid Login Test ********************")
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(5)
        self.lp = Login_Page(self.driver)  # create a object for LoginPage
        self.lp.clickMyAccountLink()
        self.lp.clickLoginLink()
        self.lp.setEmail(self.invalied_email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(2)
        error_message = self.driver.find_element(By.XPATH, "//div[contains(@class, 'alert-danger') and contains(text(), 'Warning:')]").text
        if error_message == "Warning: No match for E-Mail Address and/or Password." or error_message == "Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour.":
            assert True
            self.logger.info("***************** invalid Login Test is Pass ********************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_InValid_Login.png")
            self.driver.close()
            self.logger.info("***************** invalid Login test is Fail ********************")
            assert False




