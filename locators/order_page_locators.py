from selenium.webdriver.common.by import By

class OrderFormPageLocators:

     ORDER_HEADER = (By.CLASS_NAME, 'Order_Header__BZXOb')                    #имя формы заказа "Для кого самокат"
     NAME_FIELD = (By.XPATH, '//input[@placeholder="* Имя"]')                 #поле Имя
     LAST_NAME_FIELD = (By.XPATH, '//input[@placeholder="* Фамилия"]')        #поле Фамилия
     ADDRESS_FIELD = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')   #поле Адрес
     STATION_METRO_FIELD = (By.XPATH, '//input[@placeholder="* Станция метро"]')          #поле для выбора "Станция метро"
     METRO_STATION_SOKOLNIKI = (By.XPATH, './/div[text()="Сокольники"]')                  #станция метро Сокольники
     METRO_STATION_CHERKOZOVSKAYA = (By.XPATH, './/div[text()="Черкизовская"]')           #станция метро Черкизовская
     PHONE_NUMBER_FIELD = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')  #поле номер телефона
     NEXT_BUTTON = (By.CLASS_NAME, 'Button_Button__ra12g.Button_Middle__1CSJM')                     #кнопка Далее
     LOGO_SAMOKAT = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')                                    #логотип "самоката"