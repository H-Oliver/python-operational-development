'''
def test(*args):
    print(args)

test(*[1,2,4,5,6,7,8])

def test1(x,*args):
    print (x)
    print(args)

test(1,2,3,4,5,6)

def test2(**kwargs):
    print(kwargs)
    print(kwargs["name"])
    print(kwargs["age"])
test2(name="oliver",age="26")
test2(**{"name":"alex","age":"23"})
'''

