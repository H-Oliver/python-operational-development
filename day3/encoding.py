# -*- coding:utf-8 -*-
import sys
print(sys.getdefaultencoding())

s = "你好"
print(s.encode("gbk"))
print(s.encode("uft-8"))
print(s.encode("utf-8").decode("utf-8").encode("gb2312"))
