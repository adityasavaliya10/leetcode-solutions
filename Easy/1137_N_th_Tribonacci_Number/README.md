# 1137. N-th Tribonacci Number

## Problem

The Tribonacci sequence Tn is defined as follows:

```text
T0 = 0
T1 = 1
T2 = 1
```

and

```text
Tn = Tn-1 + Tn-2 + Tn-3
```

for `n >= 3`.

Given `n`, return the value of `Tn`.

---

## Example 1

Input:

```python
n = 4
```

Output:

```python
4
```

Explanation:

```text
T3 = T2 + T1 + T0
   = 1 + 1 + 0
   = 2

T4 = T3 + T2 + T1
   = 2 + 1 + 1
   = 4
```

---

## Example 2

Input:

```python
n = 5
```

Output:

```python
7
```

Explanation:

```text
T5 = T4 + T3 + T2
   = 4 + 2 + 1
   = 7
```

---

# Python Solution

```python
class Solution(object):
    def tribonacci(self, n):
        if n == 0:
            return n

        if n == 1 or n == 2:
            return 1

        a = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)

        return a
```

---

# Approach

- If `n = 0`, return `0`
- If `n = 1` or `n = 2`, return `1`
- Otherwise calculate:

```text
Tn = Tn-1 + Tn-2 + Tn-3
```

using recursion.

---

# Dry Run

For:

```python
n = 4
```

The function calculates:

```text
T4 = T3 + T2 + T1
   = 2 + 1 + 1
   = 4
```

Return:

```python
4
```

---

# Complexity Analysis

### Time Complexity

```text
O(3^n)
```

because each function call creates three more recursive calls.

### Space Complexity

```text
O(n)
```

due to the recursion call stack.

---

# Concepts Used

- Recursion
- Functions
- Base Cases
- Mathematical Sequences

---

# LeetCode Link

https://leetcode.com/problems/n-th-tribonacci-number/
