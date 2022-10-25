numbers = []
with open('numbers.txt', 'r') as f:
    items = f.read().split('\n')
    for i in items:
        numbers.append([int(n) for n in i.split(',')])
for nums in numbers:
    for num in range(1, nums[2]+1):
        if num % nums[0] == 0 and num % nums[1] == 0:
              print ('FB', end = ' ')
        elif num % nums[0] == 0:
            print('F', end = ' ')
        elif num % nums[1] == 0:
            print('B', end = ' ')
        else:
            print(num, end = ' ')


