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


@pytest.fixture
def fill_order_form(driver):
    driver.find_element(*MainPageLocators.BUTTON_ORDER_UP).click()
    driver.find_element(*OrderFormPageLocators.NAME_FIELD).send_keys(Constants.name)
    driver.find_element(*OrderFormPageLocators.LAST_NAME_FIELD).send_keys(Constants.last_name)
    driver.find_element(*OrderFormPageLocators.ADDRESS_FIELD).send_keys(Constants.address_field)
    driver.find_element(*OrderFormPageLocators.STATION_METRO_FIELD).click()
    driver.find_element(*OrderFormPageLocators.METRO_STATION_SOKOLNIKI).click()
    driver.find_element(*OrderFormPageLocators.PHONE_NUMBER_FIELD).send_keys(Constants.phone_number)
    driver.find_element(*OrderFormPageLocators.NEXT_BUTTON).click()
    return driver



