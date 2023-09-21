def euclid_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_gcd_of_list(numbers):
    if len(numbers) < 2:
        return None
    gcd_result = numbers[0]
    for num in numbers[1:]:
        gcd_result = euclid_gcd(gcd_result, num)
    return gcd_result

def main():
    try:
        num_list = []
        num_count = int(input("Enter the number of integers: "))
        for i in range(num_count):
            num = int(input(f"Enter integer {i+1}: "))
            num_list.append(num)

        gcd = find_gcd_of_list(num_list)
        if gcd is not None:
            print(f"The GCD of the given integers is {gcd}")
        else:
            print("Please provide at least two integers to find the GCD.")
    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()

