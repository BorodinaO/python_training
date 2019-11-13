from model.contact import Contact
from random import randrange

def test_mod_contact(app):
    if app.contact.count() == 0:
        app.contact.client_create(Contact(firstname="Petrov", lastname="Petrovich", homephone="+7(333)9983333", mobilephone="+7(912)8838833", workphone="+7(938)8848844", secondaryphone="dfdf"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Иванов", lastname="Иванович", homephone="+7(333)9983000", mobilephone="+7(912)8838000", workphone="+7(938)8848000", secondaryphone="dfdf222")
    contact.id = old_contacts[index].id
    app.contact.mod_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)