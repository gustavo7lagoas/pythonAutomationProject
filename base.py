from abc  import abstractmethod

class BasePage(object):
    """ All page objects inherit from this """

    def __init__(self, driver):
        self._validate_page(driver)
        self.driver = driver
        self.By = driver.By
        self.WebDriverWait = driver.WebDriverWait
        self.expected_conditions = driver.expected_conditions
        self.Select = driver.Select

    @abstractmethod
    def _validate_page(self, driver):
        return

class InvalidPageException(Exception):
    """ Throw this exception when you do not find the correct page """
    pass
