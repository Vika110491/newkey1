#Задание 1
#Создать словарь оценок предполагаемых студентов (Ключ - ФИ студента, значение - список оценок студентов). Найти самого успешного и самого отстающего по среднему баллу.

print ('Students and rating!')
print ("Stepanov - 4,5,8,9,6")
print ("Nikolenko - 8,8,9,6,7")
print ("Bondarenko - 4,5,3,6,7")
print ("Sirov - 10,9,8,6,2")
print ("Bilokon - 7,8,4,7,10")
students = {'Stepanov' : [4,5,8,9,6], 'Nikolenko' : [8,8,9,6,7], 'Bondarenko' : [4,5,3,6,7], 'Sirov' : [10,9,8,6,2], 'Bilokon' : [7,8,4,7,10]}

def mean(lst):
    return sum(lst) / len(lst)
rating = sorted(students.keys(), key=lambda rating: mean(students[rating]))
print ('Good students:', rating[-1])
print ('Bad students:', rating[0])
