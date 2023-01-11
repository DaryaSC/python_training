from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from model.contact import Contact


class CantactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        self.open_contact_page()
        self.fill_contact_form(contact)
        self.app.driver.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        if text is not None:
            self.app.driver.find_element(By.NAME, field_name).click()
            self.app.driver.find_element(By.NAME, field_name).clear()
            self.app.driver.find_element(By.NAME, field_name).send_keys(text)

    def open_contact_page(self):
        if not self.app.driver.current_url.endswith("/edit.php"):
            self.app.driver.find_element(By.LINK_TEXT, "add new").click()

    def delete_contact_by_index(self, index):
        self.app.return_to_home_page()
        # select first group
        self.app.driver.find_elements(By.NAME, "selected[]")[index].click()
        self.app.driver.find_element(By.XPATH, "//input[@value='Delete']").click()
        self.app.driver.switch_to.alert.accept()
        self.app.return_to_home_page()
        self.contact_cache = None

    def edit_contact_by_index(self, contact, index):
        self.app.return_to_home_page()
        self.app.driver.find_elements(By.XPATH, "//img[@alt='Edit']")[index].click()
        self.fill_contact_form(contact)
        self.app.driver.find_element(By.NAME, "update").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def count(self):
        self.app.return_to_home_page()
        return len(self.app.driver.find_elements(By.NAME, "selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            self.app.return_to_home_page()
            self.contact_cache = []
            for element in self.app.driver.find_elements(By.NAME, "entry"):
                lastname = element.find_element(By.XPATH, "td[2]").text
                firstname = element.find_element(By.XPATH, "td[3]").text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                self.contact_cache.append(Contact(id=id, lastname=lastname, firstname=firstname))
        return list(self.contact_cache)
