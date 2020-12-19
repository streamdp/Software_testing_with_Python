import time
import math
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_answer():
    return math.log(int(time.time()))


try:
    print("\nstart browser for test..")
    browser = webdriver.Chrome()

    wait = WebDriverWait(browser, 50)
    link = f"https://stepik.org/lesson/236895/step/1"
    browser.get(link)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea"))).send_keys(str(get_answer()))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))).click()
    normal_state_text = 'Correct!'
    state = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "pre.smart-hints__hint"))).text
    assert state == normal_state_text, f"state must be {normal_state_text}, but get {state}"

finally:
    print("\nquit browser..")
    browser.quit()
