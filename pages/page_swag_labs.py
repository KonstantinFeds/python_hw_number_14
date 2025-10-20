from selene import browser


class Page_swag_labs:

    def open_login_page(self):
        browser.open('https://www.saucedemo.com/')
        return self

    def insert_login(self,value):
        browser.element('#user-name').type(value)
        return self

    def insert_password(self,value):
        browser.element('#password').type(value)
        return  self

    def click_login_button(self):
        browser.element('#login-button').click()
        return self



