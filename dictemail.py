# for people in range(5):
#     name = input("Name:")
#     email_address = input("Email_address:")

# attendees = {'Name': [], 'Email_address': []}


# def make_list(attendees):
#     attendees = {name: email_address}
#     if people in attendees:
#         name[keys].append(value)

# print(attendees[name], attendees[email_address])
my_dict = {}
for people in range(5):
    name = input("name:")
    email_address = input("email_address:")
    my_dict[name] = email_address
# my_dict.keys()
# my_dict.value()


def my_name(name):
    if name in my_dict.keys():
        return my_dict[name]
    else:
        print("Please input a normal name")

given_name = input("What name would you want to look for?")

print(my_name(given_name))
