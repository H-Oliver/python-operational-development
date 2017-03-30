def test(x,y):
    z = x + y
    print(x,y,z)

test(2,3)  #与形参一一对应
test(y=2,x=1) #与形参顺序无关
test(2,y=4)
test(x=2,y=2)