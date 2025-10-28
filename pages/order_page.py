import allure
from selene import browser, have


class Order_page:

    @allure.step('клик по кнопке для перехода оформления заказа')
    def button_checkout(self):
        browser.element('[data-test="checkout"]').click()
        return self

    @allure.step('указание имени')
    def input_firstname(self,value):
        browser.element('[data-test="firstName"]').type(value)
        return self

    @allure.step('указание фамилии')
    def input_lastname(self,value):
        browser.element('[data-test="lastName"]').type(value)
        return self

    @allure.step('указание индекса почты')
    def input_postacode(self,value):
        browser.element('[data-test="postalCode"]').type(value)
        return self

    @allure.step('клик по кнопке продолжить')
    def button_continue(self):
        browser.element('[data-test="continue"]').click()
        return self

    @allure.step('проверка товаров в заказе')
    def assert_product_in_cart(self,product1,product2,product3,product4,product5,product6):
        browser.element('[data-test="cart-list"]').all('[data-test="inventory-item-name"]').should(have.exact_texts(
            product1,
            product2,
            product3,
            product4,
            product5,
            product6))
        return self

    @allure.step('клик на кнопку завершения оформления заказа')
    def button_finish(self):
        browser.element('[data-test="finish"]').click()
        return self

    @allure.step('проверка текста после оформления заказа')
    def assert_text_finish_order(self,value):
        browser.element('[data-test="complete-header"]').should(have.exact_text(value))
        return self

    @allure.step('клик по кнопка возврата на начальную страницу')
    def button_back_home(self,value):
        browser.element('[data-test="back-to-products"]').should(have.exact_text(value)).click()
        return self

    @allure.step('проверка текста на начальной странице')
    def assert_text_header(self,value):
        browser.element('[class="header_label"]').should(have.exact_text(value))
        return self





