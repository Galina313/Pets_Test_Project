import pytest
from .pages.main_page import MainPage
import time

@pytest.mark.smoke
def test_go_to_login_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    time.sleep(5)
    browser.save_screenshot('result2.png')

@pytest.mark.smoke
@pytest.mark.win10
def test_go_to_next_main_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_next_main_page()
    time.sleep(5)
    browser.save_screenshot('result3.png')

@pytest.mark.regression
def test_go_to_last_main_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_last_main_page()
    time.sleep(5)
    browser.save_screenshot('result4.png')

def test_go_to_type_filter_pet(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_type_filter()
    page.go_to_type_filter_cat()
    time.sleep(5)
    browser.save_screenshot('result5.png')

def test_go_to_type_filter_pet_name(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_type_filter_pet_name()
    time.sleep(5)
    browser.save_screenshot('result6.png')

def test_go_to_details_of_pet(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_type_filter_pet_name()
    page.go_to_details_of_pet()
    time.sleep(5)
    browser.save_screenshot('result7.png')

def test_go_to_logout_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_logout_page()
    time.sleep(10)
    browser.save_screenshot('result8.png')