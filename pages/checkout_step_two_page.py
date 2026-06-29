from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CheckoutStepTwoPage(BasePage):
    URL = "https://www.saucedemo.com/checkout-step-two.html"

    CHECKOUT_OVERVIEW = (By.ID, "checkout_summary_container")

    PAYMENT_INFORMATION = (By.CSS_SELECTOR, "[data-test='payment-info-value']")
    SHIPPING_INFORMATION = (By.CSS_SELECTOR, "[data-test='shipping-info-value']")
    ITEM_TOTAL = (By.CSS_SELECTOR, "[data-test='subtotal-label']")
    TAX = (By.CSS_SELECTOR, "[data-test='tax-label']")
    TOTAL = (By.CSS_SELECTOR, "[data-test='total-label']")

    FINISH_BUTTON = (By.ID, "finish")
    CANCEL_BUTTON = (By.ID, "cancel")

    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")

    def load(self):
        self.open(self.URL)
        self._wait_for_page_ready()

    def wait_for_checkout_step_two_page(self, timeout=10):
        self.find_visible(self.CHECKOUT_OVERVIEW, timeout)

    def get_payment_information(self, timeout=10):
        return self.find_visible(self.PAYMENT_INFORMATION, timeout).text
    
    def get_shipping_information(self, timeout=10):
        return self.find_visible(self.SHIPPING_INFORMATION, timeout).text
    
    def get_item_total(self):
        return self.find_visible(self.ITEM_TOTAL).text
    
    def get_tax(self):
        return self.find_visible(self.TAX).text
    
    def get_total(self):
        return self.find_visible(self.TOTAL).text
    
    def get_all_products(self):
        return self.find_all_visible(self.CART_ITEMS)
    
    def get_product_name(self):
        return self.find_visible(self.ITEM_NAME).text
    
    def get_product_price(self):
        return self.find_visible(self.ITEM_PRICE).text
    
    def click_finish(self):
        self.click(self.FINISH_BUTTON)

    def click_cancel(self):
        self.click(self.CANCEL_BUTTON)
        




