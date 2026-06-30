from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutCompletePage

def complete_checkout(driver):

    login_page = LoginPage(driver)
    login_page.load()
    login_page.valid_credential_login("standard_user", "secret_sauce")
    login_page.wait_for_inventory()

    inventory = InventoryPage(driver)
    inventory.add_backpack()
    inventory.open_cart()

    cart = CartPage(driver)
    cart.checkout()

    checkout_step_one = CheckoutStepOnePage(driver)
    checkout_step_one.checkout("Sanjita", "Adhikari", "44600")
    checkout_step_two = CheckoutStepTwoPage(driver)
    checkout_step_two.click_finish()

def test_checkout_complete_page_loaded(driver):
    complete_checkout(driver)
    complete = CheckoutCompletePage(driver)
    complete.wait_for_checkout_complete_page()
    assert "checkout-complete" in driver.current_url


def test_complete_header(driver):
    complete_checkout(driver)
    complete = CheckoutCompletePage(driver)
    assert complete.get_complete_header() == "Thank you for your order!"


def test_complete_message(driver):
    complete_checkout(driver)
    complete = CheckoutCompletePage(driver)
    assert complete.get_complete_text() == "Your order has been dispatched, and will arrive just as fast as the pony can get there!"


def test_pony_express_image(driver):
    complete_checkout(driver)
    complete = CheckoutCompletePage(driver)
    assert complete.is_pony_express_displayed()


def test_back_home_button(driver):
    complete_checkout(driver)
    complete = CheckoutCompletePage(driver)
    complete.click_back_home()
    assert "inventory" in driver.current_url