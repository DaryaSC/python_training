from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="fgh", middlename="hfgh", lastname="fgh", nickname="fhfg", title="hfg", company="fghfg",
                address="fghfh", home="54", mobile="546", work="4864", fax="345343",
                email="fdgf", email2="gsaf", email3="sdfh", homepage="gdsrg", address2="gdg", phone2="gdfg",
                notes="dgdfg")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
