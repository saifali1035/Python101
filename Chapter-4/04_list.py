a = [1,2,55,8,9]
print(a)
print(type(a))
print(a[2])   #with index

a[2]= 99      #changing item of a list
print (a)


b=[1, 2.9, False, "Saif"]
print(b)      #list with items of diff datatype



friends=["Saif","Ali","Wasim","Anil","Faisal"]
print(friends[0:2])          #first value is from where to start and second is till where we can to go


#Sorting the list

list_1=[4,6,2,3,10,0]
list_1.sort()
print(list_1)


#reverse

list_1.reverse()
print(list_1)


#append

list_1.append(45)
print(list_1)

#insert

list_1.insert(0,30)
print(list_1)

#pop

print(list_1.pop(0))
print(list_1)


# remove

list_1.remove(6)
print(list_1)

