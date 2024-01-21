numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))

tasks =["make a dishes", "play videogames"]
print(tasks)

types = [1, True, "hola"]
print(types)

print(numbers[0])
print(tasks[0])


# los str no son mutables en cambio, las listas si

text = "Hola"
#text[0] = w

tasks[0] = "watch platzi courses"
print(tasks)

tasks[0] = "od the dishes"
print(tasks)

print(numbers[:3])
print(True in types)
print("hola" in types)


