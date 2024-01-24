from constants import Urls
from pages.base_page import BasePage
from locators.order_page_locators import OrderFormPageLocators
from locators.rent_page_locators import RentFormPageLocators
from locators.main_page_locators import MainPageLocators
import allure



class OrderPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver,url)

    @allure.step("Клик на кнопку 'Заказать', подтвердить открытие формы Заказа")
    def click_button_order_up(self):
        self.click_button_order_on_main(MainPageLocators.BUTTON_ORDER_UP)
        assert self.find_element(OrderFormPageLocators.ORDER_HEADER)

    @allure.step("Заполнить форму 'Заказ'")
    def fill_order_form(self,name,last_name,address, metro_station,tel_number):
        self.find_element(OrderFormPageLocators.NAME_FIELD).send_keys(name)
        self.find_element(OrderFormPageLocators.LAST_NAME_FIELD).send_keys(last_name)
        self.find_element(OrderFormPageLocators.ADDRESS_FIELD).send_keys(address)
        self.click_on_element(OrderFormPageLocators.STATION_METRO_FIELD)
        self.click_on_element(metro_station)
        self.find_element(OrderFormPageLocators.PHONE_NUMBER_FIELD).send_keys(tel_number)
        self.click_on_element(OrderFormPageLocators.NEXT_BUTTON)
        assert self.find_element(RentFormPageLocators.RENT_HEADER)

    @allure.step("Проверка доступности формы 'Аренда'")
    def get_rent_form(self):
        self.find_element(RentFormPageLocators.RENT_HEADER)
        expected_url = Urls.URL_RENT_PAGE
        assert expected_url

    @allure.step("Клик на логотип 'Самокат'")
    def click_logo_samokat(self):
        """проверить переход по логотипу самоката"""
        self.click_on_element(OrderFormPageLocators.LOGO_SAMOKAT)
        assert self.find_element(OrderFormPageLocators.LOGO_SAMOKAT)


    @allure.step("Получение главной страницы сайта")
    def get_main_pade(self):
        self.get_current_url()
        expected_url = Urls.URL
        assert expected_url





