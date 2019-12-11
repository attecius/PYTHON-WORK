

# try:
#     print(x)

# except NameError:
#     print("No variable of this name exists")


x = int(input("Enter a number"))

y = int(input("Enter another number"))

  


try:
   z=  x/y
   print(z)
   print(A)
except ZeroDivisionError:
    print(("Cannot divide by 0"))
except NameError:
    print("NO VARIABLE EXISTS")