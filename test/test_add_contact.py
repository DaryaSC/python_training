from model.contact import Contact
import random
import string
import pytest


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_number(maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home="",
                    mobile="", work="", fax="", email="", email2="", email3="", homepage="", address2="", phone2="",
                    notes="")] + [
    Contact(firstname=random_string(10), middlename=random_string(10),
            lastname=random_string(10), nickname=random_string(10),
            title=random_string(10), company=random_string(10), address=random_string(10),
            home=random_number(7), mobile=random_number(7), work=random_number(7), fax=random_number(7),
            email=random_string(10), email2=random_string(10), email3=random_string(10),
            homepage=random_string(10), address2=random_string(10), phone2=random_number(7),
            notes=random_string(10))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
