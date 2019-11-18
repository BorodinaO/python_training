from model.contact import Contact
from model.group import Group
import random


def test_remove_contact_from_group(app, db, orm):
    if len(app.group.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(app.contact.get_contact_list()) == 0:
        app.contact.client_create(Contact(firstname="Petrov", lastname="Petrovich", address="Petrova1-42",
                                          home="+7(333)9983333", mobile="+7(912)8838833", work="+7(938)8848844",
                                          email="dfdsf@rr.ru", email2="ytytyt@tt.ru", email3="iiror@it.ru"))
    if len(db.get_groups_with_contacts()) == 0:
        contact_id = random.choice(db.get_contact_list()).id
        group_id = random.choice(db.get_group_list()).id
        app.contact.add_contact_in_group(Contact(id=contact_id), Group(id=group_id))

    group_id = random.choice(db.get_groups_with_contacts()).id

    contact_id = random.choice(orm.get_contacts_in_group(Group(id=group_id))).id

    old_contact_list = orm.get_contacts_in_group(Group(id=group_id))
    app.contact.remove_contact_from_group(Contact(id=contact_id), Group(id=group_id))
    new_contact_list = orm.get_contacts_in_group(Group(id=group_id))
    assert sorted(old_contact_list, key=Contact.id_or_max) != sorted(new_contact_list, key=Contact.id_or_max)
    app.contact.add_contact_in_group(Contact(id=contact_id), Group(id=group_id))
    new_contact_list = orm.get_contacts_in_group(Group(id=group_id))
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
