import random
random.seed(123)
range_inicio = int(input("Enter the start value:\n"))
range_final = int(input("Enter the end value:\n"))
num_random = random.randint(range_inicio, range_final)
print(f"Generated random number: {num_random}")