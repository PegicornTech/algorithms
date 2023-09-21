def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to optimize - if no swaps are made in a pass, the list is already sorted
        swapped = False

        # Last i elements are already in place, so we don't need to check them again
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements because they are out of order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no two elements were swapped in this pass, the list is already sorted
        if not swapped:
            break

# Example usage
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    bubble_sort(arr)
    print("Sorted array:", arr)

