# 1816. Truncate Sentence

## Problem

A sentence is a list of words separated by a single space.

Given a string `s` representing a sentence and an integer `k`, return the sentence after truncating it so that it contains only the first `k` words.

---

## Example 1

Input:

```python
s = "Hello how are you Contestant"
k = 4
```

Output:

```python
"Hello how are you"
```

Explanation:

The sentence contains five words.

Keep only the first four words:

* Hello
* how
* are
* you

---

## Example 2

Input:

```python
s = "What is the solution"
k = 2
```

Output:

```python
"What is"
```

Explanation:

Keep only the first two words.

---

# Python Solution

```python
class Solution(object):
    def truncateSentence(self, s, k):
        words = s.split()
        return " ".join(words[:k])
```

---

# Approach

1. Use `split()` to divide the sentence into a list of words.
2. Use list slicing `[:k]` to keep only the first `k` words.
3. Use `" ".join()` to combine those words back into a sentence.
4. Return the new sentence.

---

# Built-in Functions Used

## `split()`

The `split()` function breaks a string into a list of words.

Example:

```python
text = "I love Python"

print(text.split())
```

Output:

```python
["I", "love", "Python"]
```

---

## List Slicing `[:k]`

List slicing returns the first `k` elements.

Example:

```python
words = ["I", "love", "Python", "very", "much"]

print(words[:3])
```

Output:

```python
["I", "love", "Python"]
```

---

## `join()`

The `join()` function combines a list of strings into one string.

Example:

```python
words = ["I", "love", "Python"]

print(" ".join(words))
```

Output:

```python
I love Python
```

The `" "` means each word is joined with a space.

---

# Dry Run

Input:

```python
s = "I love programming every day"
k = 3
```

### Step 1

```python
words = s.split()
```

Result:

```python
["I", "love", "programming", "every", "day"]
```

### Step 2

```python
words[:3]
```

Result:

```python
["I", "love", "programming"]
```

### Step 3

```python
" ".join(words[:3])
```

Result:

```python
"I love programming"
```

Return:

```python
"I love programming"
```

---

# Complexity Analysis

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

where `n` is the length of the input sentence.

---

# Concepts Used

* Strings
* Lists
* `split()`
* List Slicing
* `join()`

---

# LeetCode Link

https://leetcode.com/problems/truncate-sentence/
