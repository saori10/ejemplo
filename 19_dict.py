my_dict = {}
print(type(my_dict))

my_dict = {
    "name" : "Saori",
    "last_name" : "Rocillo ",
    "age" : "15"
}
print(my_dict)

print(len(my_dict))

print(my_dict["age"])
print(my_dict["last_name"])
print(my_dict.get("age"))

print("name" in my_dict)
print("noestá" in my_dict)