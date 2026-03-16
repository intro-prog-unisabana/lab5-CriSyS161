import math
a = int(input("Enter an integer: "))
b = math.log2(a)
print("Log base 2 of ",a," is: ",b)
c = math.floor(b)
d = math.ceil(b)
print("Floor: ",c)
print("Ceiling: ",d)