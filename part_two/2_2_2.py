from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    y = int(num1) + int(num2)

    select = browser.find_element_by_id("dropdown")
    select.click()

    check_option = browser.find_element_by_css_selector(f"[value='{str(y)}']").click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
