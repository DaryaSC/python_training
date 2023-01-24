from selenium.webdriver.common.by import By
from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        if not (self.app.driver.current_url.endswith("/group.php") and len(
                self.app.driver.find_elements(By.NAME, "new")) > 0):
            self.app.driver.find_element(By.LINK_TEXT, "group page").click()

    def create(self, group):
        self.open_groups_page()
        # init group creation
        self.app.driver.find_element(By.NAME, "new").click()
        self.fill_group_form(group)
        # submit group creation
        self.app.driver.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        if text is not None:
            self.app.driver.find_element(By.NAME, field_name).click()
            self.app.driver.find_element(By.NAME, field_name).clear()
            self.app.driver.find_element(By.NAME, field_name).send_keys(text)

    def delete_group_by_index(self, index):
        self.open_groups_page()
        self.app.driver.find_elements(By.NAME, "selected[]")[index].click()
        self.app.driver.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        self.open_groups_page()
        self.app.driver.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()
        self.app.driver.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def open_groups_page(self):
        if not (self.app.driver.current_url.endswith("/group.php") and len(
                self.app.driver.find_elements(By.NAME, "new")) > 0):
            self.app.driver.find_element(By.LINK_TEXT, "groups").click()

    def edit_group_by_index(self, group, index):
        self.open_groups_page()
        self.app.driver.find_elements(By.NAME, "selected[]")[index].click()
        self.app.driver.find_element(By.NAME, "edit").click()
        self.fill_group_form(group)
        self.app.driver.find_element(By.NAME, "update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def edit_group_by_id(self, group, id):
        self.open_groups_page()
        self.app.driver.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()
        self.app.driver.find_element(By.NAME, "edit").click()
        self.fill_group_form(group)
        self.app.driver.find_element(By.NAME, "update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def count(self):
        self.open_groups_page()
        return len(self.app.driver.find_elements(By.NAME, "selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            self.open_groups_page()
            self.group_cache = []
            for element in self.app.driver.find_elements(By.CSS_SELECTOR, "span.group"):
                text = element.text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)
