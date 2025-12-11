Pi = 3.14
rooms = "\n прямоугольник - 1\n треугольник- 2\n круг- 3"
print(rooms)
print("Введите тип комнаты:")
type_room = input()
if type_room == "1":
    print("Введи длину и ширину")
    a = int(input("длина - "))
    b = int(input("ширина - "))
    formula = a * b
    print('ответ -', formula)
elif type_room == "2":
    print("Треугольная комната")
    print("введи длины сторон")
    a = int(input("длина первой стороны - "))
    b = int(input("длина второй стороны - "))
    c = int(input("длина третьей стороны - "))
    p = (a + b + c) /2
    s = (p*(p - a)*(p - b)*(p - c)) ** 0.5
    print('ответ - ', s)
elif type_room == "3":
    print("Круглая комната")
    print("Введи радиус круга")
    r = int(input("Радиус круга - "))
    formula = Pi * (r ** 2)
    print("ответ - ", formula)
else:
    print("Введите цифру")