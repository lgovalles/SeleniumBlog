from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LayoutPage():
    # Selectors 
    CSS_SELECTOR = By.CSS_SELECTOR
    LOGIN_BUTTON = "a.btn.btn-lg.btn-primary"
    SIGNUP_BUTTON = "a.btn.btn-lg.btn-success"
    LOGIN_LINK = "a[href='/login']"
    SIGNPUP_LINK = "a[href='/signup']"

    # Methods 
    def __init__(self,browser):
        self.browser = browser
        # Define Explicit Waits for 5 sec
        self.wait = WebDriverWait(self.browser,5)

    def click_login_button(self):
        login_buttons = self.wait.until(EC.element_to_be_clickable((self.CSS_SELECTOR,self.LOGIN_BUTTON)))
        login_buttons.click()

    def click_signup_button(self):
        signup_buttons = self.wait.until(EC.element_to_be_clickable((self.CSS_SELECTOR,self.SIGNUP_BUTTON)))
        signup_buttons.click()

    def click_login_link(self):
        signup_buttons = self.wait.until(EC.element_to_be_clickable((self.CSS_SELECTOR,self.LOGIN_BUTTON)))
        signup_buttons.click()
    
    def click_sigup_link(self):
        signup_buttons = self.wait.until(EC.element_to_be_clickable((self.CSS_SELECTOR,self.SIGNUP_BUTTON)))
        signup_buttons.click()