from selene import browser, have


class Cart_page:

    def go_to_cart(self):
        browser.element('[data-test="shopping-cart-link"]').click()

    def count_products_to_cart(self):
        browser.element('[data-test="cart-list"]').all('[data-test="inventory-item-name"]').should(have.texts((
        'Sauce Labs Backpack',
        'Sauce Labs Bolt T-Shirt',
        'Sauce Labs Onesie',
        'Sauce Labs Bike Light',
        'Sauce Labs Fleece Jacket',
        'Test.allTheThings() T-Shirt (Red)'
    )))

