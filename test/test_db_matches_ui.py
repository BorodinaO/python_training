from model.group import Group
from timeit import timeit
import pytest


def test_group_list(app, db):
    with pytest.allure.step('Failure test'):
        print(timeit(lambda: app.group.get_group_list(), number=1))

        def clean(group):
            return Group(id=group.id, name=group.name.strip())

        print(timeit(lambda: map(clean, db.get_group_list()), number=1000))
        assert False
