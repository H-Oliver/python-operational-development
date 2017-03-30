# -*- coding:utf-8 -*-



import sys,os
print(sys.path)


os.path.abspath(__file__)
x = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(x)

import module_alex

module_alex.say_hello()