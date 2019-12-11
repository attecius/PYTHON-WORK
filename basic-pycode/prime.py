print("enter the number")
var = int(input())
if(var == 2 or var == 3 or var == 7 or var == 5):
    print("number is prime")
elif(var%2==0):
    print("num is not prime")
elif(var%3==0):
    print("num is not prime")
elif(var%7==0):
    print("num is not prime")   
elif(var%5==0):
    print("num is not prime")         
else:
    print("prime")    