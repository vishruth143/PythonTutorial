# Write design_pattern Python program to check if design_pattern string is design_pattern palindrome.
def check_palindrome(s):
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

check_palindrome("madam")