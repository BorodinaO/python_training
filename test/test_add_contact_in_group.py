from model.group import Group
from model.contact import Contact
import random


def test_add_contact_in_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(db.get_contact_list()) == 0:
        app.contact.client_create(Contact(firstname="Petrov", lastname="Petrovich", address="Petrova1-42",
                                          home="+7(333)9983333", mobile="+7(912)8838833", work="+7(938)8848844",
                                          email="dfdsf@rr.ru", email2="ytytyt@tt.ru", email3="iiror@it.ru"))
    groups_list = db.get_group_list()
    group = random.choice(groups_list)
    contacts_ih_group = orm.get_contacts_in_group(group)
    contact_list = db.get_contact_list()
    contact = random.choice(contact_list)
    if contact in contacts_ih_group:
        app.contact.remove_contact_from_group(contact, group)
        contacts_ih_group = orm.get_contacts_in_group(group)
    app.contact.add_contact_in_group(contact, group)
    contacts_ih_group.append(contact)
    assert sorted(contacts_ih_group, key=Contact.id_or_max) == sorted(orm.get_contacts_in_group(group),
                                                                      key=Contact.id_or_max)
