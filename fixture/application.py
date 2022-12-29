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

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")

    def return_to_home_page(self):
        self.driver.find_element(By.LINK_TEXT, "home").click()

    def destroy(self):
        self.driver.quit()
