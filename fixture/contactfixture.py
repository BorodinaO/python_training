from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


class ContactFixture:

    def __init__(self, app):
        self.app = app

    def client_create(self, contact):
        wd = self.app.wd
        # client creation
        wd.find_element_by_link_text("add new").click()
        # fill form
        self.contact_fill_form(contact)
        # save client
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def mod_first_contact(self, contact):
        self.mod_contact_by_index(0)

    def mod_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_forms_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # fill form
        self.contact_fill_form(contact)
        # save contact
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def mod_contact_by_id(self, contact, id):
        wd = self.app.wd
        self.open_forms_page()
        wd.get("http://localhost/addressbook/edit.php?id={0}".format(id))
        # fill form
        self.contact_fill_form(contact)
        # save contact
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def contact_fill_form(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)

    def count(self):
        wd = self.app.wd
        self.open_forms_page()
        return len(wd.find_elements_by_name("selected[]"))

    def open_forms_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")):
            wd.find_element_by_xpath("//img[@alt='Addressbook']").click()

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_forms_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                address = cells[3].text
                self.contact_cache.append(
                    Contact(lastname=lastname, firstname=firstname, id=id, all_phones_from_home_page=all_phones,
                            all_emails_from_home_page=all_emails, address=address))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_forms_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_edit_by_id(self, contact, id):
        wd = self.app.wd
        self.open_forms_page()
        wd.get("http://localhost/addressbook/edit.php?id={0}".format(id))
        self.contact_fill_form(contact)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        home = wd.find_element_by_name("home").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return Contact(home=home, work=work, mobile=mobile, phone2=phone2,
                       firstname=firstname, lastname=lastname, id=id,
                       email=email, email2=email2, email3=email3, address=address)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=home, work=work, mobile=mobile, phone2=phone2)

    def add_contact_in_group(self, contact, group):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//select[@name='group']/option[@value='']").click()
        self.select_contact_by_id(contact.id)
        wd.find_element_by_xpath("//select[@name='to_group']/option[@value='%s']" % group.id).click()
        wd.find_element_by_name("add").click()
        self.app.open_home_page()
        self.contact_cache = None

    def remove_contact_from_group(self, contact, group):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//select[@name='group']/option[@value='%s']" % group.id).click()
        self.select_contact_by_id(contact.id)
        wd.find_element_by_name("remove").click()
        self.app.open_home_page()
        self.contact_cache = None