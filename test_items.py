import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_items(browser):
	browser.get(link)
	time.sleep(15)
	button = find_element_by_css_selector(".btn-add-to-basket")
	assert button