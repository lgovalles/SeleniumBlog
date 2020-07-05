from selenium.webdriver.common.by import By


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

    def enter_title(self,title):
        email_field = self.browser.find_element(self.CSS_SELECTOR, self.TITLE_FIELD)
        email_field.send_keys(title)

    def enter_description(self,description):
        password_field = self.browser.find_element(self.CSS_SELECTOR, self.DESCRIPTION_FIELD)
        password_field.send_keys(description)

    def submit_form(self):
        submit_button = self.browser.find_element(self.CSS_SELECTOR,self.SUBMIT_BUTTON)
        submit_button.click()

    def get_banner_text(self):
        banner = self.browser.find_element(self.CSS_SELECTOR,self.SUCCESS_BANNER)
        return banner.text