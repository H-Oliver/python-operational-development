#import json
import pickle


def sayhi(name):
    print("hello,",name)


f = open("test.text","rb")

data = pickle.loads(f.read())

print(data["func"])

f.close