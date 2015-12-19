import unittest
from basetestcase import BaseTestCase
from pageObjects.pagefactory import PageObjectFactory

class ProfileTest(BaseTestCase):

    def setUp(self):
        super(ProfileTest, self).setUp()
        self.pageFactory = PageObjectFactory()
        self.loginPage = self.pageFactory.create('login', self.driver)
        self.loginPage.successful_login()
        self.homePage = self.pageFactory.create('home', self.driver)
        self.homePage.go_to_profile()
        self.profilePage = self.pageFactory.create('profile', self.driver)

    def testCreatePost(self):
        self.profilePage.create_post( \
            '1', \
            'Image From Internet', \
            'http://i.space.com/images/i/000/005/972/original/sun-photo-solar-filament-101118-02.jpg?1294094311', \
            'Default', \
            '4')
        detailsPage = self.pageFactory.create('post', self.driver)
        self.assertEqual(detailsPage.get_post_title(), '1')

if __name__ == '__main__':
    unittest.main()
