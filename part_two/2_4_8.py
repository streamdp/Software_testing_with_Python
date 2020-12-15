from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    wait = WebDriverWait(browser, 12)
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    wait.until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))

    button = wait.until(EC.element_to_be_clickable((By.ID, "book")))
    button.click()

    x = wait.until(EC.presence_of_element_located((By.ID, "input_value"))).text
    y = calc(x)
    answer = wait.until(EC.presence_of_element_located((By.ID, "answer")))
    answer.send_keys(y)

    button = wait.until(EC.presence_of_element_located((By.ID, "solve")))
    button.click()

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()

finally:
    time.sleep(10)
    browser.quit()