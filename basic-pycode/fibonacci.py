var=int(input())
a=0
b=1
print(0)
print(1)
if var<0:
    print("wrong input")
elif var==0:
    print(a)
elif var == 1:
     print(b)
else:
    for i in range (2,var):
        c = a + b
        a=b
        b=c
        print(b)         


