from pages.order_page import Order_page


def test_checkout_order(open_browser,authorization,add_products_to_cart,product_in_cart):
    order_page = Order_page()

    (
    order_page
     .button_checkout()
     .input_firstname('Firsttest')
     .input_lastname('Lasttest')
     .input_postacode('1234567')
     .button_continue()
     .assert_product_in_cart('Sauce Labs Backpack',
                                      'Sauce Labs Bolt T-Shirt',
                                      'Sauce Labs Onesie',
                                      'Sauce Labs Bike Light',
                                      'Sauce Labs Fleece Jacket',
                                      'Test.allTheThings() T-Shirt (Red)')
     .button_finish()
     .assert_text_finish_order('Thank you for your order!')
     .button_back_home('Back Home')
     .assert_text_header('Swag Labs')
    )





