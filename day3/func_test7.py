def test(name,age=18,*args,**kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)
    logger("TEST4")

def logger(source):
    print("from %s" % source)

test("alex",age="24",sex="m",hobby="tesla")