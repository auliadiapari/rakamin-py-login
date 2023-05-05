from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginLocators():

    email_field = (By.NAME, 'email')
    password_field = (By.NAME, 'password')
    login_button = (By.XPATH, '//*[@id="shell"]/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div['
                              '2]/form/div[4]/button')
