from model.contact import Contact
from model.group import Group
import random


def test_del_contact_from_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    groups = orm.get_group_list()
    group = random.choice(groups)
    if len(orm.get_contacts_in_group(group.id)) == 0:
        if len(orm.get_contact_list()) == 0:
            app.contact.create(Contact(lastname="test", firstname="test"))
        contacts = orm.get_contact_list()
        contact = random.choice(contacts)
        app.contact.add_contact_in_group(contact.id, group.id)
    old_contacts_in_group = orm.get_contacts_in_group(group.id)
    contact_in_group = random.choice(old_contacts_in_group)
    app.contact.del_contact_from_group(contact_in_group.id, group.id)
    new_contacts_in_group = orm.get_contacts_in_group(group.id)
    old_contacts_in_group.remove(contact_in_group)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)
