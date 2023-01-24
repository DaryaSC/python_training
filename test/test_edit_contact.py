import random
from model.contact import Contact


def test_edit_some_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="test", firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    index = old_contacts.index(contact)
    contact_new = Contact(firstname="test")
    contact_new.id = contact.id
    contact_new.lastname = contact.lastname
    app.contact.edit_contact_by_id(contact_new, contact.id)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact_new
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
