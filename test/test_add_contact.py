# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest


def test_add_contact(app, db, json_contacts):
    contact = json_contacts
    with pytest.allure.step('Given a contact list'):
        old_contacts = db.get_contact_list()
    with pytest.allure.step('When I add a contact %s to the list' % contact):
        app.contact.client_create(contact)
    with pytest.allure.step('Compare new_contacts and old_contacts after add contact'):
        new_contacts = db.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
