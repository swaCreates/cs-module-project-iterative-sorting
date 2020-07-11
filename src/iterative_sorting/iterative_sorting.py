# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1): # going from first to last el in list
        cur_index = i # tracking/marking the current el we are on
        smallest_index = cur_index # just re-referencing the current el
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        # creating a abstract second list of all RHS elements to curr element on LHS
        for j in range(cur_index + 1, len(arr)):
            if arr[smallest_index] > arr[j]: # if LHS > RHS
                smallest_index = j # change current smallest element to new smallest element

        # TO-DO: swap
        # Your code here
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
# Your code here
# go through entire list
    is_swapped = True
    while is_swapped:
        is_swapped = False # will help stop the loop if the swaps did not happen
        for i in range(0, len(arr) -1):
            if arr[i] > arr[i+1]: # if LHS > RHS
                arr[i], arr[i+1] = arr[i+1], arr[i] #swapping sides
                is_swapped = True
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
