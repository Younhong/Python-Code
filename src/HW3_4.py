import datetime
import math

string1 = input("when did you join Handong? ")
string2 = input("when do you expect to graduate? ")
delimiter = string1[4]
list1 = string1.split(delimiter);
list2 = string2.split(delimiter);
entrance_year = datetime.date(int(list1[0]),int(list1[1]),int(list1[2]))
graduate_year = datetime.date(int(list2[0]),int(list2[1]),int(list2[2]))
today = datetime.date.today()
print ('you spent', (today - entrance_year).days, 'days in handong')
print ((graduate_year - today).days, 'days left until graduation')
print ('you are at', round(10 * (today - entrance_year).days / float((graduate_year - entrance_year).days),2), 'point out of 10 until graduation, cheers!')