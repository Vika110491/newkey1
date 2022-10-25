#Задание 3
#Вспоминаем работу с файлом. Есть файл, в котором много англоязычных текстовых строк. Считаем частоту встретившихся слов в файле, но через функции и map, без единого цикла!





import re
from itertools import zip_longest

dict_result = {}
info = open('test.txt', 'r').read().lower()
words_k = re.findall(r'\w+', info)
words_k. sort()
words_count = []
dict_result = dict(zip_longest(words_k, words_count, fillvalue=0))

def word_match(word):
    if word in dict_result.keys():
        dict_result[word] = dict_result.get(word) + 1
    return dict_result

result = list(map(word_match, words_k))[0]

print(result)
