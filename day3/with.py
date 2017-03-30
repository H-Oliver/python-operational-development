import sys
#f = open("yesterday2","r",encoding="utf-8")
#f_new = open("yesterday2.new","w",encoding="utf-8")
with open("yesterday2","r",encoding="utf-8") as f,\
      open("yesterday2.new","r",encoding="utf-8"):
    for line in f:
        print(line)
