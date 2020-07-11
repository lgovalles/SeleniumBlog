from selenium.webdriver.common.by import By


class LoginPage():
    # Selectors 
    CSS_SELECTOR = By.CSS_SELECTOR
    EMAIL_FIELD = "input[type='email']"
    PASSWORD_FIELD = "input[type='password']"
    SUBMIT_BUTTON = "input[type='submit']"

    # Methods 
    def __init__(self,browser):
        self.browser = browser
    
    def enter_email(self,email):
        email_field = self.browser.find_element(self.CSS_SELECTOR, self.EMAIL_FIELD)
        email_field.send_keys(email)

    def enter_password(self,password):
        password_field = self.browser.find_element(self.CSS_SELECTOR, self.PASSWORD_FIELD)
        password_field.send_keys(password)
    
    def submit_form(self):
        submit_button = self.browser.find_element(self.CSS_SELECTOR,self.SUBMIT_BUTTON)
        submit_button.click()