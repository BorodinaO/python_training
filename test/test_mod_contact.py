from model.contact import Contact
import random


def test_mod_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.client_create(
            Contact(firstname="Petrov", lastname="Petrovich", home="+7(333)9983333", mobile="+7(912)8838833",
                    work="+7(938)8848844", phone2="dfdf",
                    email="dfdsf@rr.ru", email2="ytytyt@tt.ru", email3="iiror@it.ru"))
    old_contacts = db.get_contact_list()
    contact = Contact(firstname="Иванов", lastname="Иванович", home="+7(333)9983000", mobile="+7(912)8838000",
                      work="+7(938)8848000", phone2="222", address="hghgg",
                      email="dfdsf11@rr.ru", email2="ytytyt11@tt.ru", email3="iiro11r@it.ru")
    index = random.randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    id = contact.id
    app.contact.mod_contact_by_id(contact, id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
