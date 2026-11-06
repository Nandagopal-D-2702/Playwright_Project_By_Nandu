from playwright.sync_api import Page, expect

def test_navigate_and_title(page: Page):
    page.goto("https://www.saucedemo.com/")
    print("Page title:", page.title)
    print("Current URL:", page.url)
    assert page.title() == "Swag Labs"


def test_locators(page:Page):
    page.goto("https://www.saucedemo.com/")

    # By role (Best Practice - mimics how users/screen readers see the page)
    username_field = page.get_by_placeholder("Username")
    password_field = page.get_by_placeholder("Password")
    login_button = page.get_by_text("Login")

    # Fill and Click
    username_field.fill("standard_user")
    password_field.fill("secret_sauce")
    login_button.click()


def test_login_success(page:Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_text("Login").click()

    # expect() retries automatically until true or time out - great for async UI updates
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.get_by_text("Products")).to_be_visible()


# A test that adds an item to cart on saucedemo.com and verifies the cart badge shows "1"
def test_add_to_cart(page:Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_text("Login").click()

    page.get_by_text("Sauce Labs Backpack").click()
    page.get_by_role("button", name="Add to cart").click()

    # page.locator(".shopping_cart_badge")
    # expect(page.get_by_text("1")).to_be_visible()

    expect(page.locator(".shopping_cart_badge")).to_have_text("1")


# A test that logs in with a wrong password and verifies an error message appears (this teaches you negative-case testing, which QAOps interviews love asking about)
def test_login_wrong_password(page:Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_nandu")
    page.get_by_text("Login").click()

    expect(page.get_by_text("Epic sadface: Username and password do not match any user in this service")).to_be_visible()
    expect(page.get_by_role("alert")).to_be_visible()



