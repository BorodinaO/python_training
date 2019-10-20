# -*- coding: utf-8 -*-
from model.contact import ContactHelper

def test_add_contact(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.client_create(ContactHelper(firstname = "Petrov", middlename = "Petr", lastname = "Petrovich", nickname = "Ppp1", title = "Rere", company = "OooPetrov", address = "Petrova1-42",
                           home = "+7(333)9983333", mobile = "+7(912)8838833", work = "+7(938)8848844", fax = "+7(448)8847777", email = "dfdsf@rr.ru",
                           email2 = "ytytyt@tt.ru", email3 = "iiror@it.ru", homepage = "www.tt.ru", bday = "13", bmonth = "January", byear = "1990", aday = "15", amonth = "November",
                           ayear = "2015", address2 = "gfgdfg,3 - 5", phone2 = "dfdf", notes = "dfdfs"))
    app.contact.return_to_home_page()
    app.session.logout()
