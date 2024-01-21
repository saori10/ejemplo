# CRUD = Create - Read - Update - Delete 

numbers = [1, 2, 3, 4, 5] 
print(numbers[1])

numbers[-1] = 10
print(numbers)

# append() = añade un nuevo elemento al final de la lista
numbers.append(700)
print(numbers)

# insert() = añade un nuevo elemento en un indice específico
numbers.insert(0, "hola")
print(numbers)

numbers.insert(3, "change")
print(numbers)

# se pueden unir listas
tasks = ["todo 1", "todo 2", "todo 3"]
new_list = numbers + tasks
print(new_list)

# index() = para preguntar la posición de un elemento
index = new_list.index("todo 2")
print(index)

new_list[index]= "todo changed"
print(new_list)

# remove() = borra el primer item de la lista cuyo valor concuerde con el indicado
new_list.remove("todo 1")
print(new_list)

# pop() = elimina el último elemnto de la lista y el que se le indique
new_list.pop()
print(new_list)

new_list.pop(0)
print(new_list)

# reverse() = le da vuelta a la lista
new_list.reverse()
print(new_list)

# sort() = ordena automaticamente los elementos de la lista por su valor de menor a mayor
numbers_a = [1, 4, 6, 3]
numbers_a.sort()
print(numbers_a)

strings = ["re", "ab", "ed"]
strings.sort()
print(strings)


