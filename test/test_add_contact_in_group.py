from model.group import Group
from model.contact import Contact
import random


def test_add_contact_in_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group = random.choice(db.get_group_list())

    if len(db.get_contact_list()) == 0 or len(orm.get_contacts_not_in_group(group)) == 0:
        app.contact.client_create(Contact(firstname="Petrov", lastname="Petrovich", address="Petrova1-42",
                                          home="+7(333)9983333", mobile="+7(912)8838833", work="+7(938)8848844",
                                          email="dfdsf@rr.ru", email2="ytytyt@tt.ru", email3="iiror@it.ru"))
    contact = random.choice(orm.get_contacts_not_in_group(group))
    old_contact_list = orm.get_contacts_in_group(group)
    app.contact.add_contact_in_group(contact, group)
    new_contact_list = orm.get_contacts_in_group(group)
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
