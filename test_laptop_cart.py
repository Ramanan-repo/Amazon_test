from playwright.sync_api import Page
import test_main
import time

def test_login_laptop_cart(page: Page):
    """testing covered in this testcase: Adding location, select laptop,
        adding in cart and proceeding to buy"""

    test_main.test_open_set_location(page)
    page.wait_for_timeout(1000)
    test_main.test_set_categories(page)
    test_main.test_select_brand(page)
    test_main.test_select_customer_review(page)
    test_main.test_select_items(page)
    test_main.test_proceed_to_buy_from_cart(page)

