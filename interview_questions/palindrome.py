# Write a Python program to check if a string is a palindrome.
def check_palindrome(s):
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

check_palindrome("madam")