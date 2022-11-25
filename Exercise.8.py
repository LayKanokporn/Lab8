#Lab 8 1630902656 Kanokporn Hudsree
def LinearSearch(array, n, k):

    for j in range(0, n):

        if (array[j] == k):

            return j

    return -1

 
array = [7,10,12,14,16,20,29,37]

k = 7
n = len(array)

result = LinearSearch(array, n, k)

if(result == -1):

    print("Element not found")

else:

    print("Element found at index: ", result)
def binarySearch(arr, k, low, high):
   
    while low <= high:
        mid = low + (high - low)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:

            low = mid + 1
        else:

            high = mid - 1
    return -1

arr = [7,10,12,14,16,20,29,37]

k = 8
result = binarySearch(arr, k, 0, len(arr)-1)

if result != -1:

    print("Element is present at index " + str(result))

else:

    print("Not found")