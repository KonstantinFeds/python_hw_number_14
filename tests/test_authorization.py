from selene import browser, have
from pages.page_swag_labs import Page_swag_labs


def test_authorization(open_browser):

    swag_labs_shop = Page_swag_labs()

    (
     swag_labs_shop
     .open_login_page()
     .insert_login('standard_user')
     .insert_password('secret_sauce')
     .click_login_button()
    )

    browser.element('.title').should(have.exact_text('Products'))



