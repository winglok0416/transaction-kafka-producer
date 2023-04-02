from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from exception import StreamingDataNotAvailableException


class ScrappingDriver:
    def __init__(self):
        self.url = "http://www.nasdaq.com/market-activity/stocks/aapl/latest-real-time-trades"
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.url)
        self.first_visit = True

    def scrap_data(self):
        try:
            if self.first_visit is False:
                self.driver.refresh()
            else:
                self.first_visit = False

            table_body = self.driver.find_element(By.CLASS_NAME, "latest-real-time-trades__table-body")

            return table_body.find_elements(By.CLASS_NAME, "latest-real-time-trades__row")

        except NoSuchElementException:
            raise StreamingDataNotAvailableException

    def close(self):
        self.driver.close()
