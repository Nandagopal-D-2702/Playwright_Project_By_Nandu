from pages.login_page import LoginPage
from pages.inventory_page import InvertoryPage

def test_add_to_cart(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InvertoryPage(page)
    inventory_page.add_item_to_cart("Sauce Labs Backpack")
    inventory_page.expect_cart_count("1")
