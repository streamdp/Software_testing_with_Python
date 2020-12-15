from selenium import webdriver
import os
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_css_selector("[name='firstname']")
    first_name.send_keys("Ivan")
    last_name = browser.find_element_by_css_selector("[name='lastname']")
    last_name.send_keys("Petrov")
    email = browser.find_element_by_css_selector("[name='email']")
    email.send_keys("ivan.petrov@gmail.com")

    file = 'file.txt'
    open(file, 'a').close()  # создаём , если отсутствует

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    load_file = browser.find_element_by_css_selector("[type='file']")
    load_file.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    os.remove(file)  # удаляем

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()








