side1 = 0 # первая сторона
side2 = -10 # вторая сторона
side3 = 10 # третья сторона
#опять же, также можно использовать input(), чтобы пользователь сам вводил значения

# проверка на положительные значения
if side1 <= 0 or side2 <= 0 or side3 <= 0:
    result = "Треугольник не существует"
# проверка правила
elif not (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
    result = "Треугольник не существует"
# проверка на тип
elif side1 == side2 == side3:
    result = "Равносторонний треугольник"
elif side1 == side2 or side2 == side3 or side1 == side3:
    result = "Равнобедренный треугольник"
else:
    result = "Разносторонний треугольник"

print(result)
