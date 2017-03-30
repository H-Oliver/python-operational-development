import getpass
_username = "oliver"
_password = "abc123"
username = input("username:")
password = input("password:")

if _username == username and _password == password:
    print("Welcome user {name} login...".format(name=username))
else:
    print("Invalid username or password!")