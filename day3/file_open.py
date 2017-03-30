#data = open("yesterday",encoding="utf-8").read()
#f = open("yesterday2","r+",encoding="utf-8",) #文件句柄,读写
#f = open("yesterday2","w+",encoding="utf-8",) #文件句柄,写读
#f = open("yesterday2","a+",encoding="utf-8",) #文件句柄,追加写读
f = open("yesterday2","rb") #文件句柄,二进制文件读


'''
print(f.readline())
print(f.readline())
print(f.readline())
print(f.tell())
f.write("\n-------------hello-------------\n")
f.write("\n-------------hello-------------\n")
f.write("\n-------------hello-------------\n")
f.write("\n-------------hello-------------\n")
print(f.tell())
f.seek(10)
print(f.readline())
f.write("afafafafafafafaff")
f.write("\n我爱北京天安门....\n")
f.write("天安门上太阳升....")
print(data)
print(f.tell())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.tell())
f.seek(0)
print(f.readline())
print("---------")
print(f.encoding)
print(f.fileno())
print(f.name)
print(f.flush())
print(dir(f.buffer))
f.write("hello 1\n")
f.truncate(10)
'''

f.close()
