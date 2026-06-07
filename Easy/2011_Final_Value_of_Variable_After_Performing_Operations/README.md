# 2011. Final Value of Variable After Performing Operations

## Problem

There is a programming language with only four operations and one variable `X`:

- `++X` → Increment the value of `X` by 1, then return the value of `X`.
- `X++` → Return the value of `X`, then increment the value of `X` by 1.
- `--X` → Decrement the value of `X` by 1, then return the value of `X`.
- `X--` → Return the value of `X`, then decrement the value of `X` by 1.

Initially, the value of `X` is `0`.

Given an array of strings `operations`, return the final value of `X` after performing all the operations.

---

## Example 1

Input:

```python
operations = ["--X","X++","X++"]
```

Output:

```python
1
```

Explanation:

```text
X = 0
--X → -1
X++ → 0
X++ → 1
```

Final value = 1

---

## Example 2

Input:

```python
operations = ["++X","++X","X++"]
```

Output:

```python
3
```

---

# Python Solution

```python
class Solution(object):
    def finalValueAfterOperations(self, operations):
        x = 0

        for i in operations:
            if "++" in i:
                x += 1
            else:
                x -= 1

        return x
```

---

# Approach

- Initialize `x = 0`
- Loop through each operation
- If the operation contains `"++"`, increment `x`
- Otherwise, decrement `x`
- Return the final value of `x`

---

# Built-in Concepts Used

### `in`

Checks whether a substring exists inside a string.

Example:

```python
"++" in "X++"
```

Output:

```python
True
```

Example:

```python
"++" in "--X"
```

Output:

```python
False
```

---

# Complexity Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(1)`

where `n` is the number of operations.

---

# Concepts Used

- Loops
- Strings
- Conditions
- `in` Operator

---

# LeetCode Link

https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
