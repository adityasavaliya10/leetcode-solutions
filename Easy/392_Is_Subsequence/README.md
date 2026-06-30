# 392. Is Subsequence

## Problem

Given two strings `s` and `t`, return `true` if `s` is a subsequence of `t`, or `false` otherwise.

A **subsequence** is a new string formed from the original string by deleting some (or no) characters without changing the relative order of the remaining characters.

---

## Example 1

Input:

```python
s = "abc"
t = "ahbgdc"
```

Output:

```python
True
```

Explanation:

The characters `a`, `b`, and `c` appear in `t` in the same order.

---

## Example 2

Input:

```python
s = "axc"
t = "ahbgdc"
```

Output:

```python
False
```

Explanation:

The character `x` does not appear in `t`.

---

# Python Solution

```python
class Solution(object):
    def isSubsequence(self, s, t):
        i = 0

        for ch in t:
            if i < len(s) and s[i] == ch:
                i += 1

        return i == len(s)
```

---

# Approach

* Create a variable `i` to keep track of the current character in `s`.
* Loop through every character in `t`.
* If the current character in `t` matches the current character in `s`, move `i` to the next character.
* After checking all characters in `t`, if `i` reaches the length of `s`, then all characters of `s` were found in order.
* Return `True`; otherwise, return `False`.

---

# Dry Run

Input:

```python
s = "abc"
t = "ahbgdc"
```

Start:

```python
i = 0
```

Need to find:

```text
a
```

Loop through `t`:

```text
a h b g d c
```

* `a` == `a` ✅ → `i = 1`
* `h` != `b` ❌
* `b` == `b` ✅ → `i = 2`
* `g` != `c` ❌
* `d` != `c` ❌
* `c` == `c` ✅ → `i = 3`

Check:

```python
i == len(s)
```

↓

```python
3 == 3
```

↓

```python
True
```

---

# Complexity Analysis

* **Time Complexity:** `O(n)`

  * `n` = length of `t`

* **Space Complexity:** `O(1)`

---

# Concepts Used

* Strings
* Loops
* Indexing
* `len()`
* Conditions
* Two Pointers

---

# LeetCode Link

https://leetcode.com/problems/is-subsequence/
