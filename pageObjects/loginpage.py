from base import BasePage
from base import InvalidPageException

class LoginPage(BasePage):

    # Locators
    _join_button_locator = 'joinEnvygramBtn'
    _login_link_locator = 'loginDialogButton'
    _user_id_locator = 'UserLogin_email'
    _user_passwd_locator = 'UserLogin_password'
    _sign_in_locator = 'signIn'

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    @property
    def _join_button(self):
        return self.driver.find_element_by_id(self._join_button_locator)

    @property
    def _login_link(self):
        return self.driver.find_element_by_id(self._login_link_locator)

    @property
    def _user_id(self):
        return self.driver.find_element_by_id(self._user_id_locator)

    @property
    def _user_passwd(self):
        return self.driver.find_element_by_id(self._user_passwd_locator)

    @property
    def _sign_in(self):
        return self.driver.find_element_by_id(self._sign_in_locator)

    def login(self, user_id, user_passwd):
        self._login_link.click()
        self._user_id.clear()
        self._user_id.send_keys(user_id)
        self._user_passwd.clear()
        self._user_passwd.send_keys(user_passwd)
        self._sign_in.click()

    def successful_login(self):
        self.login('gustavo7lagoas', 'testingUser')

    def _validate_page(self, driver):
        """ Checkes if page has been loaded """
        if not driver.title == 'Envygram':
            raise InvalidPageException('Not in login page')
