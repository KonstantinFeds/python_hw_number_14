from selene import browser, have
from pages.login_page import Login_page


def test_authorization(open_browser):

    login_page = Login_page()

    (
     login_page
     .open_login_page()
     .insert_login('standard_user')
     .insert_password('secret_sauce')
     .click_login_button()
    )

    browser.element('.title').should(have.exact_text('Products'))



