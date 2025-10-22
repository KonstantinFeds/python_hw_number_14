import pytest
from selene import browser
from pages.login_page import Login_page
from pages.product_page import Product_page

"Cделать открытие браузера на всю сессию тестов"



@pytest.fixture()
def open_browser():

    browser.config.browser_name = 'firefox'
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


@pytest.fixture()
def add_products_to_cart():
    product_page = Product_page()

    (product_page
     .add_backpack_to_cart()
     .add_t_shirt_to_cart()
     .add_onesie_to_cart()
     .add_bike_light_to_cart()
     .add_jacket_to_cart()
     .add_red_t_shirt_to_cart()
     .assert_count_product_to_cart('6'))

