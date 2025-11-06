# ════════════════════════ SETTINGS ════════════════════════
from playwright.sync_api import sync_playwright

# ════════════════════════ VARIABLES ════════════════════════
incorrect_username_variable = "wrong_user"
incorrect_password_variable = "wrong_password"
correct_username_variable = "standard_user"
correct_password_variable = "secret_sauce"

# ════════════════════════ KEYWORDS ════════════════════════
class log_in_class():
    def __init__(self, page):
        self.page = page
    
    def incorrect_password(self):
        self.page.fill("[id='password']", (incorrect_password_variable)) 
        self.page.click("[id='login-button']") 
        assert "Epic sadface: Username is required" in self.page.content()

    def incorrect_username(self):
        self.page.fill("[id='password']", ("")) 
        self.page.fill("[id='user-name']", (incorrect_username_variable)) 
        self.page.click("[id='login-button']") 
        assert "Epic sadface: Password is required" in self.page.content()

    def incorrect_password_and_username(self):
        self.page.fill("[id='user-name']", (incorrect_username_variable)) 
        self.page.fill("[id='password']", (incorrect_password_variable)) 
        self.page.click("[id='login-button']") 
        assert "Epic sadface: Username and password do not match any user in this service" in self.page.content()

    def correct_password_and_username(self):
        self.page.fill("[id='user-name']", (correct_username_variable)) 
        self.page.fill("[id='password']", (correct_password_variable)) 
        self.page.click("[id='login-button']") 
