# 58. Length of Last Word

## Problem

Given a string `s` consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

---

## Example 1

Input:

```python
s = "Hello World"
```

Output:

```python
5
```

Explanation:

The last word is `"World"` and its length is `5`.

---

## Example 2

Input:

```python
s = "   fly me   to   the moon  "
```

Output:

```python
4
```

Explanation:

The last word is `"moon"` and its length is `4`.

---

## Example 3

Input:

```python
s = "luffy is still joyboy"
```

Output:

```python
6
```

Explanation:

The last word is `"joyboy"` and its length is `6`.

---

# Python Solution

```python
class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.split()
        return len(words[-1])
```

---

# Approach

- Use `split()` to separate the string into words.
- Use `words[-1]` to get the last word.
- Use `len()` to find its length.
- Return the result.

---

# Built-in Functions Used

### `split()`

Separates a string into a list of words.

Example:

```python
"Hello World".split()
```

Output:

```python
["Hello", "World"]
```

### `len()`

Returns the length of a string or list.

Example:

```python
len("World")
```

Output:

```python
5
```

---

# Complexity Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`

where `n` is the length of the string.

---

# Concepts Used

- Strings
- Lists
- split()
- len()
- Indexing

---

# LeetCode Link

https://leetcode.com/problems/length-of-last-word/
