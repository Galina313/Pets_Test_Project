from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.keys import Keys

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_next_main_page(self):
        next_main_page = self.browser.find_element(*MainPageLocators.NEXT_MAIN_PAGE)
        next_main_page.click()

    def go_to_last_main_page(self):
        last_main_page = self.browser.find_element(*MainPageLocators.LAST_MAIN_PAGE)
        last_main_page.click()
    def go_to_type_filter(self):
        type_filter = self.browser.find_element(*MainPageLocators.TYPE_FILTER)
        type_filter.click()

    def go_to_type_filter_cat(self):
        type_filter_cat = self.browser.find_element(*MainPageLocators.TYPE_FILTER_PET)
        type_filter_cat.click()

    def go_to_type_filter_pet_name(self):
        type_filter_pet_name = self.browser.find_element(*MainPageLocators.TYPE_FILTER_PET_NAME)
        type_filter_pet_name.send_keys('Atos')
        type_filter_pet_name.send_keys(Keys.RETURN)

    def go_to_details_of_pet(self):
        details_of_pet = self.browser.find_element(*MainPageLocators.DETAILS_OF_PET)
        details_of_pet.click()

    def go_to_logout_page(self):
        logout_page = self.browser.find_element(*MainPageLocators.LOGOUT_PAGE)
        logout_page.click()