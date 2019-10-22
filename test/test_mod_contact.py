from model.contact import Contact

def test_mod_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.mod_first_contact(Contact(firstname = "Иванов", middlename = "Иван", lastname = "Иванович", nickname = "111", title = "Rere11", company = "OooPetrov111", address = "Petrova99-99",
                           home = "+7(333)9983000", mobile = "+7(912)8838000", work = "+7(938)8848000", fax = "+7(448)8840000", email = "dfdsf@111rr.ru",
                           email2 = "ytytyt@t111t.ru", email3 = "iiror@i111t.ru", homepage = "www.t111t.ru", bday = "10", bmonth = "January", byear = "1992", aday = "10", amonth = "November",
                           ayear = "2016", address2 = "gfgdfg,1 - 5", phone2 = "dfdf222", notes = "dfdf222s"))
    app.session.logout()