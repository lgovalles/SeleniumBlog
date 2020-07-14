import unittest
import datetime
from pages.signup_page import SignupPage
from pages.message import Message
from selenium import webdriver

# TC N#: Sing up for blog
class SingUpTest(unittest.TestCase):
    
    timestamp = datetime.datetime.timestamp(datetime.datetime.now())

    def setUp(self):
        self.browser = webdriver.Firefox()
        # Go to signup form
        self.browser.get('https://selenium-blog.herokuapp.com/signup')
        # Define varibles 
        self.username = f'nameT{self.timestamp}'
        self.email = f'nameT{self.timestamp}@test.com'
        self.password = "Secret"

    def test_sing_up(self):
        # Assert
        assert_text = f'Welcome to the alpha blog nameT{self.timestamp}'
        # Fill out and submit form
        signup = SignupPage(self.browser)
        signup.enter_username(self.username)
        signup.enter_email(self.email)
        signup.enter_password(self.password )
        signup.submit_form()
        #Confirm user is signed up successfully
        banner = Message(self.browser)
        banner_text = banner.get_banner_text()
        self.assertEqual(banner_text, assert_text)

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()