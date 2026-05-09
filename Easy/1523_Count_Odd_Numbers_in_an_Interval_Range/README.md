# 1523. Count Odd Numbers in an Interval Range

## Difficulty
Easy

## Problem Summary
Given two integers `low` and `high`, return the number of odd numbers between `low` and `high` (inclusive).

## Beginner Approach (Using a For Loop)

This is the most straightforward way to solve the problem. We check every number from `low` to `high` and count how many numbers are odd.

### Python Solution

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = 0

        for i in range(low, high + 1):
            if i % 2 != 0:
                count += 1

        return count

Why This Approach Works
We iterate through every number in the range.
We use i % 2 != 0 to check whether a number is odd.
We increase the counter whenever we find an odd number.
Drawback of This Approach

This solution is correct, but it is inefficient for very large ranges because it checks every single number.


Optimized Approach 

Instead of checking every number, we can calculate the answer directly using a formula.

Python Solution

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2

How the Formula Works
    (high + 1) // 2 gives the number of odd numbers from 1 to high.
    low // 2 gives the number of odd numbers before low.
    Subtracting them gives the number of odd numbers between low and high.
Why This Approach Is Better
    No loop is required.
    The answer is computed instantly.
    It is much faster for large inputs.

Concepts Used
    Loops
    Conditional Statements
    Modulus Operator (%)
    Floor Division (//)
    Mathematical Optimization
What I Learned
    How to solve a problem using a simple brute-force approach.
    Why a correct solution may still be inefficient.
    How to optimize a solution using mathematics.
    How floor division (//) can be used to count odd numbers directly.
