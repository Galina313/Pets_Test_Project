from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')
    NEXT_MAIN_PAGE = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[3]/span[1]/button[2]')
    LAST_MAIN_PAGE = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[3]/button[4]')
    TYPE_FILTER = (By.ID, 'typesSelector')
    TYPE_FILTER_PET = (By.ID, 'pv_id_2_1')
    TYPE_FILTER_PET_NAME = (By.ID, 'petName')
    DETAILS_OF_PET = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/button[1]')
    LOGOUT_PAGE = (By.XPATH, '//*[@id="app"]/header[1]/div[1]/ul[1]/li[1]/a[1]/span[1]')

class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, 'login')
    LOGIN_PASSWORD = (By.XPATH, '//*[@id="password"]/input')
    LOGIN_BTN = (By.XPATH, '//*[@id="pv_id_2_content"]/div/form/div[3]/button/span[2]')
    PROFILE = (By.XPATH, '//*[@id="app"]/header/div')

class ProfilePageLocators:
    LOGO = (By.XPATH, '//*[@id="app"]/header[1]/div[1]/ul[1]/li[1]/a[1]')




