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
        self.app.driver.find_elements(By.NAME, "selected[]")[index].click()
        self.app.driver.find_element(By.XPATH, "//input[@value='Delete']").click()
        self.app.driver.switch_to.alert.accept()
        self.app.return_to_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        self.app.return_to_home_page()
        self.app.driver.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()
        self.app.driver.find_element(By.XPATH, "//input[@value='Delete']").click()
        self.app.driver.switch_to.alert.accept()
        self.app.return_to_home_page()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        self.app.return_to_home_page()
        self.app.driver.find_elements(By.XPATH, "//img[@alt='Edit']")[index].click()

    def open_contact_to_edit_by_id(self, id):
        self.app.return_to_home_page()
        self.app.driver.find_element(By.CSS_SELECTOR, f"a[href='edit.php?id={id}']").click()

    def edit_contact_by_index(self, contact, index):
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(contact)
        self.app.driver.find_element(By.NAME, "update").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def edit_contact_by_id(self, contact, id):
        self.open_contact_to_edit_by_id(id)
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
                address = element.find_element(By.XPATH, "td[4]").text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                all_phones = element.find_element(By.XPATH, "td[6]").text
                all_emails = element.find_element(By.XPATH, "td[5]").text
                self.contact_cache.append(Contact(id=id, lastname=lastname, firstname=firstname, address=address,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        self.open_contact_to_edit_by_index(index)
        id = self.app.driver.find_element(By.NAME, "id").get_attribute("value")
        lastname = self.app.driver.find_element(By.NAME, "lastname").get_attribute("value")
        firstname = self.app.driver.find_element(By.NAME, "firstname").get_attribute("value")
        address = self.app.driver.find_element(By.NAME, "address").get_attribute("value")
        email = self.app.driver.find_element(By.NAME, "email").get_attribute("value")
        email2 = self.app.driver.find_element(By.NAME, "email2").get_attribute("value")
        email3 = self.app.driver.find_element(By.NAME, "email3").get_attribute("value")
        home = self.app.driver.find_element(By.NAME, "home").get_attribute("value")
        mobile = self.app.driver.find_element(By.NAME, "mobile").get_attribute("value")
        work = self.app.driver.find_element(By.NAME, "work").get_attribute("value")
        phone2 = self.app.driver.find_element(By.NAME, "phone2").get_attribute("value")
        return Contact(id=id, lastname=lastname, firstname=firstname, address=address, email=email, email2=email2,
                       email3=email3, home=home, mobile=mobile, work=work, phone2=phone2)

    def add_contact_in_group(self, contact_id, group_id):
        self.app.return_to_home_page()
        self.app.driver.find_element(By.NAME, "to_group").click()
        self.app.driver.find_element(By.XPATH, "(//option[@value='%s'])[2]" % group_id).click()
        self.app.driver.find_element(By.CSS_SELECTOR, "input[value='%s']" % contact_id).click()
        self.app.driver.find_element(By.NAME, "add").click()
        self.app.return_to_home_page()

    def del_contact_from_group(self, contact_id, group_id):
        self.app.return_to_home_page()
        self.app.driver.find_element(By.NAME, "group").click()
        self.app.driver.find_element(By.XPATH, "//option[@value='%s']" % group_id).click()
        self.app.driver.find_element(By.CSS_SELECTOR, "input[value='%s']" % contact_id).click()
        self.app.driver.find_element(By.NAME, "remove").click()
        self.app.return_to_home_page()
