import math
import random
area = 0.00
total_area = 0.00
list =[]
for i in range(2):
    list.append(random.uniform(0,1))
distance = math.sqrt(list[0]*list[0]+list[1]*list[1])
if distance <=1:
    print('it is in circle area')
else:
    print('it is out of circle')
i = 0
while i <= 1:
    j = 0
    while j <=1:
        if math.sqrt(i*i+j*j) <= 1:
            area += 1
        total_area += 1
        j += 0.01
    i +=0.01       
pi = 4 * area/total_area
print(pi)
# to have more accurate result, float digit should be counted more.