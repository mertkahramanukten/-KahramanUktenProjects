import pytest
import os
from utils.driver_factory import get_driver
from pages.home_page import HomePage
from pages.careers_page import CareersPage

@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_insider_job_flow(browser):
    driver = get_driver(browser)
    driver.maximize_window()

    try:
        home = HomePage(driver)
        home.load()
        home.accept_cookies_if_visible()
        assert home.is_loaded(), "Home page did not load properly."

        careers = CareersPage(driver)
        careers.navigate_to_careers()
        careers.accept_cookies_if_visible()
        assert careers.is_sections_loaded(), "One or more career sections not found."
    except Exception as e:
        os.makedirs("screenshots", exist_ok=True)
        driver.save_screenshot(f"screenshots/failure_{browser}.png")
        raise e
    finally:
        driver.quit()