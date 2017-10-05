# #You are organizing Accra's hottest networking event. Make sure to register everyone!.
# 1. Take in a name + email. Store it in a dict.
# 2. Create a function to return an email, given a name.
# 3. Use an email library to send everybody an email.
# 4. Send a message with their name in the body.

import smtplib

list = ["evalyne.wangari@meltwater.org",
        "lavet.adhiambo@meltwater.org", "cavendish.mwangi@meltwater.org", "everlyne.kaberere@meltwater.org"]


for i in range(len(list)):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("kaberereeve44@gmail.com", " 27538204079")
    subject = "Women empowerment"
    message = "Bishes, Women in Technology!!!"
    s.sendmail("kaberereeve44@gmail.com",
               list[i], message)
    s.quit()


class Attendees:

    def __init__(self):
        self.values = {}

    def get_attendees(self):
        name = input("Enter your name:")
        email = input("Enter your email:")
        self.values[name] = email
        print(self.values)

    def search_mail(name):
        if name in dict.keys():
            email = dict[name]
            return email

mest_party = Attendees()
mest_party.get_attendees()
mest_party.get_attendees()
mest_party.get_attendees()
mest_party.get_attendees()
mest_party.get_attendees()


def get_emails(self, name, email):
    dict_one = {}
    dict_one["Everlyne Kaberere"] = ["kaberereeve44@gmail.com"]
    first_attendee = dict_one["Everlyne Kaberere"]
    print(first_attendee)
