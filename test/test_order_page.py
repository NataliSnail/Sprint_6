import pytest
from pages.order_page import OrderPage
from locators.order_page_locators import OrderFormPageLocators
from constants import Urls
import allure


class TestOrderPage:
    @allure.title("Заполнение форма 'сделать заказ'")
    @pytest.mark.parametrize("name,last_name,address, metro_station,tel_number",
                             [
                                ('Иван', 'Иванов', 'Москва, ул. Филевская, д1, кв.1', OrderFormPageLocators.METRO_STATION_SOKOLNIKI, '49512365478'),
                                ('Марфа', 'Петрова', 'Москва, ул. Тестовская,д15, кв.123', OrderFormPageLocators.METRO_STATION_CHERKOZOVSKAYA, '49518523695')
                             ]
                             )
    def test_check_order_form(self,driver,name,last_name,address, metro_station,tel_number):
        order_form = OrderPage(driver,Urls.URL)
        order_form.click_button_order_up()
        order_form.fill_order_form(name,last_name,address, metro_station,tel_number)
        order_form.get_rent_form()

    @allure.title("Проверить переход по логотипу 'Самокат' со страницы 'Оформления заказа'")
    def test_click_logo_samokat(self,driver):
        logo_samokat = OrderPage(driver,Urls.URL)
        logo_samokat.click_button_order_up()
        logo_samokat.click_logo_samokat()
        logo_samokat.get_main_pade()







