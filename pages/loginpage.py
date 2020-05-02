class loginpage():
    def __init__(self,driver):
        self.driver=driver
        self.advance_id ="details-button"
        self.link_id="proceed-link"
        self.email_textbox_id="Email"
        self.password_textbox_id="Password"
        self.login_button_xpath="//*[@id='loginForm']/div/form[1]/button"

    def advance(self):
        self.driver.find_element_by_id(self.advance_id).click()

    def link(self):
        self.driver.find_element_by_id(self.link_id).click()

    def email(self,email):
        self.driver.find_element_by_id(self.email_textbox_id).send_keys(email)

    def password(self,pwd):
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(pwd)

    def login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()