def reverse_sentence(s):
    newList = ''
    delimeter = ' '
    list = string.split(delimeter)
    for i in range(len(list)-1,-1,-1):
        newList += list[i]
        newList += ' '
    return newList
string = input("input sentence: ")
print(reverse_sentence(string))