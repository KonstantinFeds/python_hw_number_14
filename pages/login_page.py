import allure
from selene import browser, have


class Login_page:

    @allure.step('открываем главную страницу Swag Labs')
    def open_login_page(self):
        browser.open('/')
        return self

    @allure.step('указываем username')
    def insert_login(self,value):
        browser.element('#user-name').type(value)
        return self

    @allure.step('указываем password')
    def insert_password(self,value):
        browser.element('#password').type(value)
        return  self

    @allure.step('клик на кнопку Login')
    def click_login_button(self):
        browser.element('#login-button').click()
        return self

    @allure.step('проверка текста на странице продуктов после логина')
    def assert_text_after_login(self,value):
        browser.element('.title').should(have.exact_text(value))



