from base import BasePage
from base import InvalidPageException

class PostPage(BasePage):
    """
    Page object for View Post page
    It has some limitations because will be use only for validate
    a successful login.
    """

    _post_title_locator = '.icon-arrow'

    @property
    def _post_title(self):
       return self.driver.find_element_by_css_selector(self._post_title_locator)

    def __init__(self, driver):
        super(PostPage, self).__init__(driver)

    def get_post_title(self):
        return self._post_title.text

    def _validate_page(self, driver):
        # Checking the username will lock the threat until the login finishes
        try:
            driver.find_element_by_css_selector(self._post_title_locator)
        except:
            raise InvalidPageException('Error: It is not in the Post page')


