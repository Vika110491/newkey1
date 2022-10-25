#Набрать все примеры посимвольно и заставить их работать, разобраться в их работе.

print ("Времена года")
month = int(input("Введите номер месяца от 1 до 12!"))
if (month <= 3):
    print ("Зима")
elif (month >= 4 ) and (month <= 6):
    print ("Весна")
elif (month >= 7) and (month <= 9):
    print ("Лето")
elif (month >= 10) and (month <= 12):
    print ("Осень")
else:
    print ("Неверно введен месяц(((")

