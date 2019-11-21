from model.group import Group
from model.contact import Contact
import random
import pytest


def test_add_contact_in_group(app, db, orm):
    with pytest.allure.step('Get group'):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="test"))
        group = random.choice(db.get_group_list())
    with pytest.allure.step('Get contact not in this group'):
        if len(db.get_contact_list()) == 0 or len(orm.get_contacts_not_in_group(group)) == 0:
            app.contact.client_create(Contact(firstname="Petrov", lastname="Petrovich", address="Petrova1-42",
                                              home="+7(333)9983333", mobile="+7(912)8838833", work="+7(938)8848844",
                                              email="dfdsf@rr.ru", email2="ytytyt@tt.ru", email3="iiror@it.ru"))
        contact = random.choice(orm.get_contacts_not_in_group(group))
    with pytest.allure.step('Save old contact list'):
        old_contact_list = orm.get_contacts_in_group(group)
    with pytest.allure.step('Add contact in group'):
        app.contact.add_contact_in_group(contact, group)
    with pytest.allure.step('Compare new_contacts and old_contacts after add contact'):
        new_contact_list = orm.get_contacts_in_group(group)
        old_contact_list.append(contact)
        assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
