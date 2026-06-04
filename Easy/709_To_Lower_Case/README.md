# 709. To Lower Case

## Problem

Given a string `s`, return the string after replacing every uppercase letter with the same lowercase letter.

---

## Example 1

Input:

```python
s = "Hello"
```

Output:

```python
"hello"
```

---

## Example 2

Input:

```python
s = "LOVELY"
```

Output:

```python
"lovely"
```

---

## Example 3

Input:

```python
s = "here"
```

Output:

```python
"here"
```

---

# Python Solution

```python
class Solution(object):
    def toLowerCase(self, s):
        return s.lower()
```

---

# Approach

- Use Python's built-in `lower()` function.
- `lower()` converts all uppercase letters to lowercase.
- Return the converted string.

---

# Built-in Function Used

### `lower()`

Converts all uppercase letters in a string to lowercase.

Example:

```python
"HELLO".lower()
```

Output:

```python
"hello"
```

---

# Complexity Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`

where `n` is the length of the string.

---

# Concepts Used

- Strings
- Built-in Functions
- `lower()`

---

# LeetCode Link

https://leetcode.com/problems/to-lower-case/
