from pages.simple import Simple


def test_one(browser):
    simple_page = Simple(browser)
    simple_page.open()
    assert simple_page.is_displayed()


def test_two(browser):
    simple_page = Simple(browser)
    simple_page.open()
    simple_page.click()
    assert simple_page.result().text == 'Submitted'
