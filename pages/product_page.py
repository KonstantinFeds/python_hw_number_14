from selene import browser, have


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

    def assert_count_product_to_cart(self,value):
        browser.element('[data-test="shopping-cart-badge"]').should(have.exact_text(value))
        return self

    def sorting_button(self):
        browser.element('[data-test="product-sort-container"]').click()
        return self

    def select_sort_low_to_high(self):
        browser.element('[value="lohi"]').click()
        return self

    def sorting_products_with_filter_price_low_to_high(self,product1,product2,product3,product4,product5,product6):
        browser.element('[data-test="inventory-list"]').all('[data-test="inventory-item-price"]').should(
            have.exact_texts(product1,product2,product3,product4,product5,product6))


