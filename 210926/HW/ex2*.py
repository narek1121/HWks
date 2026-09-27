primes = []

for number in range(2, 31):
	# проверка делителей до квадратного корня числа
	is_prime = True
	for divisor in range(2, int(number ** 0.5) + 1):
		if number % divisor == 0:
			is_prime = False
			break

	# если делитель не находится, то число простое и добавляем его в список
	if is_prime:
		primes.append(number)

print(primes)