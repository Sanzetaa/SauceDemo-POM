from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutStepOnePage(BasePage):
    URL = "https://www.saucedemo.com/checkout-step-one.html"

    # Locators
    CHECKOUT_CONTAINER = (By.ID, "checkout_info_container")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def wait_for_checkout_page(self):
        self.find_visible(self.CHECKOUT_CONTAINER)

    def enter_first_name(self, first_name):
        self.type(self.FIRST_NAME_INPUT, first_name)

    def enter_last_name(self, last_name):
        self.type(self.LAST_NAME_INPUT, last_name)

    def enter_postal_code(self, postal_code):
        self.type(self.POSTAL_CODE_INPUT, postal_code)

    def fill_checkout_information(self, first_name, last_name, postal_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def click_cancel(self):
        self.click(self.CANCEL_BUTTON)

    def checkout(self, first_name, last_name, postal_code):
        self.fill_checkout_information(first_name, last_name, postal_code)
        self.click_continue()

    def get_error_message(self):
        return self.find_visible(self.ERROR_MESSAGE).text
    

