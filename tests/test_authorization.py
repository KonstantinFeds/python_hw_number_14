from pages.login_page import Login_page


def test_authorization():

    login_page = Login_page()

    (
     login_page
     .open_login_page()
     .insert_login('standard_user')
     .insert_password('secret_sauce')
     .click_login_button()
    )

    login_page.assert_text_after_login('Products')



