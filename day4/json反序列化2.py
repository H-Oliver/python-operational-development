#import json
import pickle


def sayhi(name):
    print("hello,",name)


f = open("test.text","rb")

#data = pickle.loads(f.read())
data = pickle.load(f)

print(data["func"]("alex"))

f.close