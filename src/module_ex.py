import random as rand
def word_count(s):
    list = s.split()
    return len(list)
def word_shuffle(s):
    nwords = word_count(s)
    return " ".join(rand.sample(s.split(),nwords))
def word_ran_cap(s):
    return " ".join(rand.capitalize(s.split(),len(s)))