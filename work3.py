#Задание 3
#Ввести число, вывести все его делители.

print ("Введите целое число")
b = int(input())
c = 1
print ("Результат")
while c <= b ** 0.5 :
    if b % c == 0:
        print (c, b //c )
        
    c+=1