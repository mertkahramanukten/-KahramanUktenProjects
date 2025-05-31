import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CareersPage(BasePage):
    COMPANY_MENU = (By.XPATH, "/html/body/nav/div[2]/div/ul[1]/li[6]/a")
    CAREERS_LINK = (By.XPATH, "//*[@id='navbarNavDropdown']/ul[1]/li[6]/div/div[2]/a[2]")

    LOCATIONS_SECTION = (By.XPATH, "//h3[contains(text(),'Our Locations')]")
    TEAMS_SECTION = (By.XPATH, "//h3[contains(text(),'Find your calling')]")
    LIFE_SECTION = (By.XPATH, "//h3[contains(text(),'Life at Insider')]")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_careers(self):
        company_menu = self.get_element(self.COMPANY_MENU)
        careers_link = self.get_element(self.CAREERS_LINK)

        ActionChains(self.driver) \
            .move_to_element(company_menu) \
            .move_to_element(careers_link) \
            .click() \
            .perform()

    def is_sections_loaded(self):
        try:
            location_xpath = "//section[@id='career-our-location']/div[@class='container']/div[@class='row']/div[@class='col-12 d-flex flex-wrap']"
            find_calling_xpath = "//section[@id='career-find-our-calling']/div[@class='container']/div[@class='row']/a[@class='btn btn-outline-secondary rounded text-medium mt-5 mx-auto py-3 loadmore']"
            life_at_xpath = "//section[contains(@class, 'elementor-section') and contains(., 'Life at Insider')]"

            # Her bir elementi al ve görünmeden önce scroll et
            for xpath in [location_xpath, find_calling_xpath, life_at_xpath]:
                el = self.get_element((By.XPATH, xpath))
                self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", el)
                time.sleep(1)  # scroll sonrası yüklenme için minik bekleme

            return all([
                self.is_visible((By.XPATH, location_xpath)),
                self.is_visible((By.XPATH, find_calling_xpath)),
                self.is_visible((By.XPATH, life_at_xpath)),
            ])
        except Exception as e:
            print(f"🚫 Bölümler yüklenemedi: {e}")
            return False


    def go_to_qa_jobs_page(self):
        self.driver.get("https://useinsider.com/careers/quality-assurance/")
        self.click((By.XPATH, "//section[@id='page-head']/div[@class='container']/div[@class='row']/div[@class='col-12 col-lg-7 order-2 order-lg-1']/div[@class='d-flex flex-column justify-content-center text-center text-lg-left h-100']/div[@class='button-group d-flex flex-row']/a[@class='btn btn-outline-secondary rounded text-medium mt-2 py-3 px-lg-5 w-100 w-md-50']"))

        # Sayfadaki belirli başlıkların görünür olup olmadığını kontrol eder
    def verify_sections(self):
        self.is_visible(self.LOCATIONS_SECTION)
        self.is_visible(self.TEAMS_SECTION)
        self.is_visible(self.LIFE_SECTION)