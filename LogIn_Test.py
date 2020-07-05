import unittest
from pages.loging_page import LoginPage
from pages.user_page import UsersPage
from selenium import webdriver

# TC N#: Login for blog
class LoginTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        # Go to signup form
        self.browser.get('https://selenium-blog.herokuapp.com/login')
        # Define varibles 
        self.email = "nameT1593915406.935035@test.com"
        self.password = "Secret"

    def test_login(self):
        # Assert 
        assert_text = "You have successfully logged in!"
        # Fill out and submit form
        login = LoginPage(self.browser)
        login.enter_email(self.email)
        login.enter_password(self.password)
        login.submit_form()
        # Confirm user is log in successfully
        users = UsersPage(self.browser)
        banner_text = users.get_banner_text()
        self.assertEqual(banner_text, assert_text)

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()