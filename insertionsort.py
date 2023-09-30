def insertionSort(array):
    # Iterate over the array starting from the second element
    for step in range(1, len(array)):
        key = array[step]  # Store the current element as the key to be inserted in the right position
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].

        # Move elements greater than key one position ahead
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]   # Shift elements to the right
            j = j - 1

        # Insert the key in the correct position
        array[j + 1] = key


data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)