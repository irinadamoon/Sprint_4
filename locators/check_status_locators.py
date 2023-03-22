from selenium.webdriver.common.by import By

class CheckStatusLocators:

    BUTTON_CANCEL_ORDER_STATUS_PAGE = [By.XPATH, "//button[text()='Отменить заказ']"]  # кн "Отменить заказ" на странице статусов заказа
    DATA_FIELD = [By.XPATH, "//div[@class='Track_OrderInfo__2fpDL']"]  # поле с данными


