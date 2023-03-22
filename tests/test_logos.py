
import allure
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestLogos:

    @allure.title("Проверка перехода на главную страницу сайта по клику на логотип 'Самокат'")
    @allure.description("Переход с гл.страницы в форму заказа по клику кн. 'Заказать' в шапке сайта и обратно по клику на логотип 'Самокат'")
    def test_logo_scooter(self, driver):
        main_page = MainPage(driver)

        main_page.go_to_register_page_using_header_button()
        main_page.click_logo_scooter()

        assert main_page.check_main_page_loaded()


    @allure.title("Проверка перехода на 'Дзен' по клику на логотип 'Яндекс'")
    @allure.description("Переход с гл.страницы на сайт 'Дзен' по клику на логотип 'Яндекс'")
    def test_logo_yandex(self, driver):
        main_page = MainPage(driver)

        assert main_page.check_yandex_url() == MainPageLocators.URL_DZEN



