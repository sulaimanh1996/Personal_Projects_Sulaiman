# ════════════════════════ SETTINGS ════════════════════════
from playwright.sync_api import sync_playwright

# ════════════════════════ VARIABLES ════════════════════════
FIRST_NAME = "test"
LAST_NAME = "test"
ZIPCODE = "test"
# ════════════════════════ KEYWORDS ════════════════════════
class payment_class():
    def __init__(self, page):
        self.page = page
    
    def go_to_basket(self):
        self.page.locator(".shopping_cart_link").click()

    def remove_from_basket(self):
        self.page.locator("#remove-sauce-labs-backpack").click()
        self.page.locator("#remove-sauce-labs-bike-light").click()
        self.page.locator("#remove-sauce-labs-fleece-jacket").click()
        self.page.locator("#remove-sauce-labs-bolt-t-shirt").click()
        self.page.locator("#remove-sauce-labs-onesie").click()
        self.page.locator("[data-test=\"remove-test.allthethings()-t-shirt-(red)\"]").click()

    def go_to_checkout(self):
        self.page.locator("[name=\"checkout\"]").click()

    def no_first_name(self):
        self.page.fill("[id='first-name']", FIRST_NAME) 
        self.page.fill("[id='last-name']", LAST_NAME) 
        self.page.fill("[id='postal-code']", ZIPCODE) 
        self.page.click("[id='login-button']") 
        assert "Error: First Name is required" in self.page.content()

    def no_last_name(self):
        self.page.fill("[id='first-name']", FIRST_NAME) 
        self.page.fill("[id='last-name']", LAST_NAME) 
        self.page.fill("[id='postal-code']", ZIPCODE) 
        self.page.click("[id='login-button']") 
        assert "Error: Last Name is required" in self.page.content()

    def no_zipcode(self):
        self.page.fill("[id='first-name']", FIRST_NAME) 
        self.page.fill("[id='last-name']", LAST_NAME) 
        self.page.fill("[id='postal-code']", ZIPCODE) 
        self.page.click("[id='login-button']") 
        assert "Error: Postal Code is required" in self.page.content()

