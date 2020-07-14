import unittest
from selenium import webdriver
from pages.articles_page import ArticlePage
from pages.message import Message

class ArticlesTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        # Go to signup form
        self.browser.get('https://selenium-blog.herokuapp.com/articles/new')
        # Define varibles 
        self.title = "Test Article"
        self.description = "Rand Text"

    def test_article_new(self):
        # Assert
        assert_text = "Article was successfully created"
        # Fill out and submit form
        form =  ArticlePage(self.browser)
        form.enter_title(self.title)
        form.enter_description(self.description)
        form.submit_form()
        # Confirm user is log in successfully
        banner = Message(self.browser)
        banner_text = banner.get_banner_text()
        self.assertEqual(banner_text, assert_text)

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()