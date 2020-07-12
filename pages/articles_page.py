from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ArticlePage():
    # Selectors 
    CSS_SELECTOR = By.XPATH
    TITLE_FIELD = "//*[@id='article_title']"
    DESCRIPTION_FIELD = "//*[@id='article_description']"
    SUBMIT_BUTTON = "/html/body/div[2]/div/div/form/div[3]/div/input"

    SUCCESS_BANNER = "//*[@id='flash_success']"

    # Methods 
    def __init__(self,browser):
        self.browser = browser
        # Define Explicit Waits for 5 sec
        self.wait = WebDriverWait(self.browser,5)

    def enter_title(self,title):
        email_field = self.browser.find_element(self.CSS_SELECTOR, self.TITLE_FIELD)
        email_field.send_keys(title)

    def enter_description(self,description):
        password_field = self.browser.find_element(self.CSS_SELECTOR, self.DESCRIPTION_FIELD)
        password_field.send_keys(description)

    def submit_form(self):
        submit_button = self.browser.find_element(self.CSS_SELECTOR,self.SUBMIT_BUTTON)
        submit_button.click()
<<<<<<< HEAD
    
    def delete_article(self):
        delete_buttons = self.wait.until(EC.element_to_be_clickable((self.CSS_SELECTOR,self.DELETE_BUTTON)))
        delete_buttons.click()
=======
>>>>>>> parent of 2cfa1f8... Testing Delete Article

    def get_banner_text(self):
        banner =  self.wait.until(EC.presence_of_element_located((self.CSS_SELECTOR,self.SUCCESS_BANNER)))
        return banner.text