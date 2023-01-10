from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import CantactHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.vars = {}
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
            self.driver.get("http://localhost/addressbook/")

    def return_to_home_page(self):
        if not len(self.driver.find_elements(By.NAME, "searchstring")) > 0:
            self.driver.find_element(By.LINK_TEXT, "home").click()

    def destroy(self):
        self.driver.quit()
