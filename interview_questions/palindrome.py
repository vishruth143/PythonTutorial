# Write python program to check if the given string is palindrome.

# Method 1: Using slicing
def is_palindrome_slicing(s: str) -> bool:
    return s == s[::-1]

# Method 2: Using two pointers
def is_palindrome_two_pointers(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Test cases
print(is_palindrome_slicing("level"))   # True
print(is_palindrome_slicing("python"))  # False

print(is_palindrome_two_pointers("madam"))  # True
print(is_palindrome_two_pointers("world"))  # False

