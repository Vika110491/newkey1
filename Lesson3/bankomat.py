#Банкомат выдает сумму максимально возможными купюрами


print ('Ваш Банк' "\n" '''Доступные номиналы купюр 1000,500,200,100,50 грн''' "\n" '''Введите сумму''''')
def atm(value):
    rest = value
    result = ''
    var1000 = 0
    var500 = 0
    var200 = 0
    var100 = 0
    var50 = 0
    if (rest - 1000 >= 0):
        while True:
            rest = rest - 1000 
            if (rest >= 0):
                 var1000 = var1000 + 1
            else: 
                rest = rest + 1000
                break
            return rest
    if (rest - 500 >= 0):
        while True: 
            rest = rest - 500
            if (rest >= 0):
                var500 = var500 + 1
            else: 
                rest = rest + 500
                break
    if (rest - 200 >= 0):
        while True: 
            rest = rest - 200
            if (rest >= 0):
                var200 = var200 + 1
            else: 
                rest = rest + 200
                break
    if (rest - 100 >= 0):
        while True:
            rest = rest - 100
            if (rest >= 0):
                var100 = var100 + 1
                break
    if (rest - 50 >= 0):
        while True:
            rest = rest - 50
            if (rest >= 0):
                var50 = var50 + 1
                break
    result = str(var1000) + ' ' + str(var500) + ' ' + str(var200)  + ' ' + str(var100)  + ' ' + str(var50)
    return result
