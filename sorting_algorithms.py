## Sorting Algorithms, written from scratch
# I wrote these and many more in Java back in HS, but since it's been so
# long I thought it would be a good idea to impliment them in python
#Bubble sort, Insertion Sort, Merge Sort, Heap Sort, Quick Sort
import numpy as np
import %timeit

rand_array = np.random.randint(1,101,40)
print(rand_array)

#1. Bubble Sort, Recursive
# Time Complexity: Best O(n), Avg O(n^2) = worst
# Space Complexity: O(n)
# After writing this it turns out this isn't really how bubblesort works.
# Not sure what to call it though.
def bubble_sort(array):
    if(all(array[i] <= array[i + 1] for i in range(len(array)-1))):
        return array

    i = 0
    # print(array)
    while i < len(array)-1:
        if array[i+1] < array[i]:
            array[i], array[i+1] = array[i+1], array[i]
        i+=1
    bubble_sort(array)

bubble_sort(rand_array)

#1.5 Bubble Sort, non Recursive
# Time Completixity O(n^2)
# Space Complexity O(1)
def bubble_sort2(arr):
    for i in range(len(arr)):
        # Last i elements are already in place
        for j in range(0, len(arr)-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

bubble_sort2(rand_array)

%timeit bubble_sort(rand_array)
%timeit bubble_sort2(rand_array)
