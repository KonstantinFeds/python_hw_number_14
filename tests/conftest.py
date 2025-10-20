import pytest
from selene import browser


@pytest.fixture()
def open_browser():

    #open_browser('https://www.saucedemo.com/')
    browser.driver.maximize_window()


    yield browser

    browser.quit()