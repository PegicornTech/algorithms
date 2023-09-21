def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: If the array has 0 or 1 element, it's already sorted

    pivot = arr[len(arr) // 2]  # Choose the pivot element (middle element in this example)
    left = [x for x in arr if x < pivot]  # Elements smaller than the pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot

    # Recursively sort the left and right sub-arrays and concatenate them with the middle array
    return quick_sort(left) + middle + quick_sort(right)

# Example usage
if __name__ == "__main__":
    arr = [3, 6, 8, 10, 1, 2, 1]
    print("Original array:", arr)
    sorted_arr = quick_sort(arr)
    print("Sorted array:", sorted_arr)

