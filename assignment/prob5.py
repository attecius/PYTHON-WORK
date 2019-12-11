var=int(input())
list=[2,3,4,8,5]
for i in list:
    for j in list:
        if i+j==var:
            print(i,j)
            