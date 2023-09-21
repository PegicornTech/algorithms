import sys

def binary_search_first_half(data, target):
    left, right = 0, len(data) - 1

    while left <= right:
        mid = left + (right - left) // 2
        current_half = data[mid].split(" ")[0]

        if current_half == target:
            return mid  # Found a match, return the index
        elif current_half < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Not found

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python binary_search_first_half.py <target>")
        sys.exit(1)

    target = sys.argv[1]

    # Sample list of strings where the first half is delimited by space
    data = ["apple pie", "banana split", "chocolate cake", "lemon tart", "orange juice", "strawberry jam"]

    # Perform binary search
    result = binary_search_first_half(data, target)

    if result != -1:
        print(f"Found '{target}' at index {result}")
    else:
        print(f"'{target}' not found in the list.")

