def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle of the list
        left_half = arr[:mid]  # Divide the list into two halves
        right_half = arr[mid:]

        merge_sort(left_half)  # Recursively sort the left half
        merge_sort(right_half)  # Recursively sort the right half

        # Initialize pointers for merging
        i = j = k = 0

        # Merge the two sorted sublists back into the original list
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if any element was left in either of the sublists
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage:
if __name__ == "__main__":
    unsorted_list = [38, 27, 43, 3, 9, 82, 10]
    print("Unsorted list:", unsorted_list)

    merge_sort(unsorted_list)

    print("Sorted list:", unsorted_list)

