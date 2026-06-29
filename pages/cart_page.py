from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CartPage(BasePage):
    URL = "https://www.saucedemo.com/cart.html"

    #Locators

    CART_LIST = (By.CLASS_NAME, "cart_list")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
    REMOVE_BIKE_LIGHT = (By.ID, "remove-sauce-labs-bike-light")

    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ITEM_QUANTITY = (By.CLASS_NAME, "cart_quantity")

    def load(self):
        self.open(self.URL)
        self._wait_for_page_ready()

    def wait_for_cart_page(self):
        self.find_visible(self.CART_LIST)

    def get_all_cart_items(self):
        return self.find_all_visible(self.CART_ITEMS)
    
    def is_cart_empty(self):
        return len(self.driver.find_elements(*self.CART_ITEMS)) == 0

    def get_item_name(self):
        return self.find_visible(self.ITEM_NAME).text

    def get_item_price(self):
        return self.find_visible(self.ITEM_PRICE).text
    
    def get_item_quantity(self):
        return self.find_visible(self.ITEM_QUANTITY).text

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BUTTON)

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def remove_backpack(self):
        self.click(self.REMOVE_BACKPACK)

    def remove_bike_light(self):
        self.click(self.REMOVE_BIKE_LIGHT)

    




