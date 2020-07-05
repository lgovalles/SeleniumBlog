from selenium.webdriver.common.by import By

class UsersPage():
    # Selectors
    CSS_SELECTOR = By.ID
    SUCCESS_BANNER = "flash_success"


    # Methods
    def __init__(self,browser):
        self.browser = browser

    def get_banner_text(self):
        banner = self.browser.find_element(self.CSS_SELECTOR,self.SUCCESS_BANNER)
        return banner.text