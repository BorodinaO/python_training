from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, id=None, all_phones_from_home_page=None, home=None,
                 work=None, mobile=None, phone2=None, email=None, email2=None, email3=None,
                 all_emails_from_home_page=None, address=None):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id
        self.home = home
        self.work = work
        self.mobile = mobile
        self.phone2 = phone2
        self.all_phones_from_home_page = all_phones_from_home_page
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_home_page = all_emails_from_home_page
        self.address = address

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % (self.id, self.lastname, self.firstname, self.email, self.email2,
                                                     self.email3,
                                                     self.home, self.work, self.phone2, self.address, self.mobile)

    def __eq__(self, other):
        return (
                       self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
