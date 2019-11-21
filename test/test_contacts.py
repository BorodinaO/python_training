import re
from model.contact import Contact
import pytest


def test_contacts_on_home_page(app, db):
    with pytest.allure.step('Given a contact list from ui'):
        contact_from_ui = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    with pytest.allure.step('Given a contact list from db'):
        contact_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    with pytest.allure.step('Compare contact list'):
        assert len(contact_from_ui) == len(contact_from_db)
        for index in range(len(contact_from_ui)):
            assert contact_from_ui[index].firstname.replace(' ', '') == contact_from_db[index].firstname.replace(' ', '')
            assert contact_from_ui[index].lastname.replace(' ', '') == contact_from_db[index].lastname.replace(' ', '')
            assert contact_from_ui[index].address.replace(' ', '') == contact_from_db[index].address.replace(' ', '')
            assert contact_from_ui[index].all_phones_from_home_page == merge_phones_like_on_home_page(
                contact_from_db[index])
            assert contact_from_ui[index].all_emails_from_home_page.replace(' ', '') == merge_emails_like_on_home_page(
                contact_from_db[index])


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work,
                                        contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))
