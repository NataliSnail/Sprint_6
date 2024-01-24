from selenium.webdriver import Keys
from constants import Urls
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderFormPageLocators
from locators.rent_page_locators import RentFormPageLocators
import allure


class RentPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver,url)


    @allure.step("Заполнить форму 'Аренда', подтвердить переход к форме 'подтверждения'")
    def fill_rent_form(self):
        self.find_element(RentFormPageLocators.DATA_FIELD).send_keys('02.02.2024')
        self.find_element(RentFormPageLocators.DATA_FIELD).send_keys(Keys.ENTER)
        self.click_on_element(RentFormPageLocators.RENTAL_PERIOD_FIELD)
        self.click_on_element(RentFormPageLocators.DROPDOWN_PLACEHOLDER_SUTKI)
        self.click_on_element(RentFormPageLocators.COLOR_FIELD_BLACK)
        self.find_element(RentFormPageLocators.COMMENT_FIELD).send_keys(
            'Доставка вечером')
        self.click_on_element(RentFormPageLocators.BUTTON_ORDER)
        assert self.find_element(RentFormPageLocators.CONFIRM_ORDER_BUTTON_YES)

    @allure.step("Клик 'Да' на форме 'Хотите оформить заказ?")
    def click_yes_on_confirm_order(self):
        self.find_element(RentFormPageLocators.CONFIRM_WINDOW)
        self.click_on_element(RentFormPageLocators.CONFIRM_ORDER_BUTTON_YES)
        assert self.find_element(RentFormPageLocators.ORDER_CONFIRMED)

    def click_button_order_confirmed(self):
        self.find_element(RentFormPageLocators.NUMBER_ORDER)
        self.click_on_element(RentFormPageLocators.BUTTON_CHECK_STATUS)
        assert self.find_element(RentFormPageLocators.TRACK_INFO)

