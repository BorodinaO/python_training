from model.contact import Contact
from random import randrange

def test_mod_contact(app):
    if app.contact.count() == 0:
        app.contact.client_create(Contact(firstname="Petrov", middlename="Petr", lastname="Petrovich", nickname="Ppp1", title="Rere",company="OooPetrov", address="Petrova1-42",home="+7(333)9983333", mobile="+7(912)8838833", work="+7(938)8848844", fax="+7(448)8847777", email="dfdsf@rr.ru", email2="ytytyt@tt.ru", email3="iiror@it.ru", homepage="www.tt.ru", bday="13", bmonth="January", byear="1990", aday="15", amonth="November", ayear="2015", address2="gfgdfg,3 - 5", phone2="dfdf", notes="dfdfs"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname = "Иванов", middlename = "Иван", lastname = "Иванович", nickname = "111", title = "Rere11", company = "OooPetrov111", address = "Petrova99-99", home = "+7(333)9983000", mobile = "+7(912)8838000", work="+7(938)8848000", fax="+7(448)8840000", email="dfdsf@111rr.ru", email2= "ytytyt@t111t.ru", email3 = "iiror@i111t.ru", homepage = "www.t111t.ru", bday = "10", bmonth = "January", byear = "1992", aday = "10", amonth = "November", ayear="2016", address2="gfgdfg,1 - 5", phone2 = "dfdf222", notes = "dfdf222s")
    contact.id = old_contacts[index].id
    app.contact.mod_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)