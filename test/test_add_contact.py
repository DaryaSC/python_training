from model.contact import Contact


def test_add_contact(app):
    app.contact.create(
        Contact(firstname="fgh", middlename="hfgh", lastname="fgh", nickname="fhfg", title="hfg", company="fghfg",
                address="fghfh", home="54", mobile="546", work="4864", fax="345343",
                email="fdgf", email2="gsaf", email3="sdfh", homepage="gdsrg", address2="gdg", phone2="gdfg",
                notes="dgdfg"))
