import json
import pickle


f = open("test.text","r")

#data = pickle.loads(f.read())
data = json.load(f)

print(data["func"]("Alex"))

f.close