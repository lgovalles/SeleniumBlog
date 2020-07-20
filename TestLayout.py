import unittest
import time
from pages.layout_page import LayoutPage
from pages.loging_page import LoginPage
from pages.signup_page import SignupPage
from selenium import webdriver

# TC N#: Login for blog
class LayoutTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        # Go to signup form
        self.browser.get('https://selenium-blog.herokuapp.com/')

    def test_open_login_page(self):
        # Assert 
        assert_text = "Log in"
        # Find and click on 
        layout = LayoutPage(self.browser)
        layout.click_login_button()
        # Confirm the login page is loading
        time.sleep(5)
        header = LoginPage(self.browser)
        header_text = header.get_header()
        self.assertEqual(header_text, assert_text)

    def test_openlink_login_page(self):
        # Assert 
        assert_text = "Log in"
        # Find and click on 
        layout = LayoutPage(self.browser)
        layout.click_login_link()
        # Confirm the login page is loading
        time.sleep(5)
        header = LoginPage(self.browser)
        header_text = header.get_header()
        self.assertEqual(header_text, assert_text)

    def test_open_signup_page(self):
        # Assert 
        assert_text = "Signup for Alpha Blog"
        # Find and click on 
        layout = LayoutPage(self.browser)
        layout.click_signup_button()
        # Confirm the signup page is loading
        time.sleep(5)
        header = SignupPage(self.browser)
        header_text = header.get_header()
        self.assertEqual(header_text, assert_text)

    def test_openlink_signup_page(self):
        # Assert 
        assert_text = "Signup for Alpha Blog"
        # Find and click on 
        layout = LayoutPage(self.browser)
        layout.click_sigup_link()
        # Confirm the signup page is loading
        time.sleep(5)
        header = SignupPage(self.browser)
        header_text = header.get_header()
        self.assertEqual(header_text, assert_text)

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()
    