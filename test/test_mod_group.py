from model.group import Group

def test_mod_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.mod_first_group(Group(name="One", header="Two", footer="Three"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)