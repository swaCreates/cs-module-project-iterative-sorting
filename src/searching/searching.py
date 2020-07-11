def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        curr = arr[i]
        if curr == target: # if curr val == target val
            return i #return index
        else: #move up in index
            i += 1

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here

    # setting pointers to the front and back of the arr
    head = 0
    tail = len(arr) - 1

    while head <= tail: # while head/tail !==
        mid = head + (tail - head) // 2 # finding the middle index of the arr

        if arr[mid] == target: # if whatever the middle val we start on == target val return it
            return mid #return index
        elif target < arr[mid]: #if target val is in lower half of arr
            tail = mid - 1 # disregard the entire RHS of arr & search left beginning from mid index again
        else: #if target val is in upper half of arr
            head = mid + 1 # disregard the entire LHS of arr & search right beginning from mid index again


    return -1  # not found
