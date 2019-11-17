from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contact", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

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
               for i in range(n)

           ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))