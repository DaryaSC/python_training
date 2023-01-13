from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import CantactHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "edge":
            self.driver = webdriver.Edge()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.base_url = base_url
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = CantactHelper(self)

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def open_home_page(self):
        if not len(self.driver.find_elements(By.NAME, "searchstring")) > 0:
            self.driver.get(self.base_url)

    def return_to_home_page(self):
        self.driver.find_element(By.LINK_TEXT, "home").click()

    def destroy(self):
        self.driver.quit()
