#Ввести число, вывести его разряды и их множители.

a = int(input('Введите число \n'))
b = print ('Единицы')
b = (a % 10)
print (b)
с = print ('Десятки')
c = (a // 10) % 10
print (c)
x = print ('Сотни')
x = (a // 100) % 10
print (x)
у = print ('Тысячи')
y = a // 1000
print (y)
