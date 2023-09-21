def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Start with a large gap and reduce it

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            # Move elements that are greater than temp
            # to the right by 'gap' positions
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            # Place temp in its correct position
            arr[j] = temp

        # Reduce the gap for the next iteration
        gap //= 2

def main():
    try:
        input_str = input("Enter a list of integers separated by spaces: ")
        input_list = [int(x) for x in input_str.split()]

        shell_sort(input_list)

        print("Sorted list:", input_list)
    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()

