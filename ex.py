def merge(list, l, m, r):
    # l, m, r -> are indices in the array
    n1 = m - l + 1
    n2 = r - m 
    # m - l + 1 // r - m 

    LEFT = [0] * n1
    RIGHT = [0] * n2 

    # Copy the data to our temporary array/list LEFT and RIGHT

    for i in range(0, n1):
        LEFT[i] = list[l + i]

    for j in range(0, n2):
        RIGHT[j] = list[m + 1 + j]

    # merge the temp arrays back into the main list - [1..r]
    i = 0 # initial index of first subarray (sub list)
    j = 0 # initial index of second subarray (or sub list)
    k = l # initial index of the merged sub array

    while i < n1 and j < n2: 
        if LEFT[i] <= RIGHT[j]  :
            list[k] = LEFT[i]
            i += 1
        else:
            list[k] = RIGHT[j]
            j += 1
        
        k += 1

    # Copy the remaining elements of LEFT (array) if there are any
    while i < n1:
        list[k] = LEFT[i]
        i += 1
        k += 1

    # copy the remaining elements of RIGHT (array) if any
    while j < n2:
        list[k] = RIGHT[j]
        j += 1
        k += 1


# l is for the left index, r is for the index of the sub array to be sorted.
def merge_sort(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        merge(arr, l, m, r)
# testing code
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is")
for i in range(n):
    print("%d" % arr[i],end=" ")
 
merge_sort(arr, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % arr[i],end=" ")