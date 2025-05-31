import time

import pytest
import os


from utils.driver_factory import get_driver
from pages.careers_page import CareersPage
from pages.jop_search import JobSearch

@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_qa_jobs_flow(browser):
    driver = get_driver(browser)
    driver.maximize_window()
    try:
        careers = CareersPage(driver)
        job = JobSearch(driver)

        careers.go_to_qa_jobs_page()
        time.sleep(2)
        job.accept_cookies_if_visible()
        time.sleep(2)
        job.filter_jobs()
        time.sleep(2)
        job.validate_jobs()
        time.sleep(2)
        job.go_to_view_role()
        time.sleep(5)

        driver.switch_to.window(driver.window_handles[-1])
        assert "lever.co" in driver.current_url, "Yönlendirme Lever başvuru sayfasına olmadı"

    except Exception as e:
        os.makedirs("screenshots", exist_ok=True)
        screenshot_path = f"screenshots/failure_case2_{browser}.png"
        driver.save_screenshot(screenshot_path)
        print(f"📸 Screenshot saved: {screenshot_path}")
        raise e

    finally:
        driver.quit()
