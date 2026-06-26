# 1662. Check If Two String Arrays are Equivalent

## Problem

Given two string arrays `word1` and `word2`, return `true` if the two arrays represent the same string, and `false` otherwise.

A string is represented by concatenating (joining) all the strings in the array in order.

---

## Example 1

Input:

```python
word1 = ["ab", "c"]
word2 = ["a", "bc"]
```

Output:

```python
True
```

Explanation:

```text
word1 → "ab" + "c" = "abc"
word2 → "a" + "bc" = "abc"
```

Both arrays represent the same string.

---

## Example 2

Input:

```python
word1 = ["a", "cb"]
word2 = ["ab", "c"]
```

Output:

```python
False
```

Explanation:

```text
word1 → "acb"
word2 → "abc"
```

The strings are different.

---

## Example 3

Input:

```python
word1 = ["abc", "d", "defg"]
word2 = ["abcddefg"]
```

Output:

```python
True
```

---

# Python Solution

```python
class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        return "".join(word1) == "".join(word2)
```

---

# Approach

- Join all strings in `word1` into one string using `join()`.
- Join all strings in `word2` into one string.
- Compare both strings.
- If they are equal, return `True`; otherwise, return `False`.

---

# Built-in Function Used

### `join()`

The `join()` method combines all strings in a list into one string.

Example:

```python
words = ["Hello", "World"]
result = "".join(words)
print(result)
```

Output:

```text
HelloWorld
```

If you use a space:

```python
" ".join(words)
```

Output:

```text
Hello World
```

---

# Dry Run

Input:

```python
word1 = ["ab", "c"]
word2 = ["a", "bc"]
```

Join `word1`:

```python
"".join(word1)
```

↓

```text
"abc"
```

Join `word2`:

```python
"".join(word2)
```

↓

```text
"abc"
```

Compare:

```python
"abc" == "abc"
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

- Time Complexity: `O(n + m)`

  - `n` = total number of characters in `word1`
  - `m` = total number of characters in `word2`

- Space Complexity: `O(n + m)`

---

# Concepts Used

- Strings
- Arrays (Lists)
- `join()`
- String Comparison (`==`)
- Return Statement

---

# LeetCode Link

https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
