import unittest
import time
from selenium import webdriver
from pages.articles_page import ArticlePage
from pages.user_page import UsersPage

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
        #time.sleep(5)
        # Confirm article is delete successfully
        banner_text = article.get_banner_text()
        self.assertEqual(banner_text, assert_text)

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()