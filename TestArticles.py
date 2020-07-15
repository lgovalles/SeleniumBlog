import unittest
import time
from selenium import webdriver
from pages.articles_page import ArticlePage
from pages.message import Message

class ArticlesTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        # Go to signup form
        self.browser.get('https://selenium-blog.herokuapp.com/articles')
        # Define varibles 
        self.title = "Test Article"
        self.description = "Rand Text"

    def test_article_delete(self):
        # Assert
        assert_text = "Article was successfully deleted"
        # Delete an Article
        article =  ArticlePage(self.browser)
        article.delete_article()
        alert = self.browser.switch_to_alert()
        alert.accept()
        # Confirm article is delete successfully
        time.sleep(5)
        banner = Message(self.browser)
        banner_text = banner.get_banner_success_text()
        self.assertEqual(banner_text, assert_text)

    def test_article_Edit(self):
        # Assert
        assert_text = "Edit article"
        # Edit an Article
        article =  ArticlePage(self.browser)
        article.edit_article()
        time.sleep(5)
        # Confirm Edit page is open 
        header_text = article.get_header()
        self.assertEqual(header_text, assert_text)

    def test_article_create(self):
        # Assert
        assert_text = "Create an article"
        # Edit an Article
        article =  ArticlePage(self.browser)
        article.create_article()
        # Confirm the create page is open
        time.sleep(5)
        header_text = article.get_header()
        self.assertEqual(header_text, assert_text)
    
    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()