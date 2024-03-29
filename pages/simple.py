from pages.base_page import BasePage
from selenium.webdriver.common.by import By

button_selector = (By.ID, 'submit-id-submit')
result_detector = (By.ID, 'result-text')


class Simple(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://www.qa-practice.com/elements/button/simple')

    def button(self):
        return self.find(button_selector)

    def is_displayed(self):
        return self.button().is_displayed()

    def click(self):
        return self.button().click()

    def result(self):
        return self.find(result_detector)
