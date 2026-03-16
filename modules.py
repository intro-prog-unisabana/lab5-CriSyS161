import math
print
num = int(input("Enter an integer:"))
resultado = math.log2(num)
print(f"The log base 2 of {num} is: {resultado}")
print(f"Floor: {math.floor(resultado)}")
print(f"Ceiling: {math.ceil(resultado)}")