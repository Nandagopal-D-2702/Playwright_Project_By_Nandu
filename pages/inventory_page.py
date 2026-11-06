from playwright.sync_api import Page, expect

class InvertoryPage:
    def __init__(self, page:Page):
        self.page = page
        self.cart_badge = page.locator(".shopping_cart_badge")

    def add_item_to_cart(self, item_name: str):
        product_card = self.page.locator(".inventory_item", has_text=item_name)
        product_card.get_by_role("button", name="Add to cart").click()

    def expect_cart_count(self, count:str):
        expect(self.cart_badge).to_have_text(count)