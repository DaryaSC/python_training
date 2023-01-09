from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class CantactHelper:

    def __init__(self, app):
        self.app = app

    def create_contact(self, contact):
        self.open_contact_page()
        self.app.driver.find_element(By.NAME, "firstname").click()
        self.app.driver.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        self.app.driver.find_element(By.NAME, "middlename").click()
        self.app.driver.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        self.app.driver.find_element(By.NAME, "lastname").click()
        self.app.driver.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        self.app.driver.find_element(By.NAME, "nickname").click()
        self.app.driver.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        self.app.driver.find_element(By.NAME, "title").click()
        self.app.driver.find_element(By.NAME, "title").send_keys(contact.title)
        self.app.driver.find_element(By.NAME, "company").click()
        self.app.driver.find_element(By.NAME, "company").send_keys(contact.company)
        self.app.driver.find_element(By.NAME, "address").click()
        self.app.driver.find_element(By.NAME, "address").send_keys(contact.address)
        self.app.driver.find_element(By.NAME, "home").click()
        self.app.driver.find_element(By.NAME, "home").send_keys(contact.home)
        self.app.driver.find_element(By.NAME, "mobile").click()
        self.app.driver.find_element(By.NAME, "mobile").send_keys(contact.mobile)
        self.app.driver.find_element(By.NAME, "work").click()
        self.app.driver.find_element(By.NAME, "work").send_keys(contact.work)
        self.app.driver.find_element(By.NAME, "fax").click()
        self.app.driver.find_element(By.NAME, "fax").send_keys(contact.fax)
        self.app.driver.find_element(By.NAME, "email").click()
        self.app.driver.find_element(By.NAME, "email").send_keys(contact.email)
        self.app.driver.find_element(By.NAME, "email2").click()
        self.app.driver.find_element(By.NAME, "email2").send_keys(contact.email2)
        self.app.driver.find_element(By.NAME, "email3").click()
        self.app.driver.find_element(By.NAME, "email3").send_keys(contact.email3)
        self.app.driver.find_element(By.NAME, "homepage").click()
        element = self.app.driver.find_element(By.NAME, "homepage")
        actions = ActionChains(self.app.driver)
        actions.double_click(element).perform()
        self.app.driver.find_element(By.NAME, "homepage").send_keys(contact.homepage)
        self.app.driver.find_element(By.NAME, "bday").click()
        dropdown = self.app.driver.find_element(By.NAME, "bday")
        dropdown.find_element(By.XPATH, "//option[. = '16']").click()
        self.app.driver.find_element(By.CSS_SELECTOR, "select:nth-child(61) > option:nth-child(18)").click()
        self.app.driver.find_element(By.NAME, "bmonth").click()
        dropdown = self.app.driver.find_element(By.NAME, "bmonth")
        dropdown.find_element(By.XPATH, "//option[. = 'January']").click()
        self.app.driver.find_element(By.CSS_SELECTOR, "select:nth-child(62) > option:nth-child(2)").click()
        self.app.driver.find_element(By.NAME, "byear").click()
        self.app.driver.find_element(By.NAME, "byear").send_keys("6464")
        self.app.driver.find_element(By.NAME, "aday").click()
        dropdown = self.app.driver.find_element(By.NAME, "aday")
        dropdown.find_element(By.XPATH, "//option[. = '18']").click()
        self.app.driver.find_element(By.CSS_SELECTOR, "select:nth-child(66) > option:nth-child(20)").click()
        self.app.driver.find_element(By.NAME, "amonth").click()
        dropdown = self.app.driver.find_element(By.NAME, "amonth")
        dropdown.find_element(By.XPATH, "//option[. = 'January']").click()
        self.app.driver.find_element(By.CSS_SELECTOR, "select:nth-child(67) > option:nth-child(2)").click()
        self.app.driver.find_element(By.NAME, "ayear").click()
        self.app.driver.find_element(By.NAME, "ayear").send_keys("5444")
        self.app.driver.find_element(By.CSS_SELECTOR, "select:nth-child(71) > option:nth-child(6)").click()
        self.app.driver.find_element(By.NAME, "address2").click()
        self.app.driver.find_element(By.NAME, "address2").send_keys(contact.address2)
        self.app.driver.find_element(By.NAME, "phone2").click()
        self.app.driver.find_element(By.NAME, "phone2").send_keys(contact.phone2)
        self.app.driver.find_element(By.NAME, "notes").click()
        self.app.driver.find_element(By.NAME, "notes").send_keys(contact.notes)
        self.app.driver.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()
        self.app.return_to_home_page()

    def open_contact_page(self):
        self.app.driver.find_element(By.LINK_TEXT, "add new").click()

    def delete_first_contact(self):
        self.app.return_to_home_page()
        # select first group
        self.app.driver.find_element(By.NAME, "selected[]").click()
        self.app.driver.find_element(By.XPATH, "//input[@value='Delete']").click()
        self.app.driver.switch_to.alert.accept()
        self.app.return_to_home_page()

    def edit_first_contact(self, text):
        self.app.return_to_home_page()
        # select first group
        self.app.driver.find_element(By.XPATH, "//img[@alt='Edit']").click()
        self.app.driver.find_element(By.NAME, "firstname").clear()
        self.app.driver.find_element(By.NAME, "firstname").send_keys(text)
        self.app.driver.find_element(By.NAME, "update").click()
        self.app.return_to_home_page()
