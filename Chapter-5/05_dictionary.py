my_dict={
    "name":"Saif",
    "age":22,
    "marks":[10,9,6],
    "my_dict2":{"name2":"Wasim"},
    1:2
}

print(my_dict["name"])

print(my_dict["my_dict2"]["name2"])    #priting values from a nested dict


#Typecasting to list
print(list(my_dict))




#Dictionary methods
print(my_dict.keys())
print(my_dict.values())


print(my_dict.items())


#Update method
my_dict.update({"New":"Entry"})

new_dict={
    "Another":"Entry"
}

my_dict.update(new_dict)

print(my_dict)


