import pytest
import time
from pages.profile_page import ProfilePage

@pytest.mark.skip
def test_go_to_logo(browser):
    test_go_to_login(browser):
    link = 'http://34.141.58.52:8080/#/profile'
    page.open()
    page.go_to_login()
    page.go_to_password()
    page.submit_login_button()
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_logo()
    time.sleep(5)
    browser.save_screenshot('result9.png')