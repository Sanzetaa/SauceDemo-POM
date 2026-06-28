from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    # Locators only — no driver logic here
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON   = (By.ID, "login-button")
    ERROR_MESSAGE  = (By.CSS_SELECTOR, "h3[data-test='error']")

    def load(self):
        self.open(self.URL)
        self._wait_for_page_ready()

    def _wait_for_page_ready(self, timeout=10):
        self.find_visible(self.USERNAME_INPUT, timeout)
        self.find_visible(self.LOGIN_BUTTON, timeout)

    def valid_credential_login(self, username, password):
        self._wait_for_page_ready()
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def wrong_credential_login(self, username, password):
        self._wait_for_page_ready()
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def blank_credential_login(self, username, password):
        self._wait_for_page_ready()
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def uppercase_credential_login(self, username, password):
        self._wait_for_page_ready()
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON) 

    def maximum_credential_login(self, username, password):
        self._wait_for_page_ready()
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON) 

    def login_using_enter(self, username, password):
        self._wait_for_page_ready()
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.press_enter(self.PASSWORD_INPUT) 

    def wait_for_inventory(self, timeout=10):
        self.wait_for_url_contains("inventory", timeout)

    def get_error_message(self):
        return self.find_visible(self.ERROR_MESSAGE).text