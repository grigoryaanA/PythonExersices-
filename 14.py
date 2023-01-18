# Write a function that fills in a list of random numbers in the domain specified by the user. The function must take
# two arguments: the beginning of the range and its end while returning nothing. The output of the list item values
# must occur in the main part of the function.

from random import randint

def randomize(begin=0, end=10, size=10):
    list = []

    for i in range(size):
        list.append(randint(begin, end))

    print(list)

