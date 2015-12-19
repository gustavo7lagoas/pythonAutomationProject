from base import BasePage
from base import InvalidPageException

class HomePage(BasePage):
    """
    Page object for Home page
    It has some limitations because will be use only for validate
    a successful login.
    """

    _profile_locator = '.username.pull-left'

    @property
    def _profile(self):
        return self.driver.find_element_by_css_selector(self._profile_locator)

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def get_page_title(self):
        return self.driver.title

    def go_to_profile(self):
        self._profile.click()

    def _validate_page(self, driver):
        # Checking the username will lock the threat until the login finishes
        userid = driver.find_element_by_css_selector('.username.pull-left').text
        if not driver.title == 'Envygram - Home' \
        and userid == 'GUSTAVO7LAGOAS':
            raise InvalidPageException('Error: It is not in the home page')


