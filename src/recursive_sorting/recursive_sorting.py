# TO-DO: complete the helpe function below to merge 2 sorted arrays
import math
import random
import sys

print(sys.getrecursionlimit())

def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    arrAIndex = 0 
    arrBIndex = 0 
    #print(f'->{elements}')
    #print(f'---->{merged_arr}')



    if arrA[len(arrA) - 1] < arrB[len(arrB) - 1]:
        arrA.append(math.inf)
    else:
        arrB.append(math.inf)

    for i in range(len(merged_arr)):

        if arrA[arrAIndex] < arrB[arrBIndex]:
            merged_arr[i] = arrA[arrAIndex]
            arrAIndex += 1

        else:
            merged_arr[i] = arrB[arrBIndex]
            arrBIndex += 1
    
    return merged_arr

print(merge([1,3,5,7,9,12], [2,4,6,8,10]))


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) == 1 :
        return arr

    leftArr = arr[:len(arr)//2]
    rightArr = arr[len(arr)//2:]

    return merge(merge_sort(leftArr), merge_sort(rightArr))


for i in range(10):
    list = random.sample(range(1,100),50)

print(list)
print(merge_sort(list))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
