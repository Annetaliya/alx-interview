#!/usr/bin/python3

''' minimum operations'''


def minOperations(n):
    '''
    calculate the fewest number of operations
    needed to achieve exactlt n 'H' character
    '''

    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        if n % factor == 0:
            operations += factor
            n //= factor
        else:
            factor += 1

    return operations
