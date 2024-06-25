number=int(input("Enter a number :"))

if (number is 1):
    print("1 is not Prime")
else:
    for i in range(2,number):
        if (number%i==0):
            print(number, "is not Prime")
            break
    else:
        print(number, "is prime")
            