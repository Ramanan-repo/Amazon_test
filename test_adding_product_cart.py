from playwright.sync_api import Page, expect
import test_Amazon_buy
import test_finding_amazon_item_in_row
import time

def test_laptop_cart(page: Page):
    """This testcase is for Selecting brand and
       adding in cart and verifying"""

    try:
        print("Step 1: Selecting categories")
        test_Amazon_buy.test_set_categories(page)
        print("Categories selected successfully")

        print("Step 2: Selecting brand")
        test_Amazon_buy.test_select_brand(page)
        print("Brand selected successfully")

        print("Step 3: Selecting customer review")
        test_Amazon_buy.test_select_customer_review(page)
        print("Customer review selected successfully")

        print("Step 4: Selecting items")
        test_Amazon_buy.test_select_items(page)
        print("Items selected successfully")

    except Exception as e:
        print(f"Test failed: {e}")
        raise

def test_bike_oil_filter_cart(page: Page):
    """This testcase is for selecting Yamaha Oil
       filter and adding in cart and verifying"""

    try:
        print("Step 1: Opening Amazon and Yamaha Bike")
        test_Amazon_buy.test_selecting_bike_yamaha(page)
        print(" Yamaha bike search completed")

        print("Step 2: Selecting Yamaha Oil filter")
        product = page.get_by_role("listitem").filter(has_text="Yamaha Oil Filter")
        adding_cart = product.get_by_role("button", name="Add to cart")
        if adding_cart.count() > 0:
            adding_cart.click()
            expect(page.get_by_text("1 in cart")).to_be_visible(timeout = 3000)
        else:
            print("\nYamaha Oil Filter is not available in List")
        print("\nSuccess!, Oil filter is added to cart")

        print("Step 3: Clicking on Cart button")
        test_Amazon_buy.test_proceed_to_buy_from_cart(page)
        print("Yamaha Oil filter is added to cart Successfully")

    except Exception as e:
        print(f"The test is Failed: {e}")
        raise


def test_select_GOT_pocket_key_chain(page :Page):

    print("\nStep 1: Search 'Game of thrones' in search bar")
    page.get_by_placeholder("Search Amazon.in").press_sequentially("Game of thrones")
    page.keyboard.press("Enter")
    expect(page.get_by_text("Check each product page "
                            "for other buying options")).to_be_visible(timeout = 3000)
    print("Searched 'Game of thrones' successfully")

    print("Step 2: Checking For Keychain")
    expected_text = "Stark Logo Case Analog Antique Pocket Watch Key Chain"

    test_finding_amazon_item_in_row.test_searching_product_in_row(page,expected_text)
    print("Keychain found successfully and added to cart")

    print("Step 3: pressing cart button")
    test_Amazon_buy.test_proceed_to_buy_from_cart(page)

    print("Step 4: Verify Item is selected or not")
    expect_text = "Pocket Watch Key Chain"
    actual_item_in_cart = page.locator(".sc-list-item")
    actual_text = actual_item_in_cart.inner_text()
    assert expect_text.lower() in actual_text.lower(), \
        "Product is not matching, Test failed!"
    print("Test Passed, Keychain is added to cart")


























