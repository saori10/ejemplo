# indexing = los textos tienen un indicador a los cuales se pueden ingresar a nivel de pocisiones
text = "Ella sabe Python"
print(text[0])
print(text[1])
# print(text[999]) = al darle una posiciún inexistente da error

# para imprimir la última letra del texto
size = len(text)
print("size => ", size)
print(text[size - 1])

# de manera más simple
print(text[-1])


# slicing = permite sacar ciertas partes del texto
print(text[0:5])
print(text[10:16])
print(text[:10])
print(text[5:-1])
print(text[5:])
print(text[:])

# saltos
print(text[10:16:1])
print(text[10:16:2])

print(text[::])