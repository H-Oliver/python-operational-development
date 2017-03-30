import getpass
import os

_username="oliver"
_password="abc123"
count = 0
while count < 3:
    username = input("username:")
    password = input("password:")
    #password = getpass.getpass("password:")

    username_file = open("e:\\python\\day1\\username.txt", "w")
    username_file.writelines(username,password)
    username_file.close()

    if username == _username and password == _password:
        print("Welcome user {name} login...".format(name=username))
        break
    else:
        print("Invalid username or password!\n")
        count += 1
if count == 3:
    print("输错三次，该用户将被系统锁定，请稍后重试")

