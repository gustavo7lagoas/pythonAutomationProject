# import all page oobjects
from loginpage import LoginPage
from homepage import HomePage
from profilepage import ProfilePage
from postpage import PostPage

class PageObjectFactory:
    page_map = {
        'login': LoginPage,
        'home': HomePage,
        'profile': ProfilePage,
        'post': PostPage
    }

    def create(self, page_key, driver):
        return self.page_map[page_key](driver)
