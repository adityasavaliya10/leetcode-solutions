# 231. Power of Two

## Problem

Given an integer `n`, return `true` if it is a power of two. Otherwise, return `false`.

An integer `n` is a power of two if there exists an integer `x` such that:

```text
n = 2^x
```

---

## Example 1

Input:

```python
n = 1
```

Output:

```python
True
```

Explanation:

```text
2^0 = 1
```

---

## Example 2

Input:

```python
n = 16
```

Output:

```python
True
```

Explanation:

```text
16 = 2 × 2 × 2 × 2 = 2^4
```

---

## Example 3

Input:

```python
n = 3
```

Output:

```python
False
```

Explanation:

```text
3 is not a power of two.
```

---

# Python Solution

```python
class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False

        while n % 2 == 0:
            n = n // 2

        return n == 1
```

---

# Approach

- If `n <= 0`, return `False`.
- Keep dividing `n` by 2 while it is divisible by 2.
- If the final value becomes `1`, return `True`.
- Otherwise return `False`.

---

# Dry Run

Input:

```python
n = 16
```

Step 1:

```python
16 % 2 == 0
n = 16 // 2 = 8
```

Step 2:

```python
8 % 2 == 0
n = 8 // 2 = 4
```

Step 3:

```python
4 % 2 == 0
n = 4 // 2 = 2
```

Step 4:

```python
2 % 2 == 0
n = 2 // 2 = 1
```

Loop stops.

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

- Time Complexity: `O(log n)`
- Space Complexity: `O(1)`

---

# Concepts Used

- Loops
- Modulo Operator `%`
- Integer Division `//`
- Conditions

---

# LeetCode Link

https://leetcode.com/problems/power-of-two/
