from pages.rent_page import RentPage
from constants import Urls
import allure


class TestRentFormPage:
    @allure.title("Заполнить форму Аренда")
    @allure.description('Заполнить форму Сделать заказ > заполнить форму аренды > нажать "Да" в окне подтверждения > нажать кнопку Посмотреть статус')
    def test_check_rent_form(self,fill_order_form):
        rent_form = RentPage(fill_order_form,Urls.URL)
        rent_form.fill_rent_form()
        rent_form.click_yes_on_confirm_order()
        rent_form.click_button_order_confirmed()




