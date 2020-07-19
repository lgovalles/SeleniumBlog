from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ArticlePage():
    # Selectors 
    CSS_SELECTOR = By.CSS_SELECTOR
    # Css selector Article page 
    DELETE_BUTTON = "a[data-method='delete']"
    EDIT_BUTTON = "a.btn.btn-xs.btn-primary"
    CREATE_LINK = "a[href='/articles/new']"
    HEADER_LABEL = "h1[align='center']"
    # CSS selector new article page
    TITLE_FIELD = "#article_title"
    DESCRIPTION_FIELD = "#article_description"
    SUBMIT_BUTTON = "input[type='submit']"
    CANCEL_LINK = "a[href='/articles']"

    # Methods 
    def __init__(self,browser):
        self.browser = browser
        # Define Explicit Waits for 5 sec
        self.wait = WebDriverWait(self.browser,5)

    def get_header(self):
        header = self.browser.find_element(self.CSS_SELECTOR,self.HEADER_LABEL)
        return header.text

    def enter_title(self,title):
        email_field = self.browser.find_element(self.CSS_SELECTOR, self.TITLE_FIELD)
        email_field.send_keys(title)

    def enter_description(self,description):
        password_field = self.browser.find_element(self.CSS_SELECTOR, self.DESCRIPTION_FIELD)
        password_field.send_keys(description)

    def submit_form(self):
        delete_buttons = self.wait.until(EC.element_to_be_clickable((self.CSS_SELECTOR,self.SUBMIT_BUTTON)))
        delete_buttons.click()
    
    def edit_article(self):
        edit_button = self.wait.until(EC.element_to_be_clickable((self.CSS_SELECTOR,self.EDIT_BUTTON)))
        edit_button.click()
    
    def create_article(self):
        create_button = self.browser.find_element(self.CSS_SELECTOR,self.CREATE_LINK)
        create_button.click()
    
    def delete_article(self):
        delete_button = self.wait.until(EC.element_to_be_clickable((self.CSS_SELECTOR,self.DELETE_BUTTON)))
        delete_button.click()

    def click_cancel(self):
        cancel_link = self.wait.until(EC.element_to_be_clickable((self.CSS_SELECTOR,self.CANCEL_LINK)))
        cancel_link.click()
    
    