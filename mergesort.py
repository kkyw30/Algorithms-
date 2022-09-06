def mergesort(arr):
    if len(arr) > 1:
        midpoint = len(arr) // 2
        left = arr[:midpoint]
        right = arr[midpoint:]

        # recursively sort the two halves
        mergesort(left)
        mergesort(right)

        j = k = 0
        for i in range(0,len(arr)):
            if len(left) > 0 and len(right) > 0:
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = left[k]
                    k += 1
            elif len(left) > 0:
                arr[i] = left[j] 
            elif len(right) > 0:
                arr[i] = right[k] 

    return arr 


# Testing 
test1 = [6, 3, 4, 2]
print(mergesort(test1)) 

test2 = [6,3]
print(mergesort(test2))
