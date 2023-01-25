import re
from model.contact import Contact


def test_checking_contact_fields(app, db):
    contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()
    sorted_contacts_from_home_page = sorted(contacts_from_home_page, key=Contact.id_or_max)
    sorted_contacts_from_db = sorted(contacts_from_db, key=Contact.id_or_max)
    for i in range(len(contacts_from_db)):
        assert sorted_contacts_from_home_page[i].lastname == sorted_contacts_from_db[i].lastname
        assert sorted_contacts_from_home_page[i].firstname == sorted_contacts_from_db[i].firstname
        assert sorted_contacts_from_home_page[i].address == sorted_contacts_from_db[i].address
        assert sorted_contacts_from_home_page[i].all_phones_from_home_page == \
               merge_phones_like_on_home_page(sorted_contacts_from_db[i])
        assert sorted_contacts_from_home_page[i].all_emails_from_home_page == \
               merge_emails_like_on_home_page(sorted_contacts_from_db[i])


def clear_phone(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_phone(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None,
                                                      [contact.email, contact.email2, contact.email3])))
