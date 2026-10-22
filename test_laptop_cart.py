from playwright.sync_api import Page, expect
import test_main
import time

def test_laptop_cart(page: Page):
    test_main.test_open_set_location(page)
    page.wait_for_timeout(1000)
    test_main.test_set_categories(page)
    test_main.test_select_brand(page)
    test_main.test_select_customer_review(page)
    test_main.test_select_items(page)
    test_main.test_proceed_to_buy_from_cart(page)


def test_bike_oil_filter_cart(page: Page):
    test_main.test_open_set_location(page)
    page.wait_for_timeout(1000)
    test_main.test_selecting_bike_yamaha(page)

    product = page.get_by_role("listitem").filter(has_text="Yamaha Oil Filter")
    adding_cart = product.get_by_role("button", name="Add to cart")
    if adding_cart.count() > 0:
        adding_cart.click()
    else:
        print("\nYamaha Oil Filter is not available in List")
    expect(page.get_by_text("1 in cart")).to_be_visible()
    print("\nSuccess!, Oil filter is added to cart")
    
    page.wait_for_timeout(1000)
    test_main.test_select_items(page)



