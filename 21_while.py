# Mientras(while) la condicion se cumpla la instrucción se ejecutará
"""
while True:
    print("se ejecuta")

counter = 0

while counter < 10:
    counter += 1
    print(counter)

counter = 0

while counter < 20:
    counter += 1
    if counter == 15:
        break  # Es una manera forzada de romper un ciclo
    print(counter)
"""

counter = 0

while counter < 20:
    counter += 1
    if counter < 15:
        continue # Salta automaticamente al siguiente ciclo obviando lo que hay de las lineas para abajo
    print(counter)