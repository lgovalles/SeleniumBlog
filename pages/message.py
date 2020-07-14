from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Message():
    # Selectors 
    CSS_SELECTOR = By.CSS_SELECTOR
    #  CSS Assert
    SUCCESS_BANNER = "#flash_success"

    # Methods 
    def __init__(self,browser):
        self.browser = browser
        # Define Explicit Waits for 5 sec
        self.wait = WebDriverWait(self.browser,5)
        
    def get_banner_text(self):
        banner =  self.wait.until(EC.presence_of_element_located((self.CSS_SELECTOR,self.SUCCESS_BANNER)))
        return banner.text