# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Petrov", middlename="Petr", lastname="Petrovich", nickname="Ppp1",
                           homephone="+7(333)9983333", mobilephone="+7(912)8838833", workphone="+7(938)8848844", secondaryphone="dfdf")
    app.contact.client_create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
