# 1480. Running Sum of 1d Array

## Problem
Given an array `nums`, return the running sum of `nums`.

### Example
Input:
```python
[1,2,3,4]
```

Output:
```python
[1,3,6,10]
```

Explanation:
- 1
- 1 + 2 = 3
- 1 + 2 + 3 = 6
- 1 + 2 + 3 + 4 = 10

---


# Approach

- Create an empty list `ans`
- Use variable `a` to store the running sum
- Traverse through `nums`
- Add each number to `a`
- Append updated sum into `ans`
- Return `ans`

---

# Complexity Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`

---

# LeetCode Link

https://leetcode.com/problems/running-sum-of-1d-array/
