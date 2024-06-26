def find_great(n1,n2,n3):
    if (n1>n2 and n1>n3):
        return n1
    elif (n2>n3):
        return n2
    else:
        return n3
    

print(find_great(111,22,37))