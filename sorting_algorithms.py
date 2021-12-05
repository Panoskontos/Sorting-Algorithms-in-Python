'logic most basic sort is a nest loop that traverses the array for each element and swaping with the next element until it is sorted'
# bubble sort


def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# insertion sort
'''
logic we have to sublists   
sorted | ubsorted
take each element and move it to the sorted side and compare it until we find it's position
'''


def insertionSort(arr):
    for i in range(1, len(arr)):
        # for each value
        value = arr[i]
        # if previous value is bigger swap values until everything is sorted
        while arr[i-1] > value and i > 0:
            # swap values
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i = i - 1
    return arr


# -----------------------------------------------------------------
# merge sort
def mergeSort(arr):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr)//2
        # Dividing the array elements into 2 halves
        L = arr[:mid]
        R = arr[mid:]
        # Sorting the first half & second half
        mergeSort(L)
        mergeSort(R)

        # Compare Left and Right array and put the smallest to the array
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # checking if anything was left and copies them
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return
#  ------------------------------------------------------------------------------


# quick sort
'''
logic pick a pivot(first or last) if a number is lower go left if a number is greater go right
repeat (with first or last in left and right) until everything is sorted
'''
# --------------------------------------------------------


def quickSort(arr):
    # base case
    if len(arr) <= 1:
        return arr
    # create 3 arrays choose any pivot
    left, right, equal = [], [], []
    pivot = arr[0]
    # append according to pivot
    for i in arr:
        if i > pivot:
            right.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            left.append(i)
    # return result
    return quickSort(left) + equal + quickSort(right)


# -------------------------------------------------------------------------


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=' ')
    print()


# create array of size and random numbers
def create_array(size):
    import numpy as np
    randnums = np.random.randint(1, size, size)
    return randnums


# test our 4 sorting techniques
def benchmark():
    from time import time
    bubble_times = []
    insetion_times = []
    quick_times = []
    merge_times = []

    n = [10, 100, 1000, 10000, 100000]
    for size in n:

        a = create_array(size)
        t0 = time()
        bubbleSort(a)
        t1 = time()
        bubble_times.append(t1-t0)

        a = create_array(size)
        t0 = time()
        insertionSort(a)
        t1 = time()
        insetion_times.append(t1-t0)

        a = create_array(size)
        t0 = time()
        quickSort(a)
        t1 = time()
        quick_times.append(t1-t0)

        a = create_array(size)
        t0 = time()
        mergeSort(a)
        t1 = time()
        merge_times.append(t1-t0)

    print("\nn \t Bubble \t Insertion \t Quick  \t Merge")
    print(90 * "_")
    for i, size in enumerate(n):
        print(size, "\t",  "%0.5f" %
              bubble_times[i], "\t",  "%0.5f" %
              insetion_times[i], "\t", "%0.5f" % quick_times[i], "\t", "%0.5f" % merge_times[i])
    print("\n")


# ignore this! it was in order to test testing our algorithms
# arr = [12, 11, 13, 5, 6, 7]
# print("Given array is", end="\n")
# printList(arr)
# bubbleSort(arr)
# printList(arr)

benchmark()
