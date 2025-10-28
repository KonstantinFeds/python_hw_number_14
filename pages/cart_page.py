import allure
from selene import browser, have


class Cart_page:

    @allure.step('клик по кнопке перехода в корзину')
    def go_to_cart(self):
        browser.element('[data-test="shopping-cart-link"]').click()

    @allure.step('наличие добавленных в корзину товаров')
    def count_products_to_cart(self,product1,product2,product3,product4,product5,product6):
        (browser.element('[data-test="cart-list"]').all('[data-test="inventory-item-name"]')
         .should(have.texts(product1,product2,product3,product4,product5,product6)))

