import jsonpickle
import random
import string
from model.contact import Contact
import os
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
