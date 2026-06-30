from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage


def go_to_checkout(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.valid_credential_login("standard_user", "secret_sauce")
    login_page.wait_for_inventory()

    inventory = InventoryPage(driver)
    inventory.add_backpack()
    inventory.open_cart()

    cart = CartPage(driver)
    cart.checkout()


def test_checkout_page_loaded(driver):
    go_to_checkout(driver)
    checkout = CheckoutStepOnePage(driver)
    checkout.wait_for_checkout_page()
    assert "checkout-step-one" in driver.current_url


def test_valid_checkout_information(driver):
    go_to_checkout(driver)
    checkout = CheckoutStepOnePage(driver)
    checkout.checkout("Sanjita", "Adhikari", "44600")
    assert "checkout-step-two" in driver.current_url


def test_blank_first_name(driver):
    go_to_checkout(driver)
    checkout = CheckoutStepOnePage(driver)
    checkout.checkout("", "Adhikari", "44600")
    assert "checkout-step-two" not  in  driver.current_url


def test_blank_last_name(driver):
    go_to_checkout(driver)
    checkout = CheckoutStepOnePage(driver)
    checkout.checkout("Sanjita", "", "44600")
    assert "checkout-step-two" not in driver.current_url


def test_blank_postal_code(driver):
    go_to_checkout(driver)
    checkout = CheckoutStepOnePage(driver)
    checkout.checkout("Sanjita", "Adhikari", "")
    assert "checkout-step-two"  not in driver.current_url


def test_blank_checkout_information(driver):
    go_to_checkout(driver)
    checkout = CheckoutStepOnePage(driver)
    checkout.checkout("", "", "")
    assert "checkout-step-two" not in driver.current_url

def test_invalid_postal_code(driver):
    go_to_checkout(driver)
    checkout = CheckoutStepOnePage(driver)
    checkout.checkout("Sanjta", "Adhikari", "12A!@#$%")
    assert "checkout-step-two" not in driver.current_url

def test_uppercase_alphabetical_postal_code(driver):
    go_to_checkout(driver)
    checkout = CheckoutStepOnePage(driver)
    checkout.checkout("Sanjta", "Adhikari", "SSDCVBB")
    assert "checkout-step-two" not in driver.current_url

def test_cancel_checkout(driver):
    go_to_checkout(driver)
    checkout = CheckoutStepOnePage(driver)
    checkout.click_cancel()
    assert "cart" in driver.current_url

def test_continue_button(driver):
    go_to_checkout(driver)
    checkout = CheckoutStepOnePage(driver)
    checkout.checkout("Sanjita", "Adhikari", "44600")
    assert "checkout-step-two" in driver.current_url
