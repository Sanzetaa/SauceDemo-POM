from pages.login_page import LoginPage


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.valid_credential_login("standard_user", "secret_sauce")
    login_page.wait_for_inventory()
    assert "inventory" in driver.current_url

def test_wrong_crendential_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.wrong_credential_login("sanjita", "adhikari")
    assert "inventory" not in  driver.current_url

def test_blank_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.blank_credential_login("", "")
    assert "inventory" not in driver.current_url

def test_uppercase_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.uppercase_credential_login("STANDARD_USER", "SECRET_SAUCE")
    assert "inventory" not in driver.current_url

def test_maximum_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.maximum_credential_login("standarduserisniceusertobenoticedinthispage", "secret_sauceing_bbhikeintheriver")
    assert "inventory" not in driver.current_url

def test_invalid_username_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.invalid_username_login("abc@#$", "secret_sauce")
    assert "inventory" not in driver.current_url

def test_invalid_password_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.invalid_password_login("standard_user", "12345")
    assert "inventory" not in driver.current_url


def test_login_using_enter(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login_using_enter("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url

