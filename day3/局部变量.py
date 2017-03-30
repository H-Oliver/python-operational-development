# age = 23
# def change_name(name):
#     print("before change",name)
#     name = "Alex"
#     age = 23
#     print("after change",name)
#
#
# name = "alex"
# change_name(name)
# print(name)
# print(age)

def change_name():
    global name
    name = "alex"

change_name()
print(name)