from model.contact import Contact
from model.group import Group
import random
import pytest


def test_remove_contact_from_group(app, db, orm):
    with pytest.allure.step('Check for empty group list'):
        if len(app.group.get_group_list()) == 0:
            app.group.create(Group(name="test"))
    with pytest.allure.step('Check for empty contact list'):
        if len(app.contact.get_contact_list()) == 0:
            app.contact.client_create(Contact(firstname="Petrov", lastname="Petrovich", address="Petrova1-42",
                                              home="+7(333)9983333", mobile="+7(912)8838833", work="+7(938)8848844",
                                              email="dfdsf@rr.ru", email2="ytytyt@tt.ru", email3="iiror@it.ru"))
    with pytest.allure.step('Check for contact in group'):
        if len(db.get_groups_with_contacts()) == 0:
            contact_id = random.choice(db.get_contact_list()).id
            group_id = random.choice(db.get_group_list()).id
            app.contact.add_contact_in_group(Contact(id=contact_id), Group(id=group_id))
    with pytest.allure.step('Choice group with contact'):
        group_id = random.choice(db.get_groups_with_contacts()).id
    with pytest.allure.step('Choice contact.id from group with contacts'):
        contact_id = random.choice(orm.get_contacts_in_group(Group(id=group_id))).id
    with pytest.allure.step('Save old contact list from group'):
        old_contact_list = orm.get_contacts_in_group(Group(id=group_id))
    with pytest.allure.step('Remove contact from group'):
        app.contact.remove_contact_from_group(Contact(id=contact_id), Group(id=group_id))
    with pytest.allure.step('Compare new_contacct_list and old_contacct_list after remove contact'):
        new_contact_list = orm.get_contacts_in_group(Group(id=group_id))
        assert sorted(old_contact_list, key=Contact.id_or_max) != sorted(new_contact_list, key=Contact.id_or_max)
        app.contact.add_contact_in_group(Contact(id=contact_id), Group(id=group_id))
        new_contact_list = orm.get_contacts_in_group(Group(id=group_id))
        assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
