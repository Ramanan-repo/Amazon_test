from playwright.sync_api import Page, expect
import test_Amazon_buy
import test_finding_amazon_item_in_row
import new_tab_utils
import re
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
            expect(page.get_by_text("1 in cart")).to_be_visible(timeout=3000)
        else:
            print("\nYamaha Oil Filter is not available in List")
        print("\nSuccess!, Oil filter is added to cart")

        print("Step 3: Clicking on Cart button")
        test_Amazon_buy.test_proceed_to_buy_from_cart(page)
        print("Yamaha Oil filter is added to cart Successfully")

    except Exception as e:
        print(f"The test is Failed: {e}")
        raise


def test_select_GOT_pocket_key_chain(page: Page,setting_location):
    """This method will search for Game of Thrones and search
        for pocket watch and adding into the cart
        note: this will check all the product until getting proper one."""

    print("\nStep 1: Search 'Game of thrones' in search bar")
    page.get_by_placeholder("Search Amazon.in").press_sequentially("Game of thrones")
    page.keyboard.press("Enter")
    expect(page.get_by_text("Check each product page "
                            "for other buying options")).to_be_visible(timeout=3000)
    print("Searched 'Game of thrones' successfully")

    print("Step 2: Checking For Keychain")
    expected_text = "Stark Logo Case Analog Antique Pocket Watch Key Chain"

    test_finding_amazon_item_in_row.test_searching_product_in_row(page, expected_text)
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

def test_buy_television_product(authenticated_session: Page,setting_location):
    """This method is to select Television product from product suggestions
        and selecting the product in another tab and adding in cart """

    page = authenticated_session
    print("Step 1: selecting appliances in search bar")
    page.locator("#searchDropdownBox").select_option("search-alias=appliances")
    page.get_by_placeholder("Search Amazon.in").fill("Samsung TV")
    result = page.locator(".autocomplete-results-container")
    suggestion = result.get_by_text("samsung tv 55 inch")
    if suggestion.is_visible():
        suggestion.click()
    else:
        page.keyboard.press("Enter")
    page.wait_for_timeout(4000)

    print("Step 2: Selecting model year")
    Model_year = page.get_by_label("Apply the filter 2026 to narrow results")
    Model_year.click()

    print("Step 3: Selecting four star rating")
    test_Amazon_buy.test_select_customer_review(page)

    print("Step 4: Select Samsung TV for in product ROW")
    search_results = page.locator("[data-component-type='s-search-result']")
    samsung_product = search_results.filter(has_text="Samsung").first
    if samsung_product.get_by_text("Samsung").is_visible():
        print("Samsung product is available")
        samsung_product.get_by_role("button", name="Add to cart").click()
        with page.expect_popup() as popup_info:
            samsung_product.locator(".a-price").first.click()
        new_tab = popup_info.value
        new_tab.wait_for_load_state("domcontentloaded")
    else:
        raise Exception("Samsung product is not available")

    print("Step 5: Verify Samsung brand is selected")
    title = new_tab.locator("#productTitle").first
    expect(title).to_be_visible(timeout=3000)
    expect(title).to_contain_text("Samsung")
    expect(title).to_contain_text("2026")

    print("Step 6: Navigating to Nav cart")
    try:
        new_tab_utils.test_new_tab_nav_cart(new_tab)
    except Exception as e:
        print(f"Test failed,{e}")
        raise
