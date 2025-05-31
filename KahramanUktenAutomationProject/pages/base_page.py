import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, by_locator):
        self.wait.until(EC.element_to_be_clickable(by_locator)).click()

    def get_element(self, by_locator):
        return self.wait.until(EC.presence_of_element_located(by_locator))

    def get_elements(self, by_locator):
        return self.wait.until(EC.presence_of_all_elements_located(by_locator))

    def get_text(self, by_locator):
        return self.get_element(by_locator).text

    def is_visible(self, by_locator):
        try:
            return self.get_element(by_locator).is_displayed()
        except:
            return False

    def accept_cookies_if_visible(self):
        try:
            cookie_btn = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Accept All')]")
            cookie_btn.click()
            print("✅ Çerez banner'ı kapatıldı")
            time.sleep(1)
        except:
            pass