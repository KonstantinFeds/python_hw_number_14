from selene import browser, have


class Cart_page:

    def go_to_cart(self):
        browser.element('[data-test="shopping-cart-link"]').click()

    def count_products_to_cart(self,product1,product2,product3,product4,product5,product6):
        (browser.element('[data-test="cart-list"]').all('[data-test="inventory-item-name"]')
         .should(have.texts(product1,product2,product3,product4,product5,product6
    )))

