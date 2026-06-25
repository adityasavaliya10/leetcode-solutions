# 268. Missing Number

## Problem

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

---

## Example 1

Input:

```python
nums = [3,0,1]
```

Output:

```python
2
```

---

## Example 2

Input:

```python
nums = [0,1]
```

Output:

```python
2
```

---

## Example 3

Input:

```python
nums = [9,6,4,2,3,5,7,0,1]
```

Output:

```python
8
```

---

# Python Solution

```python
class Solution(object):
    def missingNumber(self, nums):
        for i in range(len(nums) + 1):
            if i not in nums:
                return i
```

---

# Approach

- The array contains numbers from `0` to `n`.
- Loop through every number from `0` to `n`.
- Check if the current number exists in the array.
- If it does not exist, return it.
- The missing number is found immediately.

---

# Dry Run

Input:

```python
nums = [3,0,1]
```

Loop:

```python
i = 0
```

`0 in nums` → Yes

```python
i = 1
```

`1 in nums` → Yes

```python
i = 2
```

`2 in nums` → No

Return:

```python
2
```

---

# Complexity Analysis

- Time Complexity: `O(n²)`
- Space Complexity: `O(1)`

### Why O(n²)?

For every value of `i`, Python may need to search through the entire list when checking:

```python
i not in nums
```

So:

```text
n × n = O(n²)
```

---

# Concepts Used

- Arrays
- Loops
- `range()`
- Membership Operator (`in`, `not in`)
- Conditions

---

# LeetCode Link

https://leetcode.com/problems/missing-number/
