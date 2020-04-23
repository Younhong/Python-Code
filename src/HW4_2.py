dic = {}
def word_dic(n, s):
    words = s.split()
    for word in words:
        # if word is in dictionary
        if word in dic:
            # if already appeared twice
            if ',' in dic[word]:
                dic[word] = '?'
            else:
                # if more than 3 times
                if dic[word] == '?':
                    dic[word] = '?'
                # if appeared only once
                else:
                    dic[word] += ', '
                    dic[word] += str(n)
        # if word does not exist in dictionary
        else:
            dic[word] = str(n)
    return dic
infile = open('text_lower.txt', 'r')
outfile = open('index.txt', 'w')
lines = infile.readlines()
for line in range(len(lines)):
    x = ""
    list = lines[line].split()
    for i in range(1, len(list)):
        x += list[i]
        x += " "
    word_dic(line, x)
for word in sorted(dic.keys()):
    if dic[word] is not '?':
        outfile.write(word)
        outfile.write(" : ")
        outfile.write(dic[word])
        outfile.write("\n")
outfile.close()
infile.close()