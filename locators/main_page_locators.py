from selenium.webdriver.common.by import By

class MainPageLocators:
    ACCEPT_COOKIES = (By.ID, 'rcc-confirm-button')                                             # кнопка подтвердить куки
    IMPORTANT_QUESTIONS = (By.CLASS_NAME, "Home_FourPart__1uthg")                               #элемент "Важные вопросы"
    BUTTON_ORDER_UP = (By.CSS_SELECTOR, '[class*="Header_Nav"] [class="Button_Button__ra12g"]') #кнопка Заказать вверху страницы
    BUTTON_ORDER_DOWN = (By.CLASS_NAME, 'Button_Button__ra12g.Button_Middle__1CSJM')           #кнопка Заказать внизу страницы
    LOGO_YANDEX = (By.XPATH, '//a[contains(@href, "//yandex.ru")]')                             #логотип яндекса
    DZEN_MENU_ELEMENTS = (By.XPATH, '//a[@class="tabs-menu__link-2b"]')                         #таб меню на странице Дзен Новости разделов
    MODEL_TOXIC_PRO = (By.XPATH, '//div[@class ="Home_Row__jdQW2"]')                           # элемент "Модель Toxic PRO" на главной странице

    QUESTION_0 = (By.XPATH, '//div[@id= "accordion__heading-0"]')  # элемент вопрос  №1
    QUESTION_1 = (By.XPATH, '//div[@id= "accordion__heading-1"]')  # элемент вопрос  №2
    QUESTION_2 = (By.XPATH, '//div[@id= "accordion__heading-2"]')  # элемент вопрос  №3
    QUESTION_3 = (By.XPATH, '//div[@id= "accordion__heading-3"]')  # элемент вопрос  №4
    QUESTION_4 = (By.XPATH, '//div[@id= "accordion__heading-4"]')  # элемент вопрос  №5
    QUESTION_5 = (By.XPATH, '//div[@id= "accordion__heading-5"]')  # элемент вопрос  №6
    QUESTION_6 = (By.XPATH, '//div[@id= "accordion__heading-6"]')  # элемент вопрос  №7
    QUESTION_7 = (By.XPATH, '//div[@id= "accordion__heading-7"]')  # элемент вопрос  №8

    ANSWER_0 = (By.XPATH, '//div[@id= "accordion__panel-0"]')  # элемент ответ  №1
    ANSWER_1 = (By.XPATH, '//div[@id= "accordion__panel-1"]')  # элемент ответ  №2
    ANSWER_2 = (By.XPATH, '//div[@id= "accordion__panel-2"]')  # элемент ответ  №3
    ANSWER_3 = (By.XPATH, '//div[@id= "accordion__panel-3"]')  # элемент ответ  №4
    ANSWER_4 = (By.XPATH, '//div[@id= "accordion__panel-4"]')  # элемент ответ  №5
    ANSWER_5 = (By.XPATH, '//div[@id= "accordion__panel-5"]')  # элемент ответ  №6
    ANSWER_6 = (By.XPATH, '//div[@id= "accordion__panel-6"]')  # элемент ответ  №7
    ANSWER_7 = (By.XPATH, '//div[@id= "accordion__panel-7"]')  # элемент ответ  №8
