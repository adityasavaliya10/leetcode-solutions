# 125. Valid Palindrome

## Problem

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

---

## Example 1

Input:

```python
s = "A man, a plan, a canal: Panama"
```

Output:

```python
True
```

Explanation:

After removing spaces and punctuation and converting to lowercase:

```python
"amanaplanacanalpanama"
```

This string reads the same forwards and backwards.

---

## Example 2

Input:

```python
s = "race a car"
```

Output:

```python
False
```

---

## Example 3

Input:

```python
s = " "
```

Output:

```python
True
```

Explanation:

After removing non-alphanumeric characters, the string becomes empty, which is considered a palindrome.

---

# Python Solution

```python
class Solution(object):
    def isPalindrome(self, s):
        cleaned = ""

        for char in s:
            if char.isalnum():
                cleaned += char.lower()

        return cleaned == cleaned[::-1]
```

---

# Approach

- Create an empty string called `cleaned`
- Traverse through every character in the input string
- Keep only letters and numbers using `isalnum()`
- Convert all characters to lowercase using `lower()`
- Compare the cleaned string with its reverse
- Return the result

---

# Built-in Functions Used

### `isalnum()`

Checks whether a character is a letter or a number.

Examples:

```python
"a".isalnum()   # True
"7".isalnum()   # True
"!".isalnum()   # False
```

### `lower()`

Converts characters to lowercase.

Example:

```python
"HELLO".lower()
```

Output:

```python
"hello"
```

### `[::-1]`

Reverses a string.

Example:

```python
"abc"[::-1]
```

Output:

```python
"cba"
```

---

# Complexity Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`

---

# Concepts Used

- Strings
- Loops
- Conditions
- String Reversal
- `isalnum()`
- `lower()`

---

# LeetCode Link

https://leetcode.com/problems/valid-palindrome/
