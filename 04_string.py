name = "Saori"
last_name = "Rocillo Galeano"
print(name)
print(last_name)


# concatenacion de strings con un +
full_name = name + " " + last_name
print(full_name)


quote = "I'm Saori"
print(quote)

quote2 = 'She said "Hello"'
print(quote2)

# format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print("V1 =>",template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print("V2 =>",template)

# la mas usada en python
template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print("V3 =>",template)