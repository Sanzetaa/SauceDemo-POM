from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage

def go_to_checkout_overview(driver):

    login_page = LoginPage(driver)
    login_page.load()
    login_page.valid_credential_login("standard_user", "secret_sauce")
    login_page.wait_for_inventory()

    inventory = InventoryPage(driver)
    inventory.add_backpack()
    inventory.open_cart()

    cart = CartPage(driver)
    cart.checkout()

    checkout = CheckoutStepOnePage(driver)
    checkout.checkout("Sanjita", "Adhikari", "44600")

def test_checkout_overview_page_loaded(driver):
    go_to_checkout_overview(driver)
    overview = CheckoutStepTwoPage(driver)
    overview.wait_for_checkout_step_two_page()
    assert "checkout-step-two" in driver.current_url

def test_product_displayed(driver):
    go_to_checkout_overview(driver)
    overview = CheckoutStepTwoPage(driver)
    assert len(overview.get_all_products()) == 1

def test_product_name(driver):
    go_to_checkout_overview(driver)
    overview = CheckoutStepTwoPage(driver)
    assert overview.get_product_name() == "Sauce Labs Backpack"

def test_product_price(driver):
    go_to_checkout_overview(driver)
    overview = CheckoutStepTwoPage(driver)
    assert overview.get_product_price() == "$29.99"

def test_payment_information(driver):
    go_to_checkout_overview(driver)
    overview = CheckoutStepTwoPage(driver)
    assert overview.get_payment_information() == "SauceCard #31337"

def test_shipping_information(driver):

    go_to_checkout_overview(driver)

    overview = CheckoutStepTwoPage(driver)

    assert overview.get_shipping_information() == "Free Pony Express Delivery!"

def test_item_total(driver):

    go_to_checkout_overview(driver)

    overview = CheckoutStepTwoPage(driver)

    assert "Item total:" in overview.get_item_total()

def test_tax(driver):

    go_to_checkout_overview(driver)

    overview = CheckoutStepTwoPage(driver)

    assert "Tax:" in overview.get_tax()


def test_total(driver):

    go_to_checkout_overview(driver)

    overview = CheckoutStepTwoPage(driver)

    assert "Total:" in overview.get_total()

def test_finish_checkout(driver):

    go_to_checkout_overview(driver)

    overview = CheckoutStepTwoPage(driver)

    overview.click_finish()

    assert "checkout-complete" in driver.current_url


def test_cancel_checkout(driver):

    go_to_checkout_overview(driver)

    overview = CheckoutStepTwoPage(driver)

    overview.click_cancel()

    assert "inventory" in driver.current_url
