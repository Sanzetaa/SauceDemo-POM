from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.valid_credential_login("standard_user", "secret_sauce")
    login_page.wait_for_inventory()
    assert "inventory" in driver.current_url

def test_inventory_page_loaded(driver):
    test_valid_login(driver)
    inventory = InventoryPage(driver)
    assert "inventory" in driver.current_url

def test_inventory_products_displayed(driver):
    test_valid_login(driver)
    inventory = InventoryPage(driver)
    assert len(inventory.get_all_products()) > 0

def test_add_backpack_to_cart(driver):
    test_valid_login(driver) 
    inventory = InventoryPage(driver)
    inventory.add_backpack()
    assert inventory.get_cart_badge() == "1"

def test_remove_backpack_from_cart(driver):
    test_valid_login(driver)
    inventory = InventoryPage(driver)
    inventory.add_backpack()
    inventory.remove_backpack()

def test_add_multiple_products(driver):
    test_valid_login(driver)
    inventory = InventoryPage(driver)
    inventory.add_backpack()
    inventory.add_bike_light()
    assert inventory.get_cart_badge() == "2"

def test_open_cart(driver):
    test_valid_login(driver)
    inventory = InventoryPage(driver)
    inventory.open_cart()
    assert "cart" in driver.current_url

def test_sort_name_a_to_z(driver):
    test_valid_login(driver)
    inventory = InventoryPage(driver)
    inventory.sort_products("Name (A to Z)")
    assert "inventory" in driver.current_url


def test_sort_name_z_to_a(driver):
    test_valid_login(driver)
    inventory = InventoryPage(driver)
    inventory.sort_products("Name (Z to A)")
    assert "inventory" in driver.current_url

def test_sort_price_low_to_high(driver):
    test_valid_login(driver)
    inventory = InventoryPage(driver)
    inventory.sort_products("Price (low to high)")
    assert "inventory" in driver.current_url


def test_sort_price_high_to_low(driver):
    test_valid_login(driver)
    inventory = InventoryPage(driver)
    inventory.sort_products("Price (high to low)")
    assert "inventory" in driver.current_url

def test_open_first_product(driver):
    test_valid_login(driver)
    inventory = InventoryPage(driver)
    inventory.click_first_product()
    assert "inventory-item" in driver.current_url

def test_twitter_footer_link(driver):
    test_valid_login(driver)
    inventory = InventoryPage(driver)
    original_window = driver.current_window_handle
    inventory.click_twitter_link()
    driver.switch_to.window(driver.window_handles[1])
    assert "x.com" in driver.current_url
    driver.close()
    driver.switch_to.window(original_window)

def test_facebook_footer_link(driver):
    test_valid_login(driver)
    inventory = InventoryPage(driver)
    original_window = driver.current_window_handle
    inventory.click_facebook_link()
    driver.switch_to.window(driver.window_handles[1])
    assert "facebook.com" in driver.current_url
    driver.close()
    driver.switch_to.window(original_window)

def test_linkedin_footer_link(driver):
    test_valid_login(driver)
    inventory = InventoryPage(driver)
    original_window = driver.current_window_handle
    inventory.click_linkedin_link()
    driver.switch_to.window(driver.window_handles[1])
    assert "linkedin.com" in driver.current_url
    driver.close()
    driver.switch_to.window(original_window)

def test_logout(driver):
    test_valid_login(driver)
    inventory = InventoryPage(driver)
    inventory.logout()
    assert "saucedemo" in driver.current_url