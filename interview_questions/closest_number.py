# Write a function to find 2 closest numbers from given list of numbers.

def closest_numbers(numbers):
    if len(numbers) < 2:
        return None, None  # Not enough numbers to find a pair

    # Sort the list to make it easier to find the closest numbers
    sorted_numbers = sorted(numbers)

    min_diff = float('inf')
    closest_pair = (None, None)

    for i in range(len(sorted_numbers) - 1):
        diff = sorted_numbers[i + 1] - sorted_numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])

    return closest_pair

list1 = [10, 1, 11, 100, 98, 45, 67]
print(closest_numbers(list1))