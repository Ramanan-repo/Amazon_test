from playwright.sync_api import Page, expect
import time



def test_saving_authentication_login_amazon_shopping(page: Page):
    page.get_by_text("Account & Lists").click()
    expect(page.get_by_text("Sign in or create account")).to_be_visible(timeout = 3000)
    page.locator("#ap_email_login").fill("8608001535")
    page.get_by_role("button", name ="Continue").first.click()
    expect(page.locator("#auth-email-claim")).to_contain_text("8608001535")
    page.locator("#ap_password").press_sequentially("*************")
    page.locator("#signInSubmit").click()
    page.context.storage_state(path="amazon_auth.json")
    print("Amazon authenticated session saved successfully")

    time.sleep(4)





