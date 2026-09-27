numbers = [3, 5, 7, 4, 8, 10]
first_even = next(number for number in numbers if number % 2 == 0)
print(first_even)