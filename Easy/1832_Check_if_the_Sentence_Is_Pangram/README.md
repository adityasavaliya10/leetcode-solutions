# 1832. Check if the Sentence Is Pangram

## Problem

A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string `sentence` containing only lowercase English letters, return `true` if `sentence` is a pangram, or `false` otherwise.

---

## Example 1

Input:

```python
sentence = "thequickbrownfoxjumpsoverthelazydog"
```

Output:

```python
True
```

Explanation:

The sentence contains every letter from `a` to `z`.

---

## Example 2

Input:

```python
sentence = "leetcode"
```

Output:

```python
False
```

Explanation:

The sentence does not contain all 26 letters of the alphabet.

---

# Python Solution

```python
class Solution(object):
    def checkIfPangram(self, sentence):
        checker = set(sentence)
        return len(checker) == 26
```

---

# Approach

- Convert the sentence into a set using `set()`.
- A set stores only unique characters.
- Count the number of unique characters using `len()`.
- If there are exactly 26 unique letters, the sentence is a pangram.
- Otherwise, it is not.

---

# Built-in Functions Used

### `set()`

Creates a collection of unique values.

Example:

```python
set("banana")
```

Output:

```python
{'b', 'a', 'n'}
```

Notice that duplicate letters are removed.

---

### `len()`

Returns the number of items in a collection.

Example:

```python
len(set("banana"))
```

Output:

```python
3
```

---

# Dry Run

Input:

```python
sentence = "thequickbrownfoxjumpsoverthelazydog"
```

Convert to a set:

```python
checker = set(sentence)
```

Unique letters:

```text
a, b, c, d, ..., z
```

Count:

```python
len(checker)
```

Result:

```python
26
```

Check:

```python
26 == 26
```

Output:

```python
True
```

---

# Complexity Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(1)`

The set can contain at most 26 lowercase letters.

---

# Concepts Used

- Strings
- Sets
- Unique Characters
- len()
- set()

---

# LeetCode Link

https://leetcode.com/problems/check-if-the-sentence-is-pangram/
