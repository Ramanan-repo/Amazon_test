from playwright.sync_api import Page , expect
import re
import time


def test_open_set_location(page : Page):
    page.goto("https://www.amazon.in/")
    page.wait_for_timeout(3000)
    page.locator("#nav-global-location-popover-link").click()
    expect(page.get_by_role("heading", name = "Choose your location")).to_be_visible()
    page.get_by_role("textbox", name= "or enter an Indian pincode").fill("560066")
    page.wait_for_timeout(2000)
    page.get_by_role("button", name ="Apply").click()
    expect(page.get_by_text("Bengaluru 560066")).to_be_visible()
    page.wait_for_timeout(3000)


def test_set_categories(page : Page):
    page.locator("#searchDropdownBox").select_option("search-alias=electronics")
    page.get_by_placeholder("Search Amazon.in").fill("Laptop")
    page.keyboard.press("Enter")
    expect(page.get_by_text("results for ")).to_be_visible()


def test_select_brand(page : Page):
    brands = page.locator("#brandsRefinements")
    expect(brands).to_be_visible()
    page.wait_for_timeout(2000)
    page.get_by_role("button", name = "See more, Brands").click()
    page.wait_for_timeout(2000)
    select_brand = brands.inner_text()
    print(select_brand)
    if "HP" in select_brand:
        page.get_by_role("link", name = "Apply the filter HP").click()
    else:
        print("HP brand is not there in brand")
    expect(page.get_by_text("Check each product page for other buying options.")).to_be_visible()


def test_select_country_of_origin(page: Page):
    expect(page.get_by_text("Country of Origin")).to_be_visible()
    page.get_by_role("link", name ="Apply the filter India")


def test_select_items(page: Page):
    """this method is select the items and
        add in the cart"""
    page.get_by_role("button", name ="Add to cart").first.click()
    page.locator("#nav-cart").first.click()
    expect(page.get_by_text("The shopping cart is a"
                            " temporary place to store")).to_be_visible()
    print("Success!, Amazon cart is opened")


def test_select_customer_review(page: Page):
    page.get_by_role("link", name = "Apply the filter 4 stars").click()


def test_proceed_to_buy_from_cart(page:Page):
    page.mouse.wheel(0, -600)
    page.locator("#nav-cart").click()
    page.wait_for_timeout(2000)

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






