# 383. Ransom Note

## Problem

Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine`, and `false` otherwise.

Each letter in `magazine` can only be used once.

---

## Example 1

Input:

```python
ransomNote = "a"
magazine = "b"
```

Output:

```python
False
```

Explanation:

The magazine does not contain the letter `"a"`.

---

## Example 2

Input:

```python
ransomNote = "aa"
magazine = "ab"
```

Output:

```python
False
```

Explanation:

The magazine has only one `"a"`, but the ransom note needs two.

---

## Example 3

Input:

```python
ransomNote = "aa"
magazine = "aab"
```

Output:

```python
True
```

Explanation:

The magazine contains enough `"a"` characters to build the ransom note.

---

# Python Solution

```python
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for ch in ransomNote:
            if ransomNote.count(ch) > magazine.count(ch):
                return False

        return True
```

---

# Approach

- Loop through every character in `ransomNote`.
- Count how many times the current character appears in `ransomNote`.
- Count how many times the same character appears in `magazine`.
- If the magazine has fewer occurrences of that character, return `False`.
- If every character has enough occurrences, return `True`.

---

# Built-in Function Used

### `count()`

The `count()` method returns how many times a value appears in a string.

Example:

```python
text = "banana"

print(text.count("a"))
```

Output:

```python
3
```

Another example:

```python
text = "banana"

print(text.count("z"))
```

Output:

```python
0
```

---

# Dry Run

Input:

```python
ransomNote = "aa"
magazine = "aab"
```

First iteration:

```python
ch = "a"
```

Count in `ransomNote`:

```python
ransomNote.count("a")
```

↓

```python
2
```

Count in `magazine`:

```python
magazine.count("a")
```

↓

```python
2
```

Check:

```python
2 > 2
```

↓

```python
False
```

The loop finishes because there are enough `"a"` characters.

Return:

```python
True
```

---

# Complexity Analysis

- Time Complexity: `O(n × m)`
- Space Complexity: `O(1)`

where:

- `n` = length of `ransomNote`
- `m` = length of `magazine`

The `count()` method scans the strings each time it is called.

---

# Concepts Used

- Strings
- Loops
- `count()`
- Conditions
- Return Statement

---

# LeetCode Link

https://leetcode.com/problems/ransom-note/
