from playwright.sync_api import Page, expect

class LoginPage:

    URL = "https://www.saucedemo.com/"

    def __init__(self, page:Page):
        self.page = page
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_text("Login")
        self.error_message = page.get_by_text("Epic sadface: Username and password do not match any user in this service")

    def goto(self):
        self.page.goto(self.URL)

    def login(self, username:str, password:str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def expect_login_error_visible(self):
        expect(self.error_message).to_be_visible()


