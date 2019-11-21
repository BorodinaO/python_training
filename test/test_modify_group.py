from model.group import Group
import pytest


def test_modify_group_name(app):
    with pytest.allure.step('Modify group name'):
        app.group.modify_first_group(Group(name="New group"))


def test_modify_group_header(app):
    with pytest.allure.step('Modify group header'):
        app.group.modify_first_group(Group(header="New header"))
