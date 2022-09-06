# function to find partition position 
def partition(arr, l, r):
  pivot = arr[r]
  i = l - 1
  
  for j in range(l, r):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]              # swap elements 
  arr[i+1], arr[r] = arr[r], arr[i+1]        # swap pivot element with greater element specified by i
  
  return i+1                                # return pivot position

# function to perform quicksort
def quicksort(arr, l, r):
  if l < r:
    pi = partition(arr, l, r)
    quicksort(arr, l, pi - 1)        # recursively call quicksort on left side of pivot
    quicksort(arr, pi + 1, r)        # recursively call quicksort on right side of pivot
    
# Test
data = [8, 5, 2, 1, 0, 9, 7]
quicksort(data, 0, size-1)
print(data) 
      
