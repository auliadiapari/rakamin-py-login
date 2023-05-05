import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLoginInvalidUser:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        method = vars()

    def test_login_invalid_user_go_homepage(self, driver):
        self.driver.maximize_window()
        self.driver.get('https://jubelio.com')

