import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_site_accepts_language(browser):
	browser.get(link)
	time.sleep(30)
	button = find_element_by_css_selector(".btn-add-to-basket")
	assert button
