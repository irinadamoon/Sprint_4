
import allure
from pages.main_page import MainPage
from pages.register_form_page import RegisterForm
from pages.rent_page import RentPage


# тест возможности регистрации по кн "Заказать" в футере
class TestRegisterFooterButton:


    @allure.title("Тест возможности регистрации по кн 'Заказать' в футере")
    @allure.description("Заполнение полей ввода, подтверждение заказа, проверка, что заказ подтвержден")
    def test_register_using_footer_order_button(self, driver, data_base):
        main_page = MainPage(driver)
        register_page = RegisterForm(driver, data_base)
        rent_page = RentPage(driver, data_base)


        main_page.go_to_register_page_using_footer_button()
        register_page.fill_in_registration_form(data_base)
        rent_page.rent_window_loaded()
        rent_page.order_black_scooter_using_footer_order_button(data_base)

        assert rent_page.check_order_status()
