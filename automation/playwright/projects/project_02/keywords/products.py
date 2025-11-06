# ════════════════════════ SETTINGS ════════════════════════
from playwright.sync_api import sync_playwright

# ════════════════════════ VARIABLES ════════════════════════


# ════════════════════════ KEYWORDS ════════════════════════
class products_class():
    def __init__(self, page):
        self.page = page
    
    def add_to_cart_main_page(self):
        self.page.locator("[data-test=\"add-to-cart-test.allthethings()-t-shirt-(red)\"]").click()
        self.page.locator("[data-test=\"(WRITE HERE WHAT THE DATA TEST IS)\"]").click()
        self.page.locator("[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]").click()
        self.page.locator("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]").click()
        self.page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
        self.page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()

    def remove_from_cart_main_page(self):
        self.page.locator("[data-test=\"remove-sauce-labs-backpack\"]").click()
        self.page.locator("[data-test=\"remove-sauce-labs-bike-light\"]").click()
        self.page.locator("[data-test=\"remove-sauce-labs-bolt-t-shirt\"]").click()
        self.page.locator("[data-test=\"remove-sauce-labs-fleece-jacket\"]").click()
        self.page.locator("[data-test=\"remove-sauce-labs-onesie\"]").click()
        self.page.locator("[data-test=\"remove-test.allthethings()-t-shirt-(red)\"]").click()