from selenium.webdriver.common.by import By

class SignupPage():
    # selectors 
    CSS_SELECTOR = By.CSS_SELECTOR
    USERNAME_FIELD = "#user_username"
    EMAIL_FIELD = "#user_email"
    PASSWORD_FIELD = "#user_password"
    SUBMIT_BUTTON = "#submit"

    # Methods 
    def __init__(self,browser):
        self.browser = browser

    def enter_username(self,username):
        username_field = self.browser.find_element(self.CSS_SELECTOR, self.USERNAME_FIELD)
        username_field.send_keys(username)
    
    def enter_email(self,email):
        email_field = self.browser.find_element(self.CSS_SELECTOR, self.EMAIL_FIELD)
        email_field.send_keys(email)

    def enter_password(self,password):
        password_field = self.browser.find_element(self.CSS_SELECTOR, self.PASSWORD_FIELD)
        password_field.send_keys(password)

    def submit_form(self):
        submit_button = self.browser.find_element(self.CSS_SELECTOR,self.SUBMIT_BUTTON)
        submit_button.click()
        