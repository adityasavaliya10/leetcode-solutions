# 326. Power of Three

## Problem

Given an integer `n`, return `true` if it is a power of three. Otherwise, return `false`.

An integer `n` is a power of three if there exists an integer `x` such that:

```text
n = 3^x
```

---

## Example 1

Input:

```python
n = 27
```

Output:

```python
True
```

Explanation:

```text
27 = 3 × 3 × 3 = 3³
```

---

## Example 2

Input:

```python
n = 0
```

Output:

```python
False
```

Explanation:

```text
0 is not a power of three.
```

---

## Example 3

Input:

```python
n = -3
```

Output:

```python
False
```

Explanation:

```text
Negative numbers cannot be powers of three.
```

---

# Python Solution

```python
class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False

        while n % 3 == 0:
            n = n // 3

        return n == 1
```

---

# Approach

- If `n <= 0`, return `False`.
- While `n` is divisible by `3`, divide it by `3`.
- After the loop:
  - If `n` becomes `1`, the original number was a power of three.
  - Otherwise, it was not.

---

# Dry Run

Input:

```python
n = 81
```

Step 1:

```python
81 % 3 == 0
n = 81 // 3 = 27
```

Step 2:

```python
27 % 3 == 0
n = 27 // 3 = 9
```

Step 3:

```python
9 % 3 == 0
n = 9 // 3 = 3
```

Step 4:

```python
3 % 3 == 0
n = 3 // 3 = 1
```

Loop stops because:

```python
1 % 3 != 0
```

Final check:

```python
n == 1
```

Output:

```python
True
```

---

# Complexity Analysis

- Time Complexity: `O(log₃ n)`
- Space Complexity: `O(1)`

---

# Concepts Used

- Loops
- Modulo Operator `%`
- Integer Division `//`
- Conditions

---

# LeetCode Link

https://leetcode.com/problems/power-of-three/
