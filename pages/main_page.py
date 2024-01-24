from constants import Urls
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderFormPageLocators
import allure

class MainPage(BasePage):
    def __init__(self,driver,url):
        super().__init__(driver,url)

    @allure.step("Прокрутить страницу вниз до элемента 'Важные вопросы'")
    def scroll_down(self):
        self.scroll_down_page(MainPageLocators.IMPORTANT_QUESTIONS)
        assert self.find_element(MainPageLocators.IMPORTANT_QUESTIONS)

    @allure.step("Кликнуть на вопрос")
    def questions_about_important_click(self, QUESTION):
        self.click_on_element(QUESTION)
        assert self.find_element(QUESTION)

    @allure.step("Проверить доступность 'Ответов' на вопросы")
    def check_answer_text(self, ANSWER, EXPECTED_TEXT):
        self.wait_visibility_of_element_located(ANSWER)
        actually_text = self.get_actually_text(ANSWER)
        assert actually_text == EXPECTED_TEXT

    @allure.step("Клик на кнопку 'Заказать' вверху страницы - открылась форма заказа")
    def click_button_order_up(self):
        self.click_button_order_on_main(MainPageLocators.BUTTON_ORDER_UP)
        assert self.find_element(OrderFormPageLocators.ORDER_HEADER)

    @allure.step("Клик на кнопку 'Заказать' внизу страницы- открылась форма заказа")
    def click_button_order_down(self):
        self.click_button_order_on_main(MainPageLocators.BUTTON_ORDER_DOWN)
        assert self.find_element(OrderFormPageLocators.ORDER_HEADER)

    @allure.step("Проверить доступность формы заказа")
    def check_order_form_after_click_button_order(self):
        self.find_element(OrderFormPageLocators.ORDER_HEADER)
        expected_url = Urls.URL_ORDER_PAGE
        assert expected_url

    @allure.step("Клик на логотип Яндекса")
    def click_on_logo_yandex(self):
        self.click_on_element(MainPageLocators.LOGO_YANDEX)
        assert self.find_element(MainPageLocators.LOGO_YANDEX)

    @allure.step("Получение страницы Дзен")
    def get_page_dzen(self):
        self.get_current_url()
        expected_url = Urls.URL_DZEN
        assert expected_url







