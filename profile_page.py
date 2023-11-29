from .base_page import BasePage
from .locators import ProfilePageLocators

class ProfilePage(BasePage):
    def go_to_logo(self):
        logo = self.browser.find_element(*ProfilePageLocators.LOGO)
        logo.click()
