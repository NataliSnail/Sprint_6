from selenium.webdriver import Keys
from constants import Urls
from constants import Constants
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderFormPageLocators
from locators.rent_page_locators import RentFormPageLocators
import allure
import random


class RentPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver,url)

    @allure.step("Клик на кнопку 'Заказать', подтвердить открытие формы Заказа")
    def click_button_order_up(self):
        self.click_button_order_on_main(MainPageLocators.BUTTON_ORDER_UP)
        assert self.find_element(OrderFormPageLocators.ORDER_HEADER)

    @allure.step("Заполнить форму 'Заказ'")
    def fill_order_form(self):
        self.send_keys(OrderFormPageLocators.NAME_FIELD, random.choice(Constants.random_name))
        self.send_keys(OrderFormPageLocators.LAST_NAME_FIELD, random.choice(Constants.random_last_name))
        self.send_keys(OrderFormPageLocators.ADDRESS_FIELD, random.choice(Constants.random_address_field))
        self.click_on_element(OrderFormPageLocators.STATION_METRO_FIELD)
        self.click_on_element(OrderFormPageLocators.METRO_STATION_SOKOLNIKI)
        self.send_keys(OrderFormPageLocators.PHONE_NUMBER_FIELD, Constants.random_phone_number)
        self.click_on_element(OrderFormPageLocators.NEXT_BUTTON)
        assert self.find_element(OrderFormPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить форму 'Аренда', подтвердить переход к форме 'подтверждения'")
    def fill_rent_form(self):
        self.send_keys(RentFormPageLocators.DATA_FIELD,random.choice(Constants.random_some_date))
        self.send_keys(RentFormPageLocators.DATA_FIELD,Keys.ENTER)
        self.click_on_element(RentFormPageLocators.RENTAL_PERIOD_FIELD)
        self.click_on_element(RentFormPageLocators.DROPDOWN_PLACEHOLDER_SUTKI)
        self.click_on_element(RentFormPageLocators.COLOR_FIELD_BLACK)
        self.send_keys(RentFormPageLocators.COMMENT_FIELD, Constants.comment_info)
        self.click_on_element(RentFormPageLocators.BUTTON_ORDER)
        assert self.find_element(RentFormPageLocators.CONFIRM_ORDER_BUTTON_YES)

    @allure.step("Клик 'Да' на форме 'Хотите оформить заказ?")
    def click_yes_on_confirm_order(self):
        self.find_element(RentFormPageLocators.CONFIRM_WINDOW)
        self.click_on_element(RentFormPageLocators.CONFIRM_ORDER_BUTTON_YES)
        assert self.find_element(RentFormPageLocators.ORDER_CONFIRMED)

    @allure.step("Клик 'Посмотреть статус' о заказе")
    def click_button_order_confirmed(self):
        self.find_element(RentFormPageLocators.NUMBER_ORDER)
        self.click_on_element(RentFormPageLocators.BUTTON_CHECK_STATUS)
        assert self.find_element(RentFormPageLocators.TRACK_INFO)

