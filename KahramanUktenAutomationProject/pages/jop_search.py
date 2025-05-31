import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class JobSearch(BasePage):
    LOCATION_DROPDOWN = (By.XPATH, "/html/body/section[2]/div/div/div[2]/div/form/div[1]/span")
    ISTANBUL_OPTION = (By.XPATH, "//li[contains(@id, 'select2-filter-by-location-result') and contains(text(), 'Istanbul, Turkiye')]")

    DEPARTMENT_DROPDOWN = (By.XPATH, "/html/body/section[2]/div/div/div[2]/div/form/div[2]/span/span[1]/span/span[1]")
    QA_OPTION = (By.XPATH, "//li[contains(@id, 'select2-filter-by-department-result') and contains(text(), 'Quality Assurance')]")

    JOB_CARDS = (By.XPATH, "//div[@id='jobs-list']//div[contains(@class, 'position-list-item')]")
    VIEW_ROLE = (By.XPATH, "(//div[@id='jobs-list']//div[contains(@class, 'position-list-item')])[1]//a[contains(text(),'View Role')]")
    VIEW_BUTTON = (By.XPATH, "(//div[@id='jobs-list']//div[contains(@class, 'position-list-item')])[1]//a[contains(text(),'View Role')]")

    def filter_jobs(self):
        self.accept_cookies_if_visible()
        self.click(self.LOCATION_DROPDOWN)
        time.sleep(3)
        self.click(self.ISTANBUL_OPTION)
        print("✅ İstanbul seçildi")

        time.sleep(3)

        self.click(self.DEPARTMENT_DROPDOWN)
        time.sleep(3)
        qa_element = self.wait.until(EC.presence_of_element_located(self.QA_OPTION))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});", qa_element)
        qa_element.click()
        print("✅ QA seçildi")

    def validate_jobs(self):
        cards = self.get_elements(self.JOB_CARDS)
        for card in cards:
            assert "Quality Assurance" in card.text
            assert "Istanbul, Turkiye" in card.text

    def go_to_view_role(self):
        try:
            view = self.get_element(self.VIEW_ROLE)
            ActionChains(self.driver).move_to_element(view).perform()
            time.sleep(1)

            button = self.get_element(self.VIEW_BUTTON)
            button.click()
            print("✅ Hover sonrası View Role butonuna tıklandı")
        except Exception as e:
            print(f"🚫 Hover + click başarısız: {e}")
            raise e
