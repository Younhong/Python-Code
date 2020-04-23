def reverse_words(s):
    newWord = ''
    delimeter = ' '
    list = string.split(delimeter)
    for word in list:
        for i in range (len(word)-1, -1, -1):
            newWord += word[i]
        newWord += ' '
    return newWord
string = input("Enter input: ")
print(reverse_words(string))