from pages.cart_page import Cart_page


def test_product_in_cart(authorization, add_products_to_cart):

    cart_page = Cart_page()

    cart_page.go_to_cart()
    cart_page.count_products_to_cart(
        'Sauce Labs Backpack',
        'Sauce Labs Bolt T-Shirt',
        'Sauce Labs Onesie',
        'Sauce Labs Bike Light',
        'Sauce Labs Fleece Jacket',
        'Test.allTheThings() T-Shirt (Red)')



