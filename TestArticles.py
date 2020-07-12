import unittest
<<<<<<< HEAD
from selenium import webdriver
=======
>>>>>>> parent of 2cfa1f8... Testing Delete Article
from pages.articles_page import ArticlePage
from pages.user_page import UsersPage

class ArticlesTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        # Go to signup form
<<<<<<< HEAD
        self.browser.get('https://selenium-blog.herokuapp.com/articles')
=======
        self.browser.get('https://selenium-blog.herokuapp.com/articles/new')
>>>>>>> parent of 2cfa1f8... Testing Delete Article
        # Define varibles 
        self.title = "Test Article"
        self.description = "Rand Text"

<<<<<<< HEAD
    def test_article_delete(self):
        # Assert
        assert_text = "Article was successfully deleted"
        # Delete an Article
        article =  ArticlePage(self.browser)
        article.delete_article()
        #self.browser.implicitly_wait(10) # seconds
        alert = self.browser.switch_to_alert()
        alert.accept()
        # Confirm article is delete successfully
        banner_text = article.get_banner_text()
        self.assertEqual(banner_text, assert_text)

=======
    def test_article_new(self):
        # Assert
        assert_text = "Article was successfully created"
        # Fill out and submit form
        form =  ArticlePage(self.browser)
        form.enter_title(self.title)
        form.enter_description(self.description)
        form.submit_form()
        # Confirm user is log in successfully
        users = UsersPage(self.browser)
        banner_text = users.get_banner_text()
        self.assertEqual(banner_text, assert_text)
    
>>>>>>> parent of 2cfa1f8... Testing Delete Article
    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()