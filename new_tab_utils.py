from playwright.sync_api import Page, expect


def test_new_tab_nav_cart(new_tab : Page):
    new_tab.mouse.wheel(0, -600)
    item_in_cart_btn = new_tab.locator("#nav-cart")
    item_in_cart_btn.click()
    expect(item_in_cart_btn.get_by_text("1"))
    new_tab.wait_for_url("**=nav_cart", timeout=5000)
    expect(new_tab.get_by_text("The shopping cart is a"
                               " temporary place to store")).to_be_visible()
    print("\nSuccess!, Amazon cart is opened and Item is added to cart\n")