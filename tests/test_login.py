from pages.login_page import LoginPage
from playwright.sync_api import expect

def test_login_success(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_login_wrong_password(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_nandu")
    login_page.expect_login_error_visible()

