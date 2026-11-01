from playwright.sync_api import Page , expect
import pytest
import re
import time


def test_set_categories(page : Page):
    """Searching Laptop"""

    page.locator("#searchDropdownBox").select_option("search-alias=electronics")
    page.get_by_placeholder("Search Amazon.in").fill("Laptop")
    page.keyboard.press("Enter")
    page.wait_for_url("**/s?k=**", wait_until="domcontentloaded", timeout=10000)
    expect(page.get_by_text("results for ")).to_be_visible()

def test_select_brand(page : Page):
    """Searching brand for Laptop and clicking HP"""
    brands = page.locator("#brandsRefinements")
    expect(brands).to_be_visible(timeout = 2000)
    see_more = brands.get_by_text("See more")
    expect(see_more).to_be_visible()
    see_more.click()
    expect(page.get_by_text("See Less")).to_be_visible()
    select_brand = brands.inner_text()
    print(select_brand)
    if "HP" in select_brand:
        page.get_by_role("link", name = "Apply the filter HP").click()
    else:
        pytest.skip("HP brand is not there in brand")
    expect(page.get_by_text("Check each product page for other buying options.")).to_be_visible()


def test_select_items(page: Page):
    """this method is select the items and
        add in the cart"""
    page.get_by_role("button", name ="Add to cart").first.click()
    page.locator("#nav-cart").scroll_into_view_if_needed()
    page.locator("#nav-cart").first.click()
    page.wait_for_url("**=nav_cart", timeout=2000)
    expect(page.get_by_text("The shopping cart is a"
                            " temporary place to store")).to_be_visible()
    print("\nSuccess!, Amazon cart is opened\n")


def test_select_customer_review(page: Page):
    """This method is for selecting 4 star rating product"""
    page.get_by_role("link", name = "Apply the filter 4 stars").click()
    time.sleep(2)


def test_proceed_to_buy_from_cart(page:Page):
    """this method is to select the Amazon cart button in top right corner"""
    page.mouse.wheel(0, -600)
    page.locator("#nav-cart").click()
    page.wait_for_url("**=nav_cart", timeout = 2000)
    expect(page.get_by_text("The shopping cart is a"
                            " temporary place to store")).to_be_visible()
    print("\nSuccess!, Amazon cart is opened\n")


def test_selecting_bike_yamaha(page:Page):
    page.locator("#searchDropdownBox").select_option("search-alias=automotive")
    page.get_by_placeholder("Search Amazon.in").fill("R15")
    page.keyboard.press("Enter")
    expect(page.locator("#brandsRefinements")).to_be_visible()
    page.get_by_role("button", name="See more, Brands").click()
    yamaha_filter = page.get_by_role("link",name="Apply the filter YAMAHA to narrow results")
    if yamaha_filter.count() > 0:
        yamaha_filter.click()
    page.wait_for_timeout(2000)


def test_select_oil_filter(page : Page):

    product = page.get_by_role("listitem").filter(has_text="Yamaha Oil Filter")
    adding_cart = product.get_by_role("button", name = "Add to cart")
    if adding_cart.count() > 0:
        adding_cart.first.click()
    else:
        print("Yamaha Oil Filter is not available in List")

def test_select_country_of_origin(page: Page):
    expect(page.get_by_text("Country of Origin")).to_be_visible()
    page.get_by_role("link", name ="Apply the filter India")

