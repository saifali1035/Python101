import math
class Cal:
    def squareRoot(self,value):
        value=int(value)
        print(f"Value is {math.sqrt(value)}")


newNum=Cal()
value=input("Enter a number:")
newNum.squareRoot(value)

