import random
import time

# Generate a list of 300 "lastname, firstname" pairs
def generate_name_list():
    # Sample lists of firstnames and lastnames
    firstnames = ["John", "Jane", "Michael", "Emily", "William", "Olivia", "David", "Sophia", "James", "Ava"]
    lastnames = ["Smith", "Johnson", "Brown", "Davis", "Miller", "Wilson", "Moore", "Anderson", "Taylor", "Clark"]

    names = []
    for i in range(300):
        firstname = random.choice(firstnames)
        lastname = random.choice(lastnames)
        names.append(f"{lastname}, {firstname}")
    return sorted(names)  # Sort the list alphabetically

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
names_list = generate_name_list()

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

