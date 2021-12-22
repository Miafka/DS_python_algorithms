# По введенным пользователем координатам двух точек
# вывести уравнение прямой вида y = kx + b,
# проходящей через эти точки.

print("Введите координаты двух точек:")
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

if x1 == x2 and x1 != 0 and x2 != 0:
    print(f"Прямая параллельна оси ординат и имеет вид x = {x1}")
else:
    if x1 == 0 and x2 == 0:
        print(f"Прямая совпадает с осью ординат и имеет вид x = 0")
    else:
        if y1 == y2 and y1 != 0 and y2 != 0:
            print(f"Прямая параллельна оси абсцисс и имеет вид y = {y1}")
        else:
            if y1 == 0 and y2 == 0:
                print(f"Прямая совпадает с осью абсцисс и имеет вид y = 0")
            else:
                k = (y1 - y2) / (x1 - x2)
                print(f"Уравнение прямой проходящей через точки: "
                      f"({x1}, {y1}), ({x2}, {y2}) y = {k} * x + {y2 - k * x2}")
