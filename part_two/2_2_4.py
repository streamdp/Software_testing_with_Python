from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    people_radio = browser.find_element_by_id("peopleRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", people_radio)
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

    robot_checkbox = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_checkbox)
    robot_checkbox.click()
    robots_radio = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robots_radio)
    robots_radio.click()

    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is not None, "Robots radio is selected successfully"

    # Отправляем заполненную форму
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # browser.execute_script("window.scrollBy(0, 100);")
    button.click()
    assert True

finally:
    time.sleep(5)
    browser.quit()