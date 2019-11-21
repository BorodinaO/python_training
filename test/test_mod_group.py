from model.group import Group
import random
import pytest


def test_mod_group(app, db):
    with pytest.allure.step('Given a group list'):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="test"))
        old_groups = db.get_group_list()
    with pytest.allure.step('Choice group and modify'):
        index = random.randrange(len(old_groups))
        group = Group(name="One", header="Two", footer="Three")
        group.id = old_groups[index].id
        app.group.mod_group_by_id(group.id, group)
    with pytest.allure.step('Compare new_groups and old_groups after modify group'):
        old_groups[index] = group
        new_groups = db.get_group_list()
        assert len(old_groups) == len(new_groups)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
