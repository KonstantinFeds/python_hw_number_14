from selene import browser


class Product_page:

    def add_backpack_to_cart(self):
        browser.element('#add-to-cart-sauce-labs-backpack').click()
        return self

    def add_t_shirt_to_cart(self):
        browser.element('#add-to-cart-sauce-labs-bolt-t-shirt').click()
        return self

    def add_onesie_to_cart(self):
        browser.element('#add-to-cart-sauce-labs-onesie').click()
        return self

    def add_bike_light_to_cart(self):
        browser.element('#add-to-cart-sauce-labs-bike-light').click()
        return self

    def add_jacket_to_cart(self):
        browser.element('#add-to-cart-sauce-labs-fleece-jacket').click()
        return self

    def add_red_t_shirt_to_cart(self):
        browser.element('[data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]').click()
        return self
