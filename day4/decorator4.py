import time
def timer(func):    #timer(test1) func=test1
    def deco(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        stop_time=time.time()
        print("the func run time is %s" %(stop_time-start_time ))
    return deco

# def timer():
#     def deco():
#         pass

@timer  #--->test1=timer(test1)
def test1():
    time.sleep(3)
    print("in the test1")

@timer #--->test2=timer(test2)
def test2(name,age):
    # time.sleep(3)
    print("in the test2:",name,age)

# def test2():
#     time.sleep(3)
#     print("in the test2")



test1()
test2("alex",22)

