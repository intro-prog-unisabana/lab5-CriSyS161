def list_shift(numbers, valor):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] + valor
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
list_shift(numbers, 0.8)
print(numbers)

def calc_avg(numbers):
    return sum(numbers) / len(numbers)

def print_normalized (numbers):
    print(numbers)
