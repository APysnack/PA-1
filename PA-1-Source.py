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
import csv


# generates random numbers and stores them in a dictionary
def generate_nums():
    list_range = 100
    list_elements = 10

    a_list = random.sample(range(list_range), list_elements)
    b_list = random.sample(range(list_range), list_elements)
    count = len(a_list)

    return a_list, b_list, count


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


# runs the dictionary through each version of the gcd algorithms
def run_algorithms(a_list, b_list, count):
    run_bf_v1(a_list, b_list, count)
    run_bf_v2(a_list, b_list, count)
    run_euclid_gcd(a_list, b_list, count)
    run_euclid_modified(a_list, b_list, count)


def write_stats(min, max, avg, median, fname):
    print('Write these to ' + fname + ':')
    print(min, max, avg, median)


# runs the dictionary of numbers through brute force algorithm 1 and writes to csv files
def run_bf_v1(a_list, b_list, count):
    file_name = 'BF_v1_Results.csv'
    stat_file_name = 'BF_v1_Statistics.csv'
    max_time, total_time = 0, 0
    occurrence_dict = {}

    # an upper bound of min_time
    min_time = 300000

    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Number One', 'Number Two', 'Their GCD', 'Time Spent (nanoseconds)'])

        for i in range(count):
            gcd, run_time = bf_v1(a_list[i], b_list[i])
            writer.writerow([a_list[i], b_list[i], gcd, run_time])

            if run_time > max_time:
                max_time = run_time

            if run_time < min_time:
                min_time = run_time

            total_time += run_time

            if not occurrence_dict.get(run_time):
                occurrence_dict.update({run_time: 0})

            occurrence_dict[run_time] += 1

    median = max(occurrence_dict, key=occurrence_dict.get)
    avg_time = (total_time / count)
    write_stats(min_time, max_time, avg_time, median, stat_file_name)


# runs the dictionary of numbers through brute force algorithm 2 and writes to csv files
def run_bf_v2(a_list, b_list, count):
    file_name = 'BF_v2_Results.csv'
    stat_file_name = 'BF_v2_Statistics.csv'
    max_time, total_time = 0, 0
    occurrence_dict = {}

    # an upper bound of min_time
    min_time = 300000

    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Number One', 'Number Two', 'Their GCD', 'Time Spent (nanoseconds)'])

        for i in range(count):
            gcd, run_time = bf_v2(a_list[i], b_list[i])
            writer.writerow([a_list[i], b_list[i], gcd, run_time])

            if run_time > max_time:
                max_time = run_time

            if run_time < min_time:
                min_time = run_time

            total_time += run_time

            if not occurrence_dict.get(run_time):
                occurrence_dict.update({run_time: 0})

            occurrence_dict[run_time] += 1

    median = max(occurrence_dict, key=occurrence_dict.get)
    avg_time = (total_time / count)
    write_stats(min_time, max_time, avg_time, median, stat_file_name)


# runs the dictionary of numbers through original euclidean algorithm and writes to csv files
def run_euclid_gcd(a_list, b_list, count):
    file_name = 'OE_Results.csv'
    stat_file_name = 'OE_Statistics.csv'

    max_time, total_time = 0, 0
    occurrence_dict = {}

    # an upper bound of min_time
    min_time = 300000

    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Number One', 'Number Two', 'Their GCD', 'Time Spent (nanoseconds)'])

        for i in range(count):
            gcd, run_time = euclid_gcd(a_list[i], b_list[i])
            writer.writerow([a_list[i], b_list[i], gcd, run_time])

            if run_time > max_time:
                max_time = run_time

            if run_time < min_time:
                min_time = run_time

            total_time += run_time

            if not occurrence_dict.get(run_time):
                occurrence_dict.update({run_time: 0})

            occurrence_dict[run_time] += 1

    median = max(occurrence_dict, key=occurrence_dict.get)
    avg_time = (total_time / count)

    write_stats(min_time, max_time, avg_time, median, stat_file_name)


# runs the dictionary of numbers through modified euclidean algorithm and writes to csv files
def run_euclid_modified(a_list, b_list, count):
    file_name = 'SE_Results.csv'
    stat_file_name = 'SE_Statistics.csv'
    max_time, total_time = 0, 0
    occurrence_dict = {}

    # an upper bound of min_time
    min_time = 300000

    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Number One', 'Number Two', 'Their GCD', 'Time Spent (nanoseconds)'])

        for i in range(count):
            gcd, run_time = euclid_modified_gcd(a_list[i], b_list[i])
            writer.writerow([a_list[i], b_list[i], gcd, run_time])

            if run_time > max_time:
                max_time = run_time

            if run_time < min_time:
                min_time = run_time

            total_time += run_time

            if not occurrence_dict.get(run_time):
                occurrence_dict.update({run_time: 0})

            occurrence_dict[run_time] += 1

    median = max(occurrence_dict, key=occurrence_dict.get)
    avg_time = (total_time / count)
    write_stats(min_time, max_time, avg_time, median, stat_file_name)


# main function
if __name__ == '__main__':
    a_list, b_list, count = generate_nums()
    run_algorithms(a_list, b_list, count)

