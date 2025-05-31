from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self.driver.get("https://useinsider.com/")

    def is_loaded(self):
        return "Insider" in self.driver.title
