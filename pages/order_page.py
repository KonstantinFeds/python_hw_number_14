from selene import browser, have


class Order_page:

    def button_checkout(self):
        browser.element('[data-test="checkout"]').click()
        return self

    def input_firstname(self,value):
        browser.element('[data-test="firstName"]').type(value)
        return self

    def input_lastname(self,value):
        browser.element('[data-test="lastName"]').type(value)
        return self

    def input_postacode(self,value):
        browser.element('[data-test="postalCode"]').type(value)
        return self

    def button_continue(self):
        browser.element('[data-test="continue"]').click()
        return self

    def assert_product_in_cart(self,product1,product2,product3,product4,product5,product6):
        browser.element('[data-test="cart-list"]').all('[data-test="inventory-item-name"]').should(have.exact_texts(product1,
                                                                                                                    product2,
                                                                                                                    product3,
                                                                                                                    product4,
                                                                                                                    product5,
                                                                                                                    product6))
        return self

    def button_finish(self):
        browser.element('[data-test="finish"]').click()
        return self

    def assert_text_finish_order(self,value):
        browser.element('[data-test="complete-header"]').should(have.exact_text(value))
        return self

    def button_back_home(self,value):
        browser.element('[data-test="back-to-products"]').should(have.exact_text(value)).click()
        return self

    def assert_text_header(self,value):
        browser.element('[class="header_label"]').should(have.exact_text(value))
        return self





