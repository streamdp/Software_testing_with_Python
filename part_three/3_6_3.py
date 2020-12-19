import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_answer():
    return math.log(int(time.time()))


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('lesson_id',
                         ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, lesson_id):
    wait = WebDriverWait(browser, 50)
    link = f"https://stepik.org/lesson/{lesson_id}/step/1"
    browser.get(link)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea"))).send_keys(str(get_answer()))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))).click()
    normal_state_text = 'Correct!'
    state = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "pre.smart-hints__hint"))).text
    assert state == normal_state_text, f"state must be {normal_state_text}, but get {state}"