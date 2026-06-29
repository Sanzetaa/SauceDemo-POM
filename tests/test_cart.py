from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.valid_credential_login("standard_user", "secret_sauce")
    login_page.wait_for_inventory()
    assert "inventory" in driver.current_url

def add_backpack_to_cart(driver):
    test_valid_login(driver)
    inventory = InventoryPage(driver)
    inventory.add_backpack()
    inventory.open_cart()

def test_cart_page_loaded(driver):
    add_backpack_to_cart(driver)
    cart = CartPage(driver)
    cart.wait_for_cart_page()
    assert "cart" in driver.current_url

def test_cart_contains_product(driver):
    add_backpack_to_cart(driver)
    cart = CartPage(driver)
    assert len(cart.get_all_cart_items()) == 1

def test_remove_product(driver):
    add_backpack_to_cart(driver)
    cart = CartPage(driver)
    cart.remove_backpack()
    assert cart.is_cart_empty()

def test_continue_shopping(driver):
    add_backpack_to_cart(driver)
    cart = CartPage(driver)
    cart.continue_shopping()
    assert "inventory" in driver.current_url


def test_checkout_button(driver):
    add_backpack_to_cart(driver)
    cart = CartPage(driver)
    cart.checkout()
    assert "checkout-step-one" in driver.current_url

