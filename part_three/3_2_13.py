import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistrationForms(unittest.TestCase):
    text_to_compare = "Congratulations! You have successfully registered!"

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 5)

    def get_first_name(self):
        return self.browser.find_element_by_css_selector("div.first_block > div.form-group.first_class > input")

    def get_last_name(self):
        return self.browser.find_element_by_css_selector("div.first_block > div.form-group.second_class > input")

    def get_email(self):
        return self.browser.find_element_by_css_selector("div.first_block > div.form-group.third_class > input")

    def get_submit_button(self):
        return self.browser.find_element_by_css_selector("button.btn")

    def get_target_text(self):
        return self.browser.find_element_by_tag_name("h1").text

    def test_registration_form_one(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.browser.get(link)
        # Ваш код, который заполняет обязательные поля
        self.get_first_name().send_keys("Ivan")
        self.get_last_name().send_keys("Petrov")
        self.get_email().send_keys("ivan.petrov@gmail.com")
        # Отправляем заполненную форму
        self.get_submit_button().click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        # находим элемент, содержащий текст
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(self.text_to_compare, self.get_target_text(),
                         f"Text should be the same, but {self.text_to_compare} != {self.get_target_text()}")

    def test_registration_form_two(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.browser.get(link)
        # Ваш код, который заполняет обязательные поля
        self.get_first_name().send_keys("Ivan")
        self.get_last_name().send_keys("Petrov")
        self.get_email().send_keys("ivan.petrov@gmail.com")
        # Отправляем заполненную форму
        self.get_submit_button().click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        # находим элемент, содержащий текст
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(self.text_to_compare, self.get_target_text(),
                         f"Text should be the same, but {self.text_to_compare} != {self.get_target_text()}")

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
