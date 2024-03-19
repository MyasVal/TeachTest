from selenium import webdriver
import pytest


@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    return chrome_browser
