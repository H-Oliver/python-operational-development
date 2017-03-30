
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        #print(b)
        yield b
        a,b = b,a + b
        n = n + 1
    return "----done-----"

# print(fib(100))
f = fib(10)

while True:
    try:
        x = next(f)
        print("f:",x)
    except StopIteration as e:
        print("Generator return value",e.value)
        break

#---------------------------------
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
#---------------------------------
# for i in f:
#     print(i)

