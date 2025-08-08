from selenium import webdriver
from selenium.common.exceptions import (NoAlertPresentException,
                                        UnexpectedAlertPresentException)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service


class DriverManager:
    def __init__(self):
        service = Service(executable_path="/usr/local/bin/chromedriver")
        options = webdriver.ChromeOptions()
        options.binary_location = "/usr/bin/google-chrome"
        options.add_experimental_option("prefs", {"intl.accept_languages": "en_US"})
        options.add_argument("--no-sandbox")
        options.add_argument("--user-data-dir=chrome-profiles/mm-chrome-profile")
        options.add_argument("--load-extension=../../../dist/chrome")
        self.__driver = webdriver.Chrome(service=service, options=options)
    
    def get_driver(self):
        return self.__driver
    
    def quit(self):
        self.__driver.quit()
