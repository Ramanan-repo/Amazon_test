from playwright.sync_api import Page, expect
import time


def test_searching_product_in_row(page: Page, expected_text):
    Search_coloumn = page.locator("[data-component-type='s-search-result']")
    count = Search_coloumn.count()
    next_page = page.get_by_label("pagination")

    while True:

        count = Search_coloumn.count()
        found = False

        for i in range(count):
            print(f"Validating: {i + 1}: row and checking")
            page.wait_for_timeout(1000)
            heading = Search_coloumn.nth(i).locator("h2")
            actual_text = heading.inner_text(timeout=10000)
            print("Product:", actual_text)

            if expected_text.lower() in actual_text.lower():
                print(f"Matching found in row {i + 1}: {actual_text}")
                Search_coloumn.nth(i).get_by_role("button", name="Add to cart").click()
                page.wait_for_timeout(2000)
                found = True
                break

        if found:
            break

        next_button = next_page.get_by_text("Next")
        if next_button.is_visible() and next_button.is_enabled():
            print("Product not found. Moving to next page.")
            with (page.expect_navigation(wait_until="domcontentloaded", timeout=5000)):
                next_button.click()
            page.wait_for_timeout(1000)
            expect(page.get_by_text("Check each product page for "
                                    "other buying options")).to_be_visible(timeout=2000)
        else:
            raise AssertionError("Matching product not found in any page")