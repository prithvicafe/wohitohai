def binarySearch(arr, key, low, high):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


arr = [1, 3, 5, 7, 9]
key = 7
result = binarySearch(arr, key, 0, len(arr) - 1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")