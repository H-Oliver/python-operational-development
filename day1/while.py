'''count = 0
while True:
    print("count:",count)
    count += 1

for i in range(0,10):
    if i < 5:
        print("loop",i)
    else:
        continue
    print("呵呵...")
'''

for i in range(10):

    print('---------',i)
    for j in range(10):
        print(j)
        if j > 5:
            break