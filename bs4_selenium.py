import random
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from undetected_chromedriver import Chrome
from selenium.webdriver.firefox.options import Options

from logger import logger


class Browser:
    def __init__(self, ):
        self.driver = None

    def get_source(self, url):
        page_source = None
        logger.info(f"Sending request to ({url})")
        try:
            self.driver.get(url)
            time.sleep(random.randint(15, 35))
            page_source = self.driver.page_source
        except  Exception as e:
            logger.error(f"Request Failed ")
            page_source = None
        finally:
            return page_source

    def get_soup(self, url):
        response_text = self.get_source(url)
        if response_text is not None:
            soup = BeautifulSoup(response_text, "html.parser")
            return soup
        else:
            return None

    def close_driver(self):
        self.driver.close()


class ChromeBrowser(Browser):
    def __init__(self):
        super().__init__()
        self.driver = Chrome()


class FirefoxBrowser(Browser):
    profile_path = 'C:/Users/amirb/AppData/Roaming/Mozilla/Firefox/Profiles/28c7uhg3.default-release'  # Update with the actual path

    def __init__(self):
        super().__init__()
        self.firefox_options = Options()
        self.firefox_options.profile = webdriver.FirefoxProfile(FirefoxBrowser.profile_path)
        self.driver = webdriver.Firefox(options=self.firefox_options)
