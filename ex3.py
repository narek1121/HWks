month = 3  # номер месяца 

if month == 12 or 1 <= month <= 2:
    result = "Зима"
elif 3 <= month <= 5:
    result = "Весна"
elif 6 <= month <= 8:
    result = "Лето"
elif 9 <= month <= 11:
    result = "Осень"
else:
    result = "Некорректный номер месяца"

print(result)