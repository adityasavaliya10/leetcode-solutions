# 2114. Maximum Number of Words Found in Sentences

## Problem

A sentence is a list of words separated by a single space with no leading or trailing spaces.

You are given an array of strings `sentences`, where each element represents a sentence.

Return the maximum number of words that appear in a single sentence.

---

## Example 1

Input:

```python
sentences = [
    "alice and bob love leetcode",
    "i think so too",
    "this is great thanks very much"
]
```

Output:

```python
6
```

Explanation:

- "alice and bob love leetcode" → 5 words
- "i think so too" → 4 words
- "this is great thanks very much" → 6 words

The maximum number of words in a sentence is 6.

---

## Example 2

Input:

```python
sentences = [
    "please wait",
    "continue to fight",
    "continue to win"
]
```

Output:

```python
3
```

---

# Python Solution

```python
class Solution(object):
    def mostWordsFound(self, sentences):
        maximum = 0

        for sentence in sentences:
            words = len(sentence.split())

            if words > maximum:
                maximum = words

        return maximum
```

---

# Approach

- Initialize `maximum` to 0.
- Loop through each sentence.
- Use `split()` to separate the sentence into words.
- Use `len()` to count the number of words.
- If the current count is greater than `maximum`, update `maximum`.
- Return `maximum`.

---

# Complexity Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(1)`

---

# Concepts Used

- Strings
- split()
- len()
- for loops
- if statements
- Maximum value tracking

---

# LeetCode Link

https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/
