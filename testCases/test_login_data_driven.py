import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import Login_Page
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import excelUtils


class Test_002_Login_data_driven:

    # Read the data from config file   (from utilities.readProperties import ReadConfig)
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.log_gen()
    path = ".//TestData//login_data.xlsx"
    status_list = []

    @pytest.mark.sanity
    def test_Valid_Login_data_driven(self,setup):
        self.logger.info("***************** Verify Login Test ********************")
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(5)
        self.lp = Login_Page(self.driver)  # create a object for LoginPage

        self.rows = excelUtils.get_row_count(self.path,"Sheet1")
        print("number of rows: ",self.rows)
        self.columns = excelUtils.get_column_count(self.path,"Sheet1")
        print(("number of columns: ",self.columns))


        for r in range(2, self.rows+1):
            self.useremail = excelUtils.read_data(self.path,"Sheet1",r,1)
            self.password = excelUtils.read_data(self.path,"Sheet1",r,2)
            self.exp_login = excelUtils.read_data(self.path,"Sheet1",r,3)

            self.lp.clickMyAccountLink()
            self.lp.clickLoginLink()
            self.lp.setEmail(self.useremail)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(2)
            act_title = self.driver.title
            exp_title = "My Account"

            if act_title == exp_title:
                if self.exp_login == "Pass":
                    self.logger.info("***************** Login Test is Pass ********************")
                    self.status_list.append("pass")
                    actual = "pass"
                    self.lp.clickLogout()
                elif self.exp_login == "Fail":
                    self.logger.info("***************** Login Test is Fail ********************")
                    self.status_list.append("Fail")
                    actual = "Fail"
                    self.lp.clickLogout()
            elif act_title != exp_title:
                if self.exp_login == "pass":
                    self.logger.info("***************** Login Test is Fail ********************")
                    self.status_list.append("Fail")
                    actual = "Fail"
                elif self.exp_login == "Fail":
                    self.logger.info("***************** Login Test is Fail ********************")
                    self.status_list.append("pass")
                    actual = "pass"

            excelUtils.write_data(self.path,"Sheet1",r,4,actual)


        self.logger.info("***************** End of Login DDT Test ********************")
        self.logger.info("***************** Completed test_Valid_Login_data_driven ********************")
        self.driver.quit()





'''            
            if act_title == exp_title:
                print(self.exp_login)
                if self.exp_login == "pass":
                    self.logger.info("***************** Login Test is Pass ********************")
                    self.status_list.append("Pass")
                    self.lp.clickLogout()
                elif self.exp_login == "Fail":
                    self.logger.info("***************** Login Test is Fail ********************")
                    self.status_list.append("Fail")
                    self.lp.clickLogout()
            elif act_title != exp_title:
                if self.exp_login == "pass":
                    self.logger.info("***************** Login Test is Fail ********************")
                    self.status_list.append("Fail")
                elif self.exp_login == "Fail":
                    self.logger.info("***************** Login Test is Pass ********************")
                    self.status_list.append("pass")

        print("Status List is: ",self.status_list)

        if "fail" not in self.status_list:
            self.logger.info("***************** Login DDt test is Pass ********************")
            self.driver.close()
            assert True
        else:
            self.logger.info("***************** Login DDT test is Fail ********************")
            self.driver.close()
            assert False
        self.logger.info("***************** End of Login DDT Test ********************")
        self.logger.info("***************** Completed test_Valid_Login_data_driven ********************")
'''
'''
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
'''