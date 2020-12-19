import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


languages = [
    ("ru", "русский"),
    ("de", "немецкий"),
    ("ua", "украинский"),
    ("en-gb", "английский")
]


@pytest.mark.parametrize("code, lang", languages)
class TestLogin:
    def test_guest_should_see_login_link(self, browser, code, lang):
        link = f"http://selenium1py.pythonanywhere.com/{code}/"
        print("Проверяемый язык %s" % lang)
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_navbar_element(self, browser, code, lang):
        pass
        # этот тест тоже запустится дважды
