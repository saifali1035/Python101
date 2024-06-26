def fact(n):
    if n==0:
        return 1
    else:
        return n * fact(n-1) #fumction calling itself
    

number=int(input("Give me a number you human :"))
print(fact(number))