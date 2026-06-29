from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CheckoutCompletePage(BasePage):
    URL = "https://www.saucedemo.com/checkout-complete.html"


    CHECKOUT_COMPLETE_CONTAINER = (By.ID, "checkout_complete_container")

    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    COMPLETE_TEXT = (By.CLASS_NAME, "complete-text")

    BACK_HOME_BUTTON = (By.ID, "back-to-products")

    PONY_EXPRESS_IMAGE = (By.CLASS_NAME, "pony_express")

    def load(self):
        self.open(self.URL)
        self._wait_for_page_ready()

    def wait_for_checkout_complete_page(self, timeout=10):
        self.find_visible(self.CHECKOUT_COMPLETE_CONTAINER, timeout)

    def get_complete_header(self):
        return self.find_visible(self.COMPLETE_HEADER).text

    def get_complete_text(self):
        return self.find_visible(self.COMPLETE_TEXT).text

    def click_back_home(self):
        self.click(self.BACK_HOME_BUTTON)

    def is_pony_express_displayed(self):
        return self.find_visible(self.PONY_EXPRESS_IMAGE).is_displayed()