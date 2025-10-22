from pages.cart_page import Cart_page


def test_product_in_cart(open_browser,registration,add_products_to_cart):

    cart_page = Cart_page()

    cart_page.go_to_cart()
    cart_page.count_products_to_cart()


