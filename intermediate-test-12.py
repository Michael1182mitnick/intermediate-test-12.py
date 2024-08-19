# Given an array containing n-1 integers in the range of 1 to n, find the missing number.

def find_missing_number(arr):
    n = len(arr) + 1  # The total number of elements should be n
    expected_sum = n * (n + 1) // 2  # Sum of first n natural numbers
    actual_sum = sum(arr)  # Sum of the elements in the array
    missing_number = expected_sum - actual_sum  # The missing number
    return missing_number


# Example usage
arr = [1, 2, 4, 5, 6]
result = find_missing_number(arr)
print(f"The missing number is: {result}")
