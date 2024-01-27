
from pages.rent_page import RentPage
from constants import Urls
import allure


class TestRentFormPage:
    @allure.title("Заполнить форму Аренда")
    @allure.description('Клик на кнопку "Заказать" > Заполнить форму Сделать заказ > заполнить форму аренды ')
     def test_check_rent_form(self,driver):
        rent_form = RentPage(driver,Urls.URL)
        rent_form.click_button_order_up()
        rent_form.fill_order_form()
        rent_form.fill_rent_form()

    @allure.title("Подтверждение на форме 'Хотите оформить заказ?'")
    @allure.description(
            'Клик на кнопку "Заказать" > Заполнить форму Сделать заказ > заполнить форму аренды > нажать "Да" в окне подтверждения')
    def test_confirm_order_yes_button(self, driver):
        confirm = RentPage(driver,Urls.URL)
        confirm.click_button_order_up()
        confirm.fill_order_form()
        confirm.fill_rent_form()
        confirm.click_yes_on_confirm_order()


    @allure.title("Клик на кнопку 'Посмотреть статус' заказа")
    @allure.description(
        'Клик на кнопку "Заказать" > Заполнить форму Сделать заказ > заполнить форму аренды > нажать "Да" в окне подтверждения > нажать кнопку Посмотреть статус')
    def test_check_info_about_order_confirmed(self, driver):
        info_confirmed = RentPage(driver,Urls.URL)
        info_confirmed.click_button_order_up()
        info_confirmed.fill_order_form()
        info_confirmed.fill_rent_form()
        info_confirmed.click_yes_on_confirm_order()
        info_confirmed.click_button_order_confirmed()






