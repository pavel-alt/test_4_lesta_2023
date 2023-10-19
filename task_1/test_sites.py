from typing import List

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from task_1.parser_sites import ParserSites, Site

URL_PAGE = 'https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites'
XPATH_TO_TABLE = '//table[descendant::caption[contains(text(), "Programming languages")]]'


@pytest.fixture(scope='session')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.accept_insecure_certs = True

    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def sites(driver: WebDriver) -> List[Site]:
    wait = WebDriverWait(driver, 10)

    driver.get(URL_PAGE)
    wait.until(EC.visibility_of_element_located((By.XPATH, XPATH_TO_TABLE)))

    parser_sites = ParserSites(driver, XPATH_TO_TABLE)
    return parser_sites.get_sites()


def __digit_popularity(value: str) -> int:
    int_value = int(''.join([i for i in value if i.isdigit()]))
    return int_value


@pytest.mark.parametrize("expected_value", ([10 ** 7, 1.5 * 10 ** 7, 5 * 10 ** 7, 10 ** 8, 5 * 10 ** 8, 10 ^ 9, 1.5 * 10 ** 9]))
def test_sites(sites, expected_value):
    errors = []
    for site in sites:
        if __digit_popularity(site.popularity) < expected_value:
            errors.append(site)
    assert not errors, \
        ';\n'.join([f'{site.website}(Frontend:{site.frontend_lang})/Backend{site.backend_lang}) has {site.popularity} '
                    f'unique visitors per month. (Expected more than {expected_value})' for site in sites])
