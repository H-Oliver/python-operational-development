i = 1

while i < 10:
    j = 1
    while j <= i:
        print("%d x %d = %d" %(i,j,i * j),end="    ")
        j += 1
    print(" ")
    i += 1