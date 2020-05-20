# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # by replacing the zeros in the array, the array doesn't have to get re-created everytime you want to add a value to the merged_arr
    # could have used the below arr
    # merged_arr = []

    a = 0 # pointer for arrA
    b = 0 # pionter for arrB

    # This loops over every element in the merged_arr
    # For every element, run the comparisons, place them accordingly into merged_arr 
    for i in range(0, elements):
    # accounts for when you have reached the end of each array
    # 
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
            
        
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
            
    # accounts for value comparison of arrA and arrB and sorts accordingly
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
            

        else:
            merged_arr[i] = arrB[b]
            b += 1
            

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here

       # $%$Start
    if len(arr) > 1:
        left = merge_sort(arr[0: len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        arr = merge(left, right)   # merge() defined later
    # $%$End

   
    # if len(arr) > 1:
    #     mid = len(arr) // 2
    #     arrA = arr[:mid]
    #     arrB = arr[mid:]
        # separted into arrA and arrB

        # divides until reaches one element in the list
        # merge_sort(arrA) 
        # merge_sort(arrB)

        # arr = merge(arrA, arrB) 

    return arr
        
       

def merge_in_place(arr, start, mid, end):
	# start2 is the first element in the right
	# half of the list
    start2 = mid + 1
    # If the two halves we're merging are already
	# sorted, no need to do anything
    if arr[mid] <= arr[start2]:
        return
    # Two pointers to maintain start
    # of both arrays to merge
    while start <= mid and start2 <= end:

        # If element 1 is in right place
        if arr[start] <= arr[start2]:
            start += 1

        else:
            value = arr[start2]
            index = start2

            # Shift all the elements between element 1
            # element 2, right by 1.
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value

            # Update all the pointers
            start += 1
            mid += 1
            start2 += 1
    return arr
			
	# we don't return anything in in-place functions
	# since we're directly mutating the input array

def merge_sort_in_place(arr, l, r):
    if l < r:
        # Same as (l + r) / 2, but avoids overflow
        # for large l and r
        # this finds the middle of l and r not necessarily the middle of the arr
        m = l + (r - l) // 2

        # Sort first and second halves
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)

        merge_in_place(arr, l, m, r)

    return arr



# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
