from model.contact import Contact
import random
import pytest


def test_delete_first_contact(app, db, check_ui):
    with pytest.allure.step('Given a contact list'):
        if len(db.get_contact_list()) == 0:
            app.contact.client_create(Contact(firstname="Petrov", lastname="Petrovich", address="Petrova1-42",
                                              home="+7(333)9983333", mobile="+7(912)8838833", work="+7(938)8848844",
                                              email="dfdsf@rr.ru", email2="ytytyt@tt.ru", email3="iiror@it.ru"))
    with pytest.allure.step('Save old contact list'):
        old_contacts = db.get_contact_list()
    with pytest.allure.step('Choice contact and delete'):
        contact = random.choice(old_contacts)
        app.contact.delete_contact_by_id(contact.id)
    with pytest.allure.step('Compare new_contacts and old_contacts after delete contact'):
        assert len(old_contacts) - 1 == app.contact.count()
        new_contacts = db.get_contact_list()
        old_contacts.remove(contact)
        assert old_contacts == new_contacts
