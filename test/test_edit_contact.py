from model.contact import Contact


def test_edit_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.edit_first_contact(Contact(firstname="new frstname"))
