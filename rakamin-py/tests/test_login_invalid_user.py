from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()


class TestLoginInvalidUser:
    def test_login_invalid_user_go_homepage(self):
        driver.get("https://jubelio.com")
        driver.find_elements(By.XPATH, '/html/body/div[1]/section[1]/div/div[3]/div/div[2]/div/div/a/span/span').click()

    # try:
    #     title = driver.title
    #     assert "Jubelio - Solusi Omnichannel Untuk Pebisnis Online & Offline" in title
    #     print("Assertion is Passed")
    # except Exception as e:
    #     print("Assertion is failed", format(e))

    driver.quit()
