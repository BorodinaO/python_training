from model.group import Group

def test_mod_group(app):
    app.session.login(username="admin", password="secret")
    app.group.mod_first_group(Group(name="One", header="Two", footer="Three"))
    app.session.logout()