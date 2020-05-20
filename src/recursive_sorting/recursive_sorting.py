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
    # Your code here
    start2 = mid + 1

    if arr[mid] <= arr[start2]:
        return
    
    while start <= mid and start2 <= end:
        # first element is in correct place
        if arr[start] <= arr[start2]:
            start += 1

        else:
            value = arr[start2]
            index = start2

            while index != start:
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value

            start += 1
            mid += 1
            start2 += 1

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    if l <= r:
        mid = 1 + (r - 1) // 2

        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid + 1, r)

        merge_in_place(arr, l, mid, r)
        




    # pivot = arr[l]

    # i = l + 1
    # j = l + 1

    # while j <= r:
    #     if arr[j] <= pivot:
    #         arr[j], arr[i] = arr[i], arr[j]
        
    #     j += 1
    
    # arr[l], arr[i - 1] = arr[i-1], arr[l]

   



    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
