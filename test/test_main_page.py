import pytest
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from constants import Urls
import allure


class TestMainPage:
    @allure.title("Открыть главную страницу")
    def test_open(self,driver):
        open_page = MainPage(driver,Urls.URL)
        open_page.open_to_site()


    @allure.title("Проверить 'Вопросы о главном'")
    @allure.description('Прокрутить страницу вниз > нажать на вопрос > проверить ответ на вопрос')
    @pytest.mark.parametrize("QUESTION,ANSWER,EXPECTED_TEXT",
                             [
                                 (MainPageLocators.QUESTION_0, MainPageLocators.ANSWER_0,'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
                                 (MainPageLocators.QUESTION_1, MainPageLocators.ANSWER_1,'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
                                 (MainPageLocators.QUESTION_2, MainPageLocators.ANSWER_2,'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
                                 (MainPageLocators.QUESTION_3, MainPageLocators.ANSWER_3,'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
                                 (MainPageLocators.QUESTION_4, MainPageLocators.ANSWER_4,'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
                                 (MainPageLocators.QUESTION_5, MainPageLocators.ANSWER_5,'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
                                 (MainPageLocators.QUESTION_6, MainPageLocators.ANSWER_6,'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
                                 (MainPageLocators.QUESTION_7, MainPageLocators.ANSWER_7,'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
                              ]
                             )
    def test_check_questions_about_important_and_answer_on_it(self, driver,QUESTION,ANSWER,EXPECTED_TEXT):
        questions_on_main = MainPage(driver,Urls.URL)
        questions_on_main.scroll_down()
        questions_on_main.questions_about_important_click(QUESTION)
        questions_on_main.check_answer_text(ANSWER,EXPECTED_TEXT)

    @allure.title("Проверить кнопку Заказать вверху страницы")
    @allure.description('Нажать на кнопку "Заказать"')
    def test_check_button_order_up(self, driver):
        button_order = MainPage(driver,Urls.URL)
        button_order.click_button_order_up()


    @allure.title("Проверить кнопку Заказать внизу страницы")
    @allure.description('Нажать на кнопку "Заказать"')
    def test_check_button_order_down(self, driver):
        button_order = MainPage(driver,Urls.URL)
        button_order.scroll_down()
        button_order.click_button_order_down()


    @allure.title("Проверить переход на новую страницу при нажатии на логотип Яндекс")
    @allure.description('Нажать на логотип "Яндекс" > переключить окно на новую вкладку > подтвердить переход на страницу Дзен')
    def test_check_logo_yandex(self,driver):
        logo_yandex = MainPage(driver,Urls.URL)
        logo_yandex.click_on_logo_yandex()
        logo_yandex.switch_to_window()
        logo_yandex.get_page_dzen()








