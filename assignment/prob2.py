l=[1,2,3,4,5]
l1=[4,5,9,6,7,8]
n=0
m=0
for i in l:
    if i>n:
     n=i
for j in l1:  
        if j>m:
            m=j
if m<n:
    print(n) 
else:
    print(m)                   
