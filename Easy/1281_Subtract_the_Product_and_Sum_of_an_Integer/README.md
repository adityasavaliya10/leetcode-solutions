# Subtract the Product and Sum of Digits of an Integer

This is a solution to the LeetCode problem:
"Subtract the Product and Sum of Digits of an Integer."

## Problem Statement

Given an integer `n`, return the difference between:

1. The product of its digits
2. The sum of its digits

## Example

Input:
234

Output:
15

### Explanation

- Product of digits = 2 × 3 × 4 = 24
- Sum of digits = 2 + 3 + 4 = 9
- Result = 24 - 9 = 15

## Approach

1. Traverse each digit using `% 10`.
2. Build the sum of digits.
3. Reset the number and build the product of digits.
4. Return `product - sum`.
