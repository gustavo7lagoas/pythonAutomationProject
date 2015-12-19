import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(60)
        self.driver.By = By
        self.driver.WebDriverWait = WebDriverWait
        self.driver.expected_conditions = expected_conditions
        self.driver.maximize_window()
        self.driver.Select = Select

        # Get the application Home page
        self.driver.get('http://68.169.52.12/EnvyGram/html/site/index')

    def tearDown(self):
        # Closes the Browser Window
        self.driver.quit()
