import unittest
import time
from pages.articles_page import ArticlePage
from pages.user_page import UsersPage
from selenium import webdriver

class ArticlesTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        # Go to signup form
        # self.browser.get('https://selenium-blog.herokuapp.com/articles')
        # Define varibles 
        self.title = "Test Article"
        self.description = "Rand Text"

    def test_article_new(self):
        self.browser.get('https://selenium-blog.herokuapp.com/articles/new')
        # Assert
        assert_text = "Article was successfully created"
        # Fill out and submit form
        form =  ArticlePage(self.browser)
        form.enter_title(self.title)
        form.enter_description(self.description)
        form.submit_form()
        # Confirm user is log in successfully
        banner_text = form.get_banner_text()
        self.assertEqual(banner_text, assert_text)

    def test_article_delete(self):
        self.browser.get('https://selenium-blog.herokuapp.com/articles')
        # Assert
        assert_text = "Article was successfully deleted"
        # Delete an Article
        time.sleep(5)
        article =  ArticlePage(self.browser)
        article.delete_article()
        alert = self.browser.switch_to_alert()
        alert.accept()
        # Confirm article is delete successfully
        banner_text = article.get_banner_text()
        self.assertEqual(banner_text, assert_text)

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()