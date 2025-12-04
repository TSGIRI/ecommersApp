from selenium.webdriver.common.by import By

class Login_Page:

    # Locators
    link_MyAccount_xpath = "//span[text()='My Account']"
    link_login_xpath = "//a[text()='Login']"
    textbox_EMailAddress_id = "input-email"
    textbox_password_id = "input-password"
    button_login_xpath = "//input[@value='Login']"
    link_logout_xpath = "//a[@class='list-group-item'][normalize-space()='Logout']"

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Click My Account
    def clickMyAccountLink(self):
        self.driver.find_element(By.XPATH, self.link_MyAccount_xpath).click()

    # Click Login link
    def clickLoginLink(self):
        self.driver.find_element(By.XPATH, self.link_login_xpath).click()   # FIXED (added parentheses)

    # Enter Email
    def setEmail(self, email):
        email_box = self.driver.find_element(By.ID, self.textbox_EMailAddress_id)
        email_box.clear()
        email_box.send_keys(email)    # FIXED (send_keys not send_key)

    # Enter Password
    def setPassword(self, password):
        password_box = self.driver.find_element(By.ID, self.textbox_password_id)
        password_box.clear()
        password_box.send_keys(password)

    # Click Login button
    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    # Click Logout
    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()


