person = {
    "name" : "Saori",
    "last_name" : "Rocillo",
    "langs" : ["python", "C++"],
    "age" : 16
}

print(person)

person["name"] = "Mika"
person["age"] -= 3
person["langs"].append("rust")
print(person)

del person["last_name"]
person.pop("age")
print(person)

# genera tuplas
print("items")
print(person.items())
 

# solo los atributos que tiene
print("keys")
print(person.keys())
 
# solo los valores
print("values")
print(person.values())
 