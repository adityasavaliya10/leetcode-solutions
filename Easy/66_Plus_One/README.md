# 66. Plus One

## Problem

You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the `i`th digit of the integer.

The digits are ordered from most significant to least significant in left-to-right order.

Increment the large integer by one and return the resulting array of digits.

---

## Example 1

Input:

```python
digits = [1,2,3]
```

Output:

```python
[1,2,4]
```

Explanation:

```text
123 + 1 = 124
```

---

## Example 2

Input:

```python
digits = [4,3,2,1]
```

Output:

```python
[4,3,2,2]
```

Explanation:

```text
4321 + 1 = 4322
```

---

## Example 3

Input:

```python
digits = [9]
```

Output:

```python
[1,0]
```

Explanation:

```text
9 + 1 = 10
```

---

# Python Solution

```python
class Solution(object):
    def plusOne(self, digits):
        number = int("".join(map(str, digits)))
        number += 1
        return [int(i) for i in str(number)]
```

---

# Approach

- Convert each digit into a string using `map(str, digits)`.
- Join all the strings together using `"".join()` to form one number as a string.
- Convert the string into an integer.
- Add `1` to the integer.
- Convert the updated number back into a string.
- Convert each character of the string back into an integer using a list comprehension.
- Return the final list.

---

# Built-in Functions Used

### `map()`

Applies a function to every element in an iterable.

Example:

```python
digits = [1,2,3]
list(map(str, digits))
```

Output:

```python
['1', '2', '3']
```

---

### `join()`

Combines multiple strings into one string.

Example:

```python
"".join(["1","2","3"])
```

Output:

```text
123
```

---

### `int()`

Converts a string into an integer.

Example:

```python
int("123")
```

Output:

```python
123
```

---

### `str()`

Converts an integer into a string.

Example:

```python
str(124)
```

Output:

```text
"124"
```

---

# Dry Run

Input:

```python
digits = [9,9]
```

Convert digits to strings:

```python
['9', '9']
```

Join:

```python
"99"
```

Convert to integer:

```python
99
```

Add one:

```python
100
```

Convert back to string:

```python
"100"
```

Convert each character back to an integer:

```python
[1,0,0]
```

Return:

```python
[1,0,0]
```

---

# Complexity Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`

where `n` is the number of digits.

---

# Concepts Used

- Arrays (Lists)
- Strings
- `map()`
- `join()`
- `int()`
- `str()`
- List Comprehension
- Type Conversion

---

# LeetCode Link

https://leetcode.com/problems/plus-one/
