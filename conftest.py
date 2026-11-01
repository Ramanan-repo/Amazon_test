from playwright.sync_api import Page , expect
import pytest
import re
import time

@pytest.fixture(autouse=True)
def test_open_set_location(page : Page):
    page.goto("https://www.amazon.in/")
    page.wait_for_timeout(3000)                         #Timeout for URL loading
    expect(page.locator("#nav-logo-sprites")).to_be_visible()
    page.locator("#nav-global-location-popover-link").click()
    expect(page.get_by_role("heading", name = "Choose your location")).to_be_visible(timeout = 3000)
    page.get_by_role("textbox", name= "or enter an Indian pincode").fill("560066")
    page.wait_for_timeout(2000)
    page.get_by_role("button", name ="Apply").click()
    expect(page.get_by_text("Bengaluru 560066")).to_be_visible()