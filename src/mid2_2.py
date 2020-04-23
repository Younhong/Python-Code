import math
number = input("input number?: ")
sum = 0
for i in range(len(number)):
    if number[i].isdigit():
        sum += int(number[i])
print('sum of all digit numbers in', number, 'is', sum)