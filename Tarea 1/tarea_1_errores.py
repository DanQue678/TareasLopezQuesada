import math
# import random


def PrimeOrNot(p):
    result = True
    i = 2
    while i <= math.sqrt(p):
        if p % i == 0:
            result = False
            break
        i += 1
    return p, result

# print(PrimeOrNot(random.randint(2,10000000)))
