from dataclasses import dataclass
from typing import List

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


@dataclass
class Site:
    website: str = ''
    popularity: str = ''
    frontend_lang: str = ''
    backend_lang: str = ''
    database: str = ''
    notes: str = ''


class ParserSites:
    """
    Class for parsing websites from table.
    """

    def __init__(self, driver: WebDriver, xpath_to_table: str):
        self.driver = driver
        self.xpath_to_table = xpath_to_table

    @property
    def rows(self) -> List[WebElement]:
        """
        Get rows webelement.
        """
        return self.driver.find_elements(by=By.XPATH, value=f'{self.xpath_to_table}/tbody/tr')

    @staticmethod
    def get_value(row: WebElement, xpath: str) -> str:
        """
        Get text from row's cells.
        """
        return row.find_element(by=By.XPATH, value=xpath).text

    def builder(self, row: WebElement) -> Site:
        """
        Create dataclasses instance
        """
        list_params = [arg for arg in Site.__dict__.keys() if not arg.startswith('_')]
        values_list = [self.get_value(row, f'td[{i + 1}]') for i in range(len(list_params))]
        return Site(*values_list)

    def get_sites(self) -> List[Site]:
        """
         Return Sites list source rows
        """
        sites = []
        for row in self.rows:
            sites.append(self.builder(row))
        return sites
