import random
import time

# Generate a list of 300 "lastname, firstname" entries in alphabetical order
def generate_sorted_name_list():
    names = []
    for i in range(300):
        lastname = f"Lastname{i}"
        firstname = f"Firstname{i}"
        names.append(f"{lastname}, {firstname}")
    return names

# Binary search function with try counting
def binary_search_with_count(arr, target):
    left, right = 0, len(arr) - 1
    tries = 0  # Initialize the try count

    while left <= right:
        mid = left + (right - left) // 2
        tries += 1  # Increment the try count

        if arr[mid] == target:
            return mid, tries  # Entry found, return its index and try count
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, tries  # Entry not found, return -1 and try count

# Generate the list of "lastname, firstname" entries
names_list = generate_sorted_name_list()

# Choose a random entry to search for
target_entry = random.choice(names_list)

# Perform binary search and count the number of tries
start_time = time.time()
index, tries = binary_search_with_count(names_list, target_entry)
end_time = time.time()

if index != -1:
    print(f"Entry '{target_entry}' found at index {index} in {tries} tries.")
else:
    print(f"Entry '{target_entry}' not found in the list in {tries} tries.")
    
print(f"Execution time: {end_time - start_time:.6f} seconds")

