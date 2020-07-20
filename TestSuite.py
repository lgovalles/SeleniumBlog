import unittest
from TestArticles import ArticlesTest
from TestLogIn import LoginTest
from TestLayout import LayoutTest
from TestNewArticles import NewArticlesTest
from TestSingUp import SingUpTest

tc1 = unittest.TestLoader().loadTestsFromTestCase(ArticlesTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(LayoutTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(NewArticlesTest)
tc5 = unittest.TestLoader().loadTestsFromTestCase(SingUpTest)

# Create 
sanityTestSuiste = unittest.TestSuite([tc2,tc5])

unittest.TextTestRunner().run(sanityTestSuiste)