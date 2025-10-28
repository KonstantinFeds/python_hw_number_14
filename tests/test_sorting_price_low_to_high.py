from pages.product_page import Product_page

def test_sorting_price_low_to_high(authorization):

    product_page = Product_page()

    (
    product_page
     .sorting_button()
     .select_sort_low_to_high()
     .sorting_products_with_filter_price_low_to_high('$7.99','$9.99','$15.99','$15.99','$29.99','$49.99')
    )
