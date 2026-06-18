# 217. Contains Duplicate

## Problem

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

---

## Example 1

Input:

```python
nums = [1,2,3,1]
```

Output:

```python
True
```

Explanation:

The number `1` appears twice.

---

## Example 2

Input:

```python
nums = [1,2,3,4]
```

Output:

```python
False
```

Explanation:

All elements are distinct.

---

## Example 3

Input:

```python
nums = [1,1,1,3,3,4,3,2,4,2]
```

Output:

```python
True
```

---

# Python Solution

```python
class Solution(object):
    def containsDuplicate(self, nums):
        if len(set(nums)) < len(nums):
            return True
        else:
            return False
```

---

# Approach

- Convert the array into a set using `set()`.
- A set stores only unique elements.
- Compare the length of the set with the length of the original array.
- If the set is smaller, duplicates were removed, so return `True`.
- Otherwise, return `False`.

---

# Built-in Functions Used

### `set()`

Creates a collection of unique values.

Example:

```python
set([1,2,3,1])
```

Output:

```python
{1,2,3}
```

Notice that the duplicate `1` is removed.

---

### `len()`

Returns the number of elements.

Example:

```python
len([1,2,3,1])
```

Output:

```python
4
```

Example:

```python
len(set([1,2,3,1]))
```

Output:

```python
3
```

---

# Dry Run

Input:

```python
nums = [1,2,3,1]
```

Original length:

```python
len(nums)
```

↓

```python
4
```

Set:

```python
set(nums)
```

↓

```python
{1,2,3}
```

Set length:

```python
3
```

Check:

```python
3 < 4
```

↓

```python
True
```

Return:

```python
True
```

---

# Complexity Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`

where `n` is the number of elements in the array.

---

# Concepts Used

- Arrays
- Sets
- `set()`
- `len()`
- Conditions

---

# LeetCode Link

https://leetcode.com/problems/contains-duplicate/
