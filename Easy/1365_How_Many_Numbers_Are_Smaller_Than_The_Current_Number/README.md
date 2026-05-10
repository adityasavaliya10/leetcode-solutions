# LeetCode 1365 - How Many Numbers Are Smaller Than the Current Number

## Problem Statement
Given the array `nums`, for each `nums[i]`, find out how many numbers in the array are smaller than it. Return the answer in an array.

## Example
### Input
```python
nums = [8, 1, 2, 2, 3]
```

### Output
```python
[4, 0, 1, 1, 3]
```

## Beginner Approach (Nested Loops)
This solution uses two nested loops:

1. Take one number from the list.
2. Compare it with every other number.
3. Count how many numbers are smaller than it.
4. Store the count in the result list.

This approach is very easy to understand and is great for beginners learning Python and problem solving.


## Concepts Used
- Lists
- Nested loops
- Conditional statements
- Counting
- Time complexity

## Notes
This is a beginner-friendly solution. It is not the most efficient approach, but it is excellent for understanding how to compare elements and count occurrences.
