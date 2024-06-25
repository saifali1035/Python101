a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=int(input("Enter Third Number:"))
d=int(input("Enter Fourth Number:"))

if(a>b and a>c and a>d ):
    print("The greatest of 4 number is ", a)
elif(b>c and b>d):
    print("The greatest of 4 number is ", b)
elif(c>d):
    print("The greatest of 4 number is ", c)
else:
    print("The greatest of 4 number is ",d)
   