# 2119. A Number After a Double Reversal

## Problem

Reversing an integer means reversing all its digits.

- For example, reversing `2021` gives `1202`.
- Reversing `12300` gives `321` because leading zeros are removed.

Given an integer `num`, reverse `num` to get `reversed1`, then reverse `reversed1` to get `reversed2`.

Return `true` if `reversed2` equals `num`. Otherwise, return `false`.

---

## Example 1

Input:

```python
num = 526
```

Output:

```python
True
```

Explanation:

```text
526 → 625 → 526
```

The number remains unchanged after two reversals.

---

## Example 2

Input:

```python
num = 1800
```

Output:

```python
False
```

Explanation:

```text
1800 → 81 → 18
```

Since:

```text
18 ≠ 1800
```

the answer is `False`.

---

## Example 3

Input:

```python
num = 0
```

Output:

```python
True
```

Explanation:

```text
0 → 0 → 0
```

---

# Python Solution

```python
class Solution(object):
    def isSameAfterReversals(self, num):
        if num == 0:
            return True

        return num % 10 != 0
```

---

# Approach

- If the number is `0`, return `True`.
- Otherwise, check whether the number ends with `0`.
- If it ends with `0`, some digits are lost during reversal, so return `False`.
- Otherwise, return `True`.

---

# Dry Run

Input:

```python
num = 1800
```

Check:

```python
num == 0
```

↓

```python
False
```

Check:

```python
1800 % 10
```

↓

```python
0
```

Since the last digit is `0`, the number changes after reversing twice.

Output:

```python
False
```

---

# Complexity Analysis

- Time Complexity: `O(1)`
- Space Complexity: `O(1)`

---

# Concepts Used

- Modulo Operator `%`
- Conditions
- Mathematical Observation

---

# LeetCode Link

https://leetcode.com/problems/a-number-after-a-double-reversal/
