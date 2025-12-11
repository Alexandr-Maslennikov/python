a = int(input("Сколько нужно спать:"))
b = int(input("Сколько не нужно спать:"))
h = int(input("Сколько Аня спит сейчас:"))
if h == a:
    print("Это нормально")
elif h < a:
    print("Недосып")
else:
    print("Пересып")