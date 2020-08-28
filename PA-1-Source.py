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
    # sets the range of numbers generated and the number of elements desired
    list_range = 1000
    list_elements = 1000

    # generates lists of a and b values
    a_list = random.sample(range(list_range), list_elements)
    b_list = random.sample(range(list_range), list_elements)

    return a_list, b_list, list_elements


# preprocessing to ensure a and b are positive and handles for the case where a or b == 0 or 1
def preprocess(a, b):
    a = abs(a)
    b = abs(b)

    # flag returns 1 if 1 is detected in a or b
    if a == 1 or b == 1:
        flag = 1

    # flag returns 0 if 0 is detected in a or b, overwrites with 0 if 1 was already found
    if a == 0 or b == 0:
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
    if f == 0 or f == 1:
        stop_time = time.perf_counter_ns()
        end_time = (stop_time - start_time)
        return f, end_time

    # if the numbers a and b are the same, returns a as gcd
    if a == b:
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
    if f == 0 or f == 1:
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
        if (big_num % small_num) == 0:

            # adds to the list of big_num's factors
            big_list.append(int(small_num))

        # decrements count
        small_num -= 1

    small_num = length

    # iterates all numbers from small_num through 1. adds factors to small_num's list
    for i in range(length):

        # if small num / current iteration is evenly divisible
        if (small_num % length) == 0:

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
    if f == 0 or f == 1:
        stop_time = time.perf_counter_ns()
        end_time = (stop_time - start_time)
        return f, end_time

    # if the numbers a and b are the same, returns a as gcd
    if a == b:
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
    if f == 0 or f == 1:
        stop_time = time.perf_counter_ns()
        end_time = (stop_time - start_time)
        return f, end_time

    # if the numbers a and b are the same, returns a as gcd
    if a == b:
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

