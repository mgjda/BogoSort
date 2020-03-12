import random

def isSorted(tab):
    n = len(tab)
    if n == 1 or n == 0:
        return True
    return tab[0] <= tab[1] and isSorted(tab[1:])


def bogosort(tab):
    while isSorted(tab) == False:
       random.shuffle(tab)
    return tab