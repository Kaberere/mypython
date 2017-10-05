import hashlib


class Secret:

    def __init__(self, secret, password):
        self.__secret = secret
        self.__password = password

    def get_secret(self, password):
        if password == self.__password:
            print("I don't know you")
        else:
            print("Go away")

    def change_password(self, old_password, new_password):

        if old_password == self.__password:
            self.__password = new_password
            print("Password successfully changed")
            h = hashlib.sha224(new_password.encode()).hexdigest()
            print(h)
        else:
            print("Don't try again")

old_password = input("Put old password:")
new_password = input("Put new password: ")
my_secret = Secret("secret", "password")
my_secret.change_password(old_password, new_password)
