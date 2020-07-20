import unittest
import time
from selenium import webdriver
from pages.articles_page import ArticlePage
from pages.message import Message

class NewArticlesTest(unittest.TestCase):
    
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
        banner_text = banner.get_banner_success_text()
        self.assertEqual(banner_text, assert_text)

    def test_article_cancel_request(self):
        # Assert
        assert_text = "Listing all articles"
        # Fill out and submit form
        article =  ArticlePage(self.browser)
        article.click_cancel()
        # Confirm user is log in successfully
        time.sleep(5)
        header_text = article.get_header()
        self.assertEqual(header_text, assert_text)

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()