# ════════════════════════ SETTINGS ════════════════════════
from keywords import log_in_class
from keywords import hamgurger_menu_class
from keywords import products_class
from playwright.sync_api import sync_playwright

# ════════════════════════ VARIABLES ════════════════════════
page_link_variable=("https://www.saucedemo.com")

# ════════════════════════ TESTCASE ════════════════════════
def test_user_experience():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        context = browser.new_context()
        page = context.new_page()
        page.goto(page_link_variable)

        login_handler = log_in_class(page)
        hamburger_handler = hamgurger_menu_class(page)
        product_handler = products_class(page)

        login_handler.incorrect_password()
        login_handler.incorrect_username()
        login_handler.incorrect_password_and_username()
        login_handler.correct_password_and_username()
        
        hamburger_handler.about()
        page.go_back()
        hamburger_handler.log_out()
        login_handler.correct_password_and_username()
        hamburger_handler.all_items()
        
        product_handler.add_to_cart_main_page()
        product_handler.remove_from_cart_main_page()

        browser.close()
        