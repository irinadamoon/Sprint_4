
import allure
from pages.main_page import MainPage


class TestRegisterFooterButton:


    @allure.title("Проверка что при клике на 1-й вопрос появляется соответствующий ответ")
    @allure.description("Текст ответа виден и соответствует ожидаемому")
    def test_correct_answer_1(self, driver):
        main_page = MainPage(driver)

        main_page.go_to_questions_on_main_page()
        main_page.click_question_1()

        assert main_page.check_answer_1()


    @allure.title("Проверка что при клике на 2-й вопрос появляется соответствующий ответ")
    @allure.description("Текст ответа виден и соответствует ожидаемому")
    def test_correct_answer_2(self, driver):
        main_page = MainPage(driver)

        main_page.go_to_questions_on_main_page()
        main_page.click_question_2()

        assert main_page.check_answer_2()


    @allure.title("Проверка что при клике на 3-й вопрос появляется соответствующий ответ")
    @allure.description("Текст ответа виден и соответствует ожидаемому")
    def test_correct_answer_3(self, driver):
        main_page = MainPage(driver)

        main_page.go_to_questions_on_main_page()
        main_page.click_question_3()

        assert main_page.check_answer_3()


    @allure.title("Проверка что при клике на 4-й вопрос появляется соответствующий ответ")
    @allure.description("Текст ответа виден и соответствует ожидаемому")
    def test_correct_answer_4(self, driver):
        main_page = MainPage(driver)

        main_page.go_to_questions_on_main_page()
        main_page.click_question_4()

        assert main_page.check_answer_4()


    @allure.title("Проверка что при клике на 5-й вопрос появляется соответствующий ответ")
    @allure.description("Текст ответа виден и соответствует ожидаемому")
    def test_correct_answer_5(self, driver):
        main_page = MainPage(driver)

        main_page.go_to_questions_on_main_page()
        main_page.click_question_5()

        assert main_page.check_answer_5()


    @allure.title("Проверка что при клике на 6-й вопрос появляется соответствующий ответ")
    @allure.description("Текст ответа виден и соответствует ожидаемому")
    def test_correct_answer_6(self, driver):
        main_page = MainPage(driver)

        main_page.go_to_questions_on_main_page()
        main_page.click_question_6()

        assert main_page.check_answer_6()


    @allure.title("Проверка что при клике на 7-й вопрос появляется соответствующий ответ")
    @allure.description("Текст ответа виден и соответствует ожидаемому")
    def test_correct_answer_7(self, driver):
        main_page = MainPage(driver)

        main_page.go_to_questions_on_main_page()
        main_page.click_question_7()

        assert main_page.check_answer_7()


    @allure.title("Проверка что при клике на 8-й вопрос появляется соответствующий ответ")
    @allure.description("Текст ответа виден и соответствует ожидаемому")
    def test_correct_answer_8(self, driver):
        main_page = MainPage(driver)

        main_page.go_to_questions_on_main_page()
        main_page.click_question_8()

        assert main_page.check_answer_8()