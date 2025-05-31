from selenium import webdriver

def get_driver(browser="chrome"):
    if browser == "firefox":
        return webdriver.Firefox()
    options = webdriver.ChromeOptions()
    return webdriver.Chrome(options=options)