# ════════════════════════ SETTINGS ════════════════════════
from playwright.sync_api import sync_playwright
from keywords import log_in_class, hamgurger_menu_class, products_class, setup_class, payment_class

# ════════════════════════ TESTCASE ════════════════════════
# def test_log_in_correct_and_incorrect():
#     with sync_playwright() as p:

#         setup_handler = setup_class(p)
#         browser, page = setup_handler.setup_browser()
        
#         login_handler = log_in_class(page)
#         login_handler.incorrect_password()
#         login_handler.incorrect_username()
#         login_handler.incorrect_password_and_username()
#         login_handler.correct_password_and_username()

#         browser.close()

# def test_hamburger_menu_testing():
#     with sync_playwright() as p:

#         setup_handler = setup_class(p)
#         browser, page = setup_handler.setup_browser()        

#         login_handler = log_in_class(page)
#         login_handler.correct_password_and_username()

#         hamburger_handler = hamgurger_menu_class(page)
#         hamburger_handler.about()
#         page.go_back()
#         hamburger_handler.log_out()
#         login_handler.correct_password_and_username()
#         hamburger_handler.all_items()

#         browser.close()

# def test_products():
#     with sync_playwright() as p:

#         setup_handler = setup_class(p)
#         browser, page = setup_handler.setup_browser()   

#         login_handler = log_in_class(page)
#         login_handler.correct_password_and_username()

#         product_handler = products_class(page)
#         product_handler.add_to_cart_main_page()
#         product_handler.remove_from_cart_main_page()
#         product_handler.view_and_use_product_page()
#         product_handler.change_order_products()

#         browser.close()

def test_payment():
    with sync_playwright() as p:

        setup_handler = setup_class(p)
        browser, page = setup_handler.setup_browser()   

        login_handler = log_in_class(page)
        login_handler.correct_password_and_username()

        product_handler = products_class(page)
        product_handler.add_to_cart_main_page()

        payment_handler = payment_class(page)
        payment_handler.go_to_basket()
        payment_handler.remove_from_basket()
        page.go_back()

        product_handler.add_to_cart_main_page()
        payment_handler.go_to_basket()
        payment_handler.go_to_checkout()

