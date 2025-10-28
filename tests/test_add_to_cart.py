from pages.product_page import Product_page


def test_add_to_cart(authorization):
    product_page = Product_page()

    (product_page
     .add_backpack_to_cart()
     .add_t_shirt_to_cart()
     .add_onesie_to_cart()
     .add_bike_light_to_cart()
     .add_jacket_to_cart()
     .add_red_t_shirt_to_cart()
     .assert_count_product_to_cart('6'))

