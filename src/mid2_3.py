import random
x = random.randrange(1,101)
guess = True;
count  = 0;
while(guess):
    guess_num = int(input("guess number(1-100): "))
    if (guess_num < x):
        print('up')
        count += 1
        guess = True        
    elif (guess_num > x):
        print('down')
        count += 1
        guess = True
    else:
        count += 1
        print('you got the correct number! you tried', count, 'guesses')
        guess = False