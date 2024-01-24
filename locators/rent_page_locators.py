from selenium.webdriver.common.by import By

class RentFormPageLocators:

    RENT_HEADER = (By.CLASS_NAME, 'Order_Header__BZXOb')                        # форма 'Про аренду'
    DATA_FIELD = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]') #поле Дата "когда привезти самокат
    RENTAL_PERIOD_FIELD = (By.CLASS_NAME, 'Dropdown-placeholder')               #поле Срок аренды
    DROPDOWN_PLACEHOLDER_SUTKI = (By.XPATH, '//div[text() = "сутки"]')          #элемент выбора периода аредны
    COLOR_FIELD_BLACK = (By.ID, 'black')                                        #чек бокс "черный цвет"
    COMMENT_FIELD = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')                  #поле "Комментарий для курьера"
    BUTTON_ORDER = (By.XPATH, '//div[@class = "Order_Buttons__1xGrp"]/button[text()="Заказать"]')  #кнопка заказать на форме Аренды
    CONFIRM_ORDER_BUTTON_YES = (By.XPATH,
                            '//div[@class = "Order_Buttons__1xGrp"]/button[text()="Да"]')          #кнопка подтверждения заказа в всплывающем окне
    CONFIRM_WINDOW = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')  #окно подтверждения заказа
    ORDER_CONFIRMED = (By.CLASS_NAME,'Order_ModalHeader__3FDaJ')  #подтверждение "закан оформлен"
    NUMBER_ORDER = (By.CLASS_NAME, 'Order_Text__2broi')           #номер заказа
    BUTTON_CHECK_STATUS = (By.CLASS_NAME, 'Button_Button__ra12g.Button_Middle__1CSJM')   #кнопка Посмотреть статус
    TRACK_INFO = (By.CLASS_NAME, 'Track_OrderInfo__2fpDL')                #информация о заказе