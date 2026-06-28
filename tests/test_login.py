from pages.login_page import LoginPage


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.valid_credential_login("standard_user", "secret_sauce")
    login_page.wait_for_inventory()
    assert "inventory" in driver.current_url

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.wrong_credential_login("sanjita", "adhikari")
    assert "inventory" not in  driver.current_url

