from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class InventoryPage(BasePage):
    URL = "https://www.saucedemo.com/inventory.html"

    #locators 
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    APP_LOGO = (By.CLASS_NAME, "app_logo")

    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    CLOSE_MENU_BUTTON = (By.ID, "react-burger-cross-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    ABOUT_LINK = (By.ID, "about_sidebar_link")
    RESET_APP_STATE = (By.ID, "reset_sidebar_link")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
    ADD_TO_CART_BIKE_LIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")
    REMOVE_BIKE_LIGHT = (By.ID, "remove-sauce-labs-bike-light")
    FIRST_PRODUCT = (By.CLASS_NAME, "inventory_item_name")
    TWITTER_LINK = (By.CSS_SELECTOR, "a[data-test='social-twitter']")
    FACEBOOK_LINK = (By.CSS_SELECTOR, "a[data-test='social-facebook']")
    LINKEDIN_LINK = (By.CSS_SELECTOR, "a[data-test='social-linkedin']")
    


    def load(self):
        self.open(self.URL)
        self._wait_for_page_ready()

    def wait_for_inventory_page(self):
        self.find_visible(self.INVENTORY_CONTAINER)

    def get_page_title(self):
        return self.find_visible(self.APP_LOGO).text

    def get_all_products(self):
        return self.find_all_visible(self.INVENTORY_ITEMS)

    def open_menu(self):
        self.click(self.MENU_BUTTON)

    def close_menu(self):
        self.click(self.CLOSE_MENU_BUTTON)


    def click_about(self):
        self.open_menu()
        self.click(self.ABOUT_LINK)

    def reset_app_state(self):
        self.open_menu()
        self.click(self.RESET_APP_STATE)

    def open_cart(self):
        self.click(self.CART_ICON)

    def add_backpack(self):
        self.click(self.ADD_TO_CART_BACKPACK)

    def remove_backpack(self):
        self.click(self.REMOVE_BACKPACK)

    def add_bike_light(self):
        self.click(self.ADD_TO_CART_BIKE_LIGHT)

    def remove_bike_light(self):
        self.click(self.REMOVE_BIKE_LIGHT)

    def get_cart_badge(self):
        return self.find_visible(self.CART_BADGE).text

    def click_first_product(self):
        self.click(self.FIRST_PRODUCT)

    def sort_products(self, option):
        dropdown = Select(self.find(self.SORT_DROPDOWN))
        dropdown.select_by_visible_text(option)

    
    def click_twitter_link(self):
        self.click(self.TWITTER_LINK)

    def click_facebook_link(self):
        self.click(self.FACEBOOK_LINK)

    def click_linkedin_link(self):
        self.click(self.LINKEDIN_LINK)

    def logout(self):
        self.open_menu()
        self.click(self.LOGOUT_LINK)
