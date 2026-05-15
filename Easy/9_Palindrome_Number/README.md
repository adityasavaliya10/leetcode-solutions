# Palindrome Number Checker in Python

This Python program checks whether a given integer is a palindrome.

## What is a Palindrome?

A palindrome number reads the same forward and backward.

### Examples

- 121 → Palindrome
- 1331 → Palindrome
- 123 → Not a palindrome

## Logic Used

1. Store the original number.
2. Reverse the number using:
   - `% 10` to get the last digit.
   - `reverse = reverse * 10 + digit`.
   - `num //= 10` to remove the last digit.
3. Compare the reversed number with the original number.