# writes the max, min, median, and avg time for an instance to a csv file
def write_stats(min, max, avg, median, fname):

    with open(fname, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Statistics', 'Nanoseconds'])
        writer.writerow(['Maximum Time', max])
        writer.writerow(['Minimum Time', min])
        writer.writerow(['Average Time', avg])
        writer.writerow(['Median Time', median])


# runs the dictionary of numbers through brute force algorithm 1 and writes to csv files
def run_bf_v1(a_list, b_list, count):
    # list keeps track of algorithm run_time
    time_list = []
    file_name = 'BF_v1_Results.csv'
    stat_file_name = 'BF_v1_Statistics.csv'
    max_time, total_time = 0, 0

    # an upper bound of min_time
    min_time = 300000

    # creating a csv file for the time trials
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        # writes the top row (headers) of csv file
        writer.writerow(['Number One', 'Number Two', 'Their GCD', 'Time Spent (nanoseconds)'])

        # iterates list_a and list_b and finds a gcd(a, b) using the bf_v1 algorithm
        for i in range(count):
            gcd, run_time = bf_v1(a_list[i], b_list[i])
            writer.writerow([a_list[i], b_list[i], gcd, run_time])

            # tracking min, max, and accumulating total time
            if run_time > max_time:
                max_time = run_time

            if run_time < min_time:
                min_time = run_time

            total_time += run_time

            time_list.append(run_time)

    # sorts the time list to find the median value
    time_list.sort()

    # if number of elements is even, gets the average of the 2 middle-most elements as median
    if (count % 2) == 0:
        middle_1 = math.floor(count/2)
        middle_2 = (math.floor(count/2) + 1)
        median = ((time_list[middle_1] + time_list[middle_2]) / 2)

    # if number of elements is odd, uses n/2 to find median
    else:
        middle = math.floor(count/2)
        median = time_list[middle]

    avg_time = (total_time / count)

    # writes the min, max, avg, median stats to a csv file
    write_stats(min_time, max_time, avg_time, median, stat_file_name)


# runs the dictionary of numbers through brute force algorithm 2 and writes to csv files
def run_bf_v2(a_list, b_list, count):
    file_name = 'BF_v2_Results.csv'
    stat_file_name = 'BF_v2_Statistics.csv'
    max_time, total_time = 0, 0

    # list to keep track of each calculation
    time_list = []

    # an upper bound of min_time
    min_time = 300000

    # creating a csv file for the time trials
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        # writes headers for the csv file
        writer.writerow(['Number One', 'Number Two', 'Their GCD', 'Time Spent (nanoseconds)'])

        # iterates list_a and list_b and finds a gcd(a, b) using the bf_v2 algorithm
        for i in range(count):
            gcd, run_time = bf_v2(a_list[i], b_list[i])
            writer.writerow([a_list[i], b_list[i], gcd, run_time])

            # tracks min, max times and overall times
            if run_time > max_time:
                max_time = run_time

            if run_time < min_time:
                min_time = run_time

            total_time += run_time

            time_list.append(run_time)

    # sorts list of times
    time_list.sort()

    # for even number of elements, gets avg of 2 middle-most elements as median
    if (count % 2) == 0:
        middle_1 = math.floor(count / 2)
        middle_2 = (math.floor(count / 2) + 1)
        median = ((time_list[middle_1] + time_list[middle_2]) / 2)

    # for odd number of elements, uses n/2 as median
    else:
        middle = math.floor(count / 2)
        median = time_list[middle]

    avg_time = (total_time / count)

    # writes the min, max, avg, median stats to a csv file
    write_stats(min_time, max_time, avg_time, median, stat_file_name)


# runs the dictionary of numbers through original euclidean algorithm and writes to csv files
def run_euclid_gcd(a_list, b_list, count):
    file_name = 'OE_Results.csv'
    stat_file_name = 'OE_Statistics.csv'

    max_time, total_time = 0, 0
    time_list = []

    # an upper bound of min_time
    min_time = 300000

    # creating a csv file for the time trials
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        # writes headers into the csv file
        writer.writerow(['Number One', 'Number Two', 'Their GCD', 'Time Spent (nanoseconds)'])

        # iterates list_a and list_b and finds a gcd(a, b) using the original euclid algorithm
        for i in range(count):
            gcd, run_time = euclid_gcd(a_list[i], b_list[i])
            writer.writerow([a_list[i], b_list[i], gcd, run_time])

            # tracks max, min, and aggregates total time
            if run_time > max_time:
                max_time = run_time

            if run_time < min_time:
                min_time = run_time

            total_time += run_time

            time_list.append(run_time)

    # sorts the list of times to find the median
    time_list.sort()

    # for even number of elements, gets avg of 2 middle-most elements as median
    if (count % 2) == 0:
        middle_1 = math.floor(count / 2)
        middle_2 = (math.floor(count / 2) + 1)
        median = ((time_list[middle_1] + time_list[middle_2]) / 2)

    # for odd number of elements, uses floor of n/2 as median
    else:
        middle = math.floor(count / 2)
        median = time_list[middle]

    avg_time = (total_time / count)

    # writes the min, max, avg, median stats to a csv file
    write_stats(min_time, max_time, avg_time, median, stat_file_name)


# runs the dictionary of numbers through modified euclidean algorithm and writes to csv files
def run_euclid_modified(a_list, b_list, count):
    file_name = 'SE_Results.csv'
    stat_file_name = 'SE_Statistics.csv'
    max_time, total_time = 0, 0

    # list of times for each gcd trial
    time_list = []

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

            time_list.append(run_time)

    # sorts list of times - pre-processing to find median
    time_list.sort()

    # for even number of elements, gets avg of 2 middle-most elements as median
    if (count % 2) == 0:
        middle_1 = math.floor(count / 2)
        middle_2 = (math.floor(count / 2) + 1)
        median = ((time_list[middle_1] + time_list[middle_2]) / 2)

    # if odd number of elements, uses floor of n/2 as median
    else:
        middle = math.floor(count / 2)
        median = time_list[middle]

    avg_time = (total_time / count)

    # writes all time statistics to a csv file
    write_stats(min_time, max_time, avg_time, median, stat_file_name)


def compare_algorithms():
    # the names of the csv files with the time trial data
    bfv1 = 'BF_v1_Results.csv'
    bfv2 = 'BF_v2_Results.csv'
    oe = 'OE_Results.csv'
    se = 'SE_Results.csv'

    # string representations - used for output in the .txt file
    v1txt = 'brute-force (v1)'
    v2txt = 'brute-force (v2)'
    oetxt = 'the original version of Euclid'
    setxt = 'the second version of Euclid'

    # calls function to compare the results of 2 csv files
    compare_files(bfv1, bfv2, v1txt, v2txt)
    compare_files(oe, bfv1, oetxt, v1txt)
    compare_files(oe, bfv2, oetxt, v2txt)
    compare_files(se, oe, setxt, oetxt)
    compare_files(se, bfv1, setxt, v1txt)
    compare_files(se, bfv2, setxt, v2txt)


def compare_files(csvf1, csvf2, f_name_1, f_name_2):
    count_1, count_2, tot_tsaved_1, tot_tsaved_2, = 0, 0, 0, 0

    # a list of the times in each csv file
    time_list_1 = []
    time_list_2 = []

    # opens csv file 1 and stores the list of times
    with open(csvf1, 'r') as file_1:
        reader_1 = csv.reader(file_1)
        next(reader_1)
        for line in reader_1:
            time_list_1.append(int(line[3]))

    # opens csv file 2 and stores the list of times
    with open(csvf2, 'r') as file_2:
        reader_2 = csv.reader(file_2)
        next(reader_2)
        for line in reader_2:
            time_list_2.append(int(line[3]))

    # iterates through each item in the lists
    # compares the time algorithm 1 took to compute gcd with algorithm 2
    for i, time_1 in enumerate(time_list_1):

        # if algorithm 1 took less time than algorithm 2
        if time_1 < time_list_2[i]:

            # increments count of times algorithm 1 outperformed + 1
            count_1 += 1

            # calculates the amount of time saved and accumulates total time saved
            t_saved_1 = (time_list_2[i] - time_1)
            tot_tsaved_1 += t_saved_1

        # else if the time algorithm 1 and algorithm 2 was the same, pass to next element
        elif time_1 == time_list_2[i]:
            pass

        # else: algorithm 2 outperformed algorithm 1
        else:
            # increments count_2: the number of times algorithm 2 outperformed
            count_2 += 1

            # calculates the amount of time saved and accumulates total time saved
            t_saved_2 = (time_1 - time_list_2[i])
            tot_tsaved_2 += t_saved_2

    # if algorithm 1 outperformed more times than algorithm 2:
    if count_1 > count_2:

        # count_1 should never == 0 but I added this in to prevent divide by zero error
        if count_1 == 0:
            print('db0 error')
            return

        # concatenates the output string in the case that algorithm 1 outperforms
        str_1 = 'Out of 1,000 pairs of integers, ' + f_name_1 + ' outperformed '
        str_2 = f_name_2 + ' in ' + str(count_1) + ' pairs; and the average time '
        str_3 = 'saved for these ' + str(count_1) + ' pairs of integers was '
        str_4 = str(round(tot_tsaved_1 / count_1)) + ' nanoseconds'
        str_to_print = str_1 + str_2 + str_3 + str_4

    else:

        # count_2 should never == 0 but I added this in to prevent divide by zero error
        if count_2 == 0:
            print('db0 error')
            return

        # concatenates the output string in the case that algorithm 2 outperforms
        str_1 = 'Out of 1,000 pairs of integers, ' + f_name_2 + ' outperformed '
        str_2 = f_name_1 + ' in ' + str(count_2) + ' pairs; and the average time '
        str_3 = 'saved for these ' + str(count_2) + ' pairs of integers was '
        str_4 = str(round(tot_tsaved_2 / count_2)) + ' nanoseconds'
        str_to_print = str_1 + str_2 + str_3 + str_4

    # Appends/writes .txt file with the appropriate string
    append_file(str_to_print)


def append_file(str):
    # name of text file to be written/appended
    fname = 'Conclusions.txt'

    # writes string to text file
    with open(fname, 'a') as f:
        f.write(str)
        f.write('\n')

# main function
if __name__ == '__main__':
    # generates 2 lists of random numbers for a and b values, and the length of the lists
    a_list, b_list, count = generate_nums()

    # executes the algorithms and writes their individual stats to csv files
    run_algorithms(a_list, b_list, count)

    # outputs txt file comparing the stats of csv files
    compare_algorithms()

