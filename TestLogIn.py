import unittest
import json
from pages.loging_page import LoginPage
from pages.message import Message
from selenium import webdriver

# TC N#: Login for blog
class LoginTest(unittest.TestCase):

    def setUp(self):
        # Read the data from the json file 
        with open('data/user.json') as filejson:
            userdata = json.load(filejson)
            
        self.browser = webdriver.Firefox()
        # Go to signup form
        self.browser.get('https://selenium-blog.herokuapp.com/login')
        # Define varibles 
        self.email = userdata['user']
        self.password = userdata['password']

    def test_login(self):
        # Assert 
        assert_text = "You have successfully logged in!"
        # Fill out and submit form
        login = LoginPage(self.browser)
        login.enter_email(self.email)
        login.enter_password(self.password)
        login.submit_form()
        # Confirm user is log in successfully
        banner = Message(self.browser)
        banner_text = banner.get_banner_success_text()
        self.assertEqual(banner_text, assert_text)

    def test_login_wrong(self):
        # Assert 
        assert_text = "There was a problem logging in"
        # Fill out and submit form
        login = LoginPage(self.browser)
        # login.enter_email(self.email)
        # login.enter_password(self.password)
        login.submit_form()
        # Confirm user is log in successfully
        banner = Message(self.browser)
        banner_text = banner.get_banner_danger_text()
        self.assertEqual(banner_text, assert_text)

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()
    