import unittest
from basetestcase import BaseTestCase
from pageObjects.pagefactory import PageObjectFactory

class LoginTest(BaseTestCase):

    def setUp(self):
        super(LoginTest, self).setUp()
        self.pageFactory = PageObjectFactory()
        self.loginPage = self.pageFactory.create('login', self.driver)

    def testSuccessfulLogin(self):
        self.loginPage.login('gustavo7lagoas', 'testingUser')
        homepage = self.pageFactory.create('home', self.driver)
        self.assertEqual('Envygram - Home',
                        homepage.get_page_title(), 'Login is not successful');

if __name__ == '__main__':
    unittest.main()

