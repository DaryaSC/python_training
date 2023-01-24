import random
from model.group import Group


def test_edit_some_group(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    index = old_groups.index(group)
    group_new = Group(name="new name")
    group_new.id = group.id
    app.group.edit_group_by_id(group_new, group.id)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups[index] = group_new
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
