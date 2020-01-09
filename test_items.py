import time

from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_is_present(browser):
    browser.get(link)
    time.sleep(30)
    try:
        button = browser.find_element_by_css_selector(".btn-add-to-basket")
    except NoSuchElementException:
        button = None

    assert button is not None, "Button not found"
