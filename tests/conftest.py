import pytest
from selene import browser
from pages.login_page import Login_page

"Cделать открытие браузера на всю сессию тестов"



@pytest.fixture()
def open_browser():

    browser.config.base_url = 'https://www.saucedemo.com'
    browser.driver.maximize_window()

    yield browser
    browser.quit()


@pytest.fixture()
def registration():
    swag_labs_shop = Login_page()

    (
     swag_labs_shop
     .open_login_page()
     .insert_login('standard_user')
     .insert_password('secret_sauce')
     .click_login_button()
    )
