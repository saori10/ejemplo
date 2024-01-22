# las tuplas se declaran con ()
numbers = (1, 2, 3, 4)
strings = ("sao", "santi", "luci", "santi")
print(numbers)
print("0 =>", numbers[0])
print("-1 =>", numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

# las tuplas no se modifican una vez declaradas

print(strings)
print(strings.index("santi"))

print(strings.count("santi"))

my_list = list(strings)      
print(my_list)
print(type(my_list))      

my_list[1] = "mika"
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)
