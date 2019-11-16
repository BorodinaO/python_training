# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", home="",
                    work="", mobile="", phone2="",
                    email="", email2="", email3="", address="")] + [
               Contact(firstname=firstname, lastname=lastname, home=home,
                       work=work, mobile=mobile, phone2=phone2,
                       email=email, email2=email2, email3=email3, address=address)
               for firstname in [random_string("firstname", 10)]
               for middlename in [random_string("middlename", 10)]
               for lastname in [random_string("lastname", 10)]
               for home in [random_string("home", 12)]
               for work in [random_string("work", 12)]
               for mobile in [random_string("mobile", 12)]
               for phone2 in [random_string("phone2", 12)]
               for email in [random_string("email", 10)]
               for email2 in [random_string("email2", 10)]
               for email3 in [random_string("email3", 10)]
               for address in [random_string("address", 20)]
               for i in range(5)

           ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.client_create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
