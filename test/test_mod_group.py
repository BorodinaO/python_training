from model.group import Group
import random


def test_mod_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    index = random.randrange(len(old_groups))
    group = Group(name="One", header="Two", footer="Three")
    group.id = old_groups[index].id
    old_groups[index] = group
    app.group.mod_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)