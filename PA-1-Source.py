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
import random
import time


# generates random numbers and stores them in a dictionary
def generate_nums():
    num_dict = {}

    # range is the number of trials being conducted
    for i in range(1):
        # generates random numbers between randint(min_num, max_num)
        a = random.randint(1, 999999)
        b = random.randint(1, 999999)

        # adds the randomly generated numbers to the dictionary
        num_dict.update({a: b})

    return num_dict


# preprocessing to ensure a and b are positive and handles for the case where a or b == 0 or 1
def preprocess(a, b):
    a = abs(a)
    b = abs(b)

    # flag returns 1 if 1 is detected in a or b
    if a is 1 or b is 1:
        flag = 1

    # flag returns 0 if 0 is detected in a or b, overwrites with 0 if 1 was already found
    if a is 0 or b is 0:
        flag = 0

    # else, the value of flag doesn't matter. 2 is an arbitrary return value
    else:
        flag = 2

    return a, b, flag


# brute force algorithm beginning from 1 and incrementing upward
def bf_v1(a, b):
    start_time = time.perf_counter_ns()
    # pre-processing to ensure numbers are positive.
    # f is a flag that returns 0 if a or b is 0, and returns 1 if a or b is 1
    a, b, f = preprocess(a, b)

    # returns 0 or 1 if either of those numbers are detected in inputs
    if f is 0 or f is 1:
        stop_time = time.perf_counter_ns()
        end_time = (stop_time - start_time)
        return f, end_time

    # if the numbers a and b are the same, returns a as gcd
    if a is b:
        stop_time = time.perf_counter_ns()
        end_time = (stop_time - start_time)
        return a, end_time

    # detects which number is larger/smaller
    if a > b:
        big_num = a
        small_num = b
    else:
        big_num = b
        small_num = a

    # loop: when it finds a factor for big_num, it checks to see if it's also a factor for small_num
    for i in range(small_num):

        # if (i+1) is a factor for big_num
        if big_num % (i+1) is 0:

            # if (i+1) is a factor for small_num
            if small_num % (i+1) is 0:
                gcd = (i + 1)

    stop_time = time.perf_counter_ns()
    end_time = (stop_time - start_time)
    return gcd, end_time


# brute force algorithm beginning from the smaller input and decrementing downward
def bf_v2(a, b):
    start_time = time.perf_counter_ns()

    # pre-processing to ensure numbers are positive.
    # f is a flag that returns 0 if a or b is 0, and returns 1 if a or b is 1
    a, b, f = preprocess(a, b)

    # returns 0 or 1 if 0 or 1 are detected in inputs
    if f is 0 or f is 1:
        stop_time = time.perf_counter_ns()
        end_time = (stop_time - start_time)
        return f, end_time

    # lists to track all of big_num's factors and for all of small_num's factors
    big_list = []
    small_list = []

    # assigns the larger value to big_num and the smaller to small_num
    if a > b:
        big_num = a
        small_num = b
    else:
        big_num = b
        small_num = a

    length = small_num

    # decrements all numbers from small_num down to 1.
    for i in range(length):

        # if big_num / current iteration is evenly divisible
        if (big_num % small_num) is 0:

            # adds to the list of big_num's factors
            big_list.append(int(small_num))

        # decrements count
        small_num -= 1

    small_num = length

    # iterates all numbers from small_num through 1. adds factors to small_num's list
    for i in range(length):

        # if small num / current iteration is evenly divisible
        if (small_num % length) is 0:

            # adds to the list of small_num's factors
            small_list.append(int(length))
        length -= 1

    gcd = None

    # checks every item in the list of big_num's factors. This is in sequential order
    for item in big_list:

        # if that number is found in the list of small_num's factors, updates gcd with new value
        if item in small_list:
            gcd = item
            stop_time = time.perf_counter_ns()
            end_time = (stop_time - start_time)
            return gcd, end_time

    if gcd is None:
        gcd = 1

    stop_time = time.perf_counter_ns()
    end_time = (stop_time - start_time)
    return gcd, end_time


# the original version of euclid's algorithm using division
def euclid_gcd(a, b):
    start_time = time.perf_counter_ns()
    # pre-processing to ensure numbers are positive.
    # f is a flag that returns 0 if a or b is 0, and returns 1 if a or b is 1
    a, b, f = preprocess(a, b)

    # returns 0 or 1 if either of those numbers are detected in inputs
    if f is 0 or f is 1:
        stop_time = time.perf_counter_ns()
        end_time = (stop_time - start_time)
        return f, end_time

    # if the numbers a and b are the same, returns a as gcd
    if a is b:
        stop_time = time.perf_counter_ns()
        end_time = (stop_time - start_time)
        return a, end_time

    r = None

    # while the remainder is not zero
    while r is not 0:

        # assigns q (quotient) with the integer part of a/b
        q = math.floor(a/b)
        
        # assigns r (remainder) with the product of the quotient and smaller number subtracted from the larger number
        r = a - (q*b)
        a = b
        b = r

    stop_time = time.perf_counter_ns()
    end_time = (stop_time - start_time)
    # when r = 0, a is gcd
    return a, end_time


# the modified version of euclid's algorithm using subtraction
def euclid_modified_gcd(a, b):
    start_time = time.perf_counter_ns()

    # pre-processing to ensure numbers are positive.
    # f is a flag that returns 0 if a or b is 0, and returns 1 if a or b is 1
    a, b, f = preprocess(a, b)

    # returns 0 or 1 if either of those numbers are detected in inputs
    if f is 0 or f is 1:
        stop_time = time.perf_counter_ns()
        end_time = (stop_time - start_time)
        return f, end_time

    # if the numbers a and b are the same, returns a as gcd
    if a is b:
        stop_time = time.perf_counter_ns()
        end_time = (stop_time - start_time)
        return a, end_time

    # swaps a and b to ensure that a > b
    if b > a:
        temp = a
        a = b
        b = temp

    r = None

    while r is not 0:
        # remainder is a - b
        r = a - b

        # if quotient > 1, subtract again
        if r >= b:
            r = r - b

            # if quotient > 2, subtract again
            if r >= b:
                r = r - b

                # if quotient > 3, apply division algorithm
                if r >= b:
                    r = a - (b * math.floor((a/b)))

        a = b
        b = r

    # when r = 0, a is gcd
    stop_time = time.perf_counter_ns()
    end_time = (stop_time - start_time)
    return a, end_time


def run_algorithms(num_dict):

    # iterates through dictionary of randomized values
    for item in num_dict:
        # a is the number stored in the dicts key
        a = item

        # b is the number stored in the dicts value
        b = num_dict[item]

        # calls the 4 different euclidean algorithms using a and b as arguments
        gcd_1, time_1 = bf_v1(a, b)
        gcd_2, time_2 = bf_v2(a, b)
        gcd_3, time_3 = euclid_gcd(a, b)
        gcd_4, time_4 = euclid_modified_gcd(a, b)
        print(gcd_1, time_1)
        print(gcd_2, time_2)
        print(gcd_3, time_3)
        print(gcd_4, time_4)


if __name__ == '__main__':
    num_dict = generate_nums()
    run_algorithms(num_dict)



