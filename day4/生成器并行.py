import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield
       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))

# c = consumer("alex")
# c.__next__()

# b1="韭菜馅"
# c.send(b1)
# #c.__next__()


def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("%s 开始准备做包子啦!" % name)
    for i in range(10):
        time.sleep(1)
        print("\n做了1个包子!,一人一半")
        c.send(i)
        c2.send(i)

producer("alex")