# print(all([ 0,-5,3]))
# print(any([0,-5,3]))
# print(any([]))
# print(ascii([1,2,"我是中国人"]))

# a = bytes("abcde",encoding="utf-8")
# b = bytearray("abcde",encoding="utf-8")
# print( b[1])
# b[1] = 50
# print(b)
# # print(a.capitalize(),a)

# def sayhi():pass
# print(callable(sayhi))

# code = '''
# def fib(max):
#     n,a,b = 0,0,1
#     while n < max:
#         #print(b)
#         yield b
#         a,b = b,a + b
#         n = n + 1
#     return "----done-----"
#
# # print(fib(100))
# f = fib(10)
#
# while True:
#     try:
#         x = next(f)
#         print("f:",x)
#     except StopIteration as e:
#         print("Generator return value",e.value)
#         break
#
# #---------------------------------
# # print(f.__next__())
# # print(f.__next__())
# # print(f.__next__())
# # print(f.__next__())
# # print(f.__next__())
# # print(f.__next__())
# # print(f.__next__())
# # print(f.__next__())
# # print(f.__next__())
# # print(f.__next__())
# # print(f.__next__())
# #---------------------------------
# # for i in f:
# #     print(i)
#
# '''
# py_obj = compile(code,"err.log","exec")
# exec(py_obj)

# def sayhi(n):
#     print(n)
#     for i in range(n):
#         print(i)
# sayhi(3)
#
# #(lambda n:print(n))(5)
# calc = lambda n:3 if n < 4 else n
# print(calc(2))

# calc = filter(lambda n:n>5,range(10))
# for i in calc:
#     print(i)

# res = map(lambda n:n*2,range(10))
# res1 = [lambda n:n*2,range(10)]

# import functools
# res = functools.reduce( lambda x,y:x*y,range(1,10))
# print(res)

def test():
    local_var = 333

test()
print(globals())
print(globals().get("local_var"))
