from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from constants import Urls
import pytest
from locators.order_page_locators import OrderFormPageLocators
from locators.main_page_locators import MainPageLocators
from constants import Constants



@pytest.fixture
def driver():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.get(Urls.URL)
    yield driver
    driver.quit()






