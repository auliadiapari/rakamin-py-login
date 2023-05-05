import pdb

import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLoginInvalidUser:
    def setup_method(self, method):
        self.driver = webdriver.Edge()

    def test_login_invalid_user_go_homepage(self):
        self.driver.get('https://jubelio.com')
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[1]/section[1]/div/div[3]/div/div[2]/div/div/a/span/span').click()
        print(self.driver.current_window_handle.title())
        all_window_handles = self.driver.window_handles
        default_window = all_window_handles[0]
        new_window = all_window_handles[1]
        self.driver.switch_to.window(new_window)
        print(new_window.title())
        self.driver.find_element(By.NAME, 'email').send_keys('dummymail@gmail.com')
        self.driver.find_element(By.NAME, 'password').send_keys('dummypass')
        self.driver.find_element(By.XPATH, '//*[@id="shell"]/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div['
                                           '2]/form/div[4]/button').click()

        pdb.set_trace()
