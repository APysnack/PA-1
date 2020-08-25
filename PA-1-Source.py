'''
Course: CSC 332-501
Programming Assignment 1
Assigned: 08/24/2020
Due Date: 08/31/2020

Contributors:
Armstrong, Sarah
Ibrahim, Mohammed
Nguyen, Brandon
Pysnack, Alan
'''
import math


def preprocess(a, b):
    a = abs(a)
    b = abs(b)
    if a is 1 or b is 1:
        flag = 1
    if a is 0 or b is 0:
        flag = 0
    else:
        flag = 2
    return a, b, flag


def bf_gcd_down(a, b):
    # pre-processing to ensure numbers are positive.
    # f is a flag that returns 0 if a or b is 0, and returns 1 if a or b is 1
    a, b, f = preprocess(a, b)

    big_list = []
    small_list = []

    # returns 0 or 1 if either of those numbers are detected in inputs
    if f is 0 or f is 1:
        return f

    if a > b:
        big_num = a
        small_num = b
    else:
        big_num = b
        small_num = a

    length = (small_num - 1)

    for i in range(length):
        if (big_num % length) is 0:
            big_list.append(int((big_num / length)))
        length -= 1

    length = (small_num - 1)

    for i in range(length):
        if (small_num % length) is 0:
            small_list.append(int((small_num / length)))
        length -= 1

    for item in big_list:
        if item in small_list:
            gcd = item

    return gcd


def bf_gcd_up(a, b):
    # pre-processing to ensure numbers are positive.
    # f is a flag that returns 0 if a or b is 0, and returns 1 if a or b is 1
    a, b, f = preprocess(a, b)

    # returns 0 or 1 if either of those numbers are detected in inputs
    if f is 0 or f is 1:
        return f

    if a > b:
        big_num = a
        small_num = b
    else:
        big_num = b
        small_num = a

    length = small_num

    for i in range(length):
        if big_num % (i+1) is 0:
            if small_num % (i+1) is 0:
                gcd = (i + 1)

    return gcd


# the original version of euclid's algorithm using division
def euclid_gcd(a, b):
    # pre-processing to ensure numbers are positive.
    # f is a flag that returns 0 if a or b is 0, and returns 1 if a or b is 1
    a, b, f = preprocess(a, b)

    # returns 0 or 1 if either of those numbers are detected in inputs
    if f is 0 or f is 1:
        return f

    r = None

    # pre-processing. Returns the value of zero if either a or b is zero
    if a is 0 or b is 0:
        return 0

    if a is 1 or b is 1:
        return 1

    # while the remainder is not zero
    while r is not 0:

        # assigns q (quotient) with the integer part of a/b
        q = math.floor(a/b)
        
        # assigns r (remainder) with the product of the quotient and smaller number subtracted from the larger number
        r = a - (q*b)
        a = b
        b = r

    return a


# the modified version of euclid's algorithm using subtraction
def euclid_modified_gcd(a, b):
    # pre-processing to ensure numbers are positive.
    # f is a flag that returns 0 if a or b is 0, and returns 1 if a or b is 1
    a, b, f = preprocess(a, b)

    # returns 0 or 1 if either of those numbers are detected in inputs
    if f is 0 or f is 1:
        return f

    if b > a:
        temp = a
        a = b
        b = temp

    r = None

    while r is not 0:
        r = a - b
        if r > b:
            r = r - b
            if r > b:
                r = r - b
                if r > b:
                    r = a - b * math.floor((a/b))
        a = b
        b = r

    return a


if __name__ == '__main__':
    euclid_modified_gcd(0, 290)