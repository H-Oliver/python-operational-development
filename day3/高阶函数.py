# def add(a,b,f):
#     return f(a) + f(b)
#
# res = add(3,-6,abs)
# print(res)

a = 1
b = 4
def sum():
    global a
    a = 3
    print("a + b =",a+b)

def sum1():
    global b
    b = 5
    print("a - b =",a-b)

print(a)
print(b)
print("-----------------")
sum()
print(a)
print(b)
print("-----------------")
sum1()
print(a)
print(b)

