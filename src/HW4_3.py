import re
infile = open('emaillist.txt', 'r')
count = 0;
for filename in infile:
    match = re.findall(r'\S+gmail.com$', filename)
    if bool(match) == True:
        count += 1
print ("number of gmail address:", count)
infile.close()

infile = open('emaillist.txt', 'r')
count = 0
for filename in infile:
    match = re.findall(r'\S+.fr$', filename)
    if bool(match) == True:
        count += 1
print ("number of french emails:", count)
infile.close()

infile = open('emaillist.txt', 'r')
count = 0
for filename in infile:
    match = re.findall(r'^\w[a-zA-Z.]+@\w[a-zA-Z.]+$', filename)
    if bool(match) == True:
        count += 1
print ("number of email with only alphabet:", count)
infile.close()

infile = open('emaillist.txt', 'r')
count = 0
for filename in infile:
    match = re.findall(r'^\S+@\S+\w[.]+\S+\w[.]+\S', filename)
    if bool(match) == True:
        count += 1
print ("number of email that has two dots in domain:", count)
infile.close()