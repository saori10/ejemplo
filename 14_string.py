text = "Ella sabe programar en Python"

print("JavaScript" in text)
print("Python" in text)

if "Python" in text:
    print("Elegiste bien")
else:
    print("También elegiste bien")

# len permite analizar la cantidad de caracteres en una cadena de texto
size = len(text)
print(size)

# upper = cambia todas las letras a mayúsculas
print(text.upper())

# lower = pone todas las letras en minúsculas
print(text.lower())

# count = cuenta el numero d eveces que aparece una letra en una cadena de texto
print(text.count("a"))

# swapcase = cambia los caracteres que esten en mayúscula a minúscula y viceversa
print(text.swapcase())

# startswith = para preguntar algo en específico al comienzo de la oracion
# endswith = para preguntar algo en específico al final de la oracion
# la respuesta de ambas son o True o False
print(text.startswith("Ella"))
print(text.endswith("Rust"))

# replace = permite cambiar una palabra por otra
print(text.replace("Python", "Go"))

text_2 = "este es un título"
print(text_2)

# capitalize = pone el primer caracter en mayúscula
print(text_2.capitalize())

# title = pone el inicio de cada palabra en mayúscula
print(text_2.title())

# isdigit = indica si el texto es un dijito
print(text_2.isdigit())
print("243".isdigit())
