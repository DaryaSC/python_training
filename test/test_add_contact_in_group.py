from model.contact import Contact
from model.group import Group
import random


def test_add_contact_in_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(lastname="test", firstname="test"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    groups = orm.get_group_list()
    group = random.choice(groups)
    contacts = orm.get_contacts_not_in_group(group.id)
    if len(contacts) == 0:
        app.contact.create(Contact(lastname="test1", firstname="test1"))
        contacts = orm.get_contacts_not_in_group(group.id)
    contact = random.choice(contacts)
    old_contacts_in_group = orm.get_contacts_in_group(group.id)
    app.contact.add_contact_in_group(contact.id, group.id)
    new_contacts_in_group = orm.get_contacts_in_group(group.id)
    old_contacts_in_group.append(contact)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)


