import re
from model.contact import Contact


def test_contacts_on_home_page(app, db):
    contact_from_ui = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert len(contact_from_ui) == len(contact_from_db)
    for index in range(len(contact_from_ui)):
        assert contact_from_ui[index].firstname.replace(' ', '') == contact_from_db[index].firstname.replace(' ', '')
        assert contact_from_ui[index].lastname.replace(' ', '') == contact_from_db[index].lastname.replace(' ', '')
        assert contact_from_ui[index].address.replace(' ', '') == contact_from_db[index].address.replace(' ', '')
        assert contact_from_ui[index].all_phones_from_home_page == "\n".join(
            filter(lambda x: x != "",
                   map(lambda x: clear(x),
                       filter(lambda x: x is not None,
                              [contact_from_db[index].home,
                               contact_from_db[index].mobile,
                               contact_from_db[index].work,
                               contact_from_db[index].phone2]))))

        '''def test_phones_on_contact_view_page(app):
            contact_from_view_page = app.contact.get_contact_from_view_page(0)
            contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
            assert contact_from_view_page.home == contact_from_edit_page.home
            assert contact_from_view_page.work == contact_from_edit_page.work
            assert contact_from_view_page.mobile == contact_from_edit_page.mobile
            assert contact_from_view_page.phone2 == contact_from_edit_page.phone2'''


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.work, contact.mobile,
                                        contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))
