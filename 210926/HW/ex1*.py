results = []

for number in range(1, 101):
	# проверка чисел на делимость и на 3, и на 5
	if number % 15 == 0:
		results.append("FizzBuzz")
	elif number % 3 == 0:
		results.append("Fizz")
	elif number % 5 == 0:
		results.append("Buzz")
	else:
		results.append(str(number))

# вывод всех результатов в строке через пробел
print(*results)