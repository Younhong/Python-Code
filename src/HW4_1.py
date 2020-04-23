def decrypt(s, code_book):
    str = "" 
    for letters in s:
        for i in range(len(code_book)):
            if code_book[i][1] == letters:
                str += code_book[i][0]
    return str
infile = open('secret_code_all.txt','r')
outfile = open('original_message_all.txt','w')
lines = infile.readlines()
code_book = [('k','a'), (' ','b'), ('y','c'), ('.','d'), ('t','e'), ('?','f'), ('b','g'), ('i','h'), ('w','i'), ('?','j'),
             ('u','k'), ('~','l'), ('g','m'), ('p','n'), (',','o'), ('e','p'), ('o','q'), ('r','r'), ('m','s'), ('s','t'), 
             ('?','u'), ('h','v'), ('f','w'), ('?','x'), ('n','y'), ('?','z'), ('d',' '), ('l',','), ('q','.'), ('a','~')]
for i in range(len(lines)):
    originalcode = decrypt(lines[i], code_book)
    outfile.write(originalcode)
    outfile.write("\n")
outfile.close()
infile.close()