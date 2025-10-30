import os
import shutil
from pathlib import Path
import pytest
from selene import browser
from selenium import webdriver
from dotenv import load_dotenv
from pages.cart_page import Cart_page
from pages.login_page import Login_page
from pages.product_page import Product_page
from selenium.webdriver.chrome.options import Options
from utils import attach



@pytest.fixture(scope="function")
def authorization():
    swag_labs_shop = Login_page()

    (
     swag_labs_shop
     .open_login_page()
     .insert_login('standard_user')
     .insert_password('secret_sauce')
     .click_login_button()
    )

@pytest.fixture(scope="function")
def add_products_to_cart():
    product_page = Product_page()

    (product_page
     .add_backpack_to_cart()
     .add_t_shirt_to_cart()
     .add_onesie_to_cart()
     .add_bike_light_to_cart()
     .add_jacket_to_cart()
     .add_red_t_shirt_to_cart())


@pytest.fixture(scope="function")
def product_in_cart():

    cart_page = Cart_page()

    cart_page.go_to_cart()
    cart_page.count_products_to_cart(
        'Sauce Labs Backpack',
        'Sauce Labs Bolt T-Shirt',
        'Sauce Labs Onesie',
        'Sauce Labs Bike Light',
        'Sauce Labs Fleece Jacket',
        'Test.allTheThings() T-Shirt (Red)')


@pytest.fixture(scope="session", autouse=True)
def clear_allure_results():

    allure_dir = Path("allure-results")

    if allure_dir.exists():
        shutil.rmtree(allure_dir)

    allure_dir.mkdir(exist_ok=True)

    yield


@pytest.fixture(scope="function", autouse=True)
def open_selenoid():
        load_dotenv()

        selenoid_login = os.getenv("SELENOID_LOGIN")
        selenoid_pass = os.getenv("SELENOID_PASS")
        selenoid_url = os.getenv("SELENOID_URL")

        options = Options()
        selenoid_capabilities = {
            "browserName": "firefox",
            "browserVersion": "124.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True,
            }
        }

        options.capabilities.update(selenoid_capabilities)
        driver = webdriver.Remote(
            command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
            options=options)

        # Настройка Selene браузера
        browser.config.driver = driver
        browser.config.base_url = 'https://www.saucedemo.com'
        driver.maximize_window()

        browser.config.driver = driver
        yield browser

        attach.add_screenshot(browser)
        #attach.add_logs(browser)
        attach.add_html(browser)
        attach.add_video(browser)

        browser.quit()




