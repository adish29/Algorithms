""""
file: sortingTest.py
description: Implement merge sort, bucket sort and insertion sort
and compare their time complexities.
language: python3
author: Adish Pathare, ap5988@rit.edu
"""

import math
from numpy import random as np
import time


def _merge(left, right):
    """
    Implements merge
    :return: result
    """
    # the sorted left + right will be stored in result
    result = []
    leftIndex, rightIndex = 0, 0

    # loop through until either the left or right list is exhausted
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] <= right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1

    # take the un-exhausted list and extend the remainder onto the result
    if leftIndex < len(left):
        result.extend(left[leftIndex:])
    elif rightIndex < len(right):
        result.extend(right[rightIndex:])

    return result


def mergeSort(data):
    """
    Implements merge sort algorithm
    :return: data
    """
    # an empty list, or list of 1 element is already sorted
    if len(data) < 2:
        return data
    else:
        # split the data into left and right halves
        left, right = data[:len(data) // 2], data[len(data) // 2:]

        # return the merged recursive mergeSort of the halves
        return _merge(mergeSort(left), mergeSort(right))


def insertionSort(data):
    """
    Implements insertion sort algorithm
    :return: data
    """
    # The element at first position is considered sorted.
    for i in range(1, len(data)):
        # used to access elements at previous positions.
        j = i - 1
        # element at current position
        current_element = data[i]
        while j >= 0 and current_element < data[j]:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = current_element
    return data


def bucketSort(data):
    """
    Implements bucket sort algorithm
    :return: data
    """
    n = len(data)
    b = []
    result = []
    for i in range(n):
        # b is an empty list of size n
        b.append([])
    for i in range(n):
        b[math.floor(n * data[i])].append(data[i])
    for i in range(n):
        # use insertion sort to sort individual bucket
        ans = insertionSort(b[i])
        result = result + ans

    return result



def main():
    """
    The main function which has all the test cases
    :return: None
    """

    mean,sd = 0.5, 0.0001

    test1 = np.uniform(0,1,10)
    test2 = np.uniform(0,1,100)
    test3 = np.uniform(0,1,1000)
    test4 = np.uniform(0,1,10000)
    test5 = np.uniform(0,1,100000)

    test6 = np.normal(mean,sd,10)
    test7 = np.normal(mean, sd, 100)
    test8 = np.normal(mean, sd, 1000)
    test9 = np.normal(mean, sd, 10000)
    test10 = np.normal(mean, sd, 100000)

    print("Time(in sec) taken by merge sort on input of size 10000 and uniform distributed data")
    start_time = time.time()
    ans = mergeSort(test4)
    print(time.time() - start_time)
    print("Time(in sec) taken by bucket sort on input of size 10000 and uniform distributed data")
    start_time = time.time()
    ans = bucketSort(test4)
    print(time.time() - start_time)
    print("Time(in sec) taken by insertion sort on input of size 10000 and uniform distributed data")
    start_time = time.time()
    ans = insertionSort(test4)
    print(time.time() - start_time)
    print("Time(in sec) taken by merge sort on input of size 10000 and gaussian distributed data")
    start_time = time.time()
    ans = mergeSort(test9)
    print(time.time() - start_time)
    print("Time(in sec) taken by bucket sort on input of size 10000 and gaussian distributed data")
    start_time = time.time()
    ans = bucketSort(test9)
    print(time.time() - start_time)
    print("Time(in sec) taken by insertion sort on input of size 10000 and gaussian distributed data")
    start_time = time.time()
    ans = insertionSort(test9)
    print(time.time() - start_time)


if __name__ == '__main__':
    main()
