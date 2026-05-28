# 2942. Find Words Containing Character

## Problem

You are given a 0-indexed array of strings `words` and a character `x`.

Return an array of indices representing the words that contain the character `x`.

The returned array may be in any order.

---

## Example 1

Input:
```python
words = ["leet","code"]
x = "e"
```

Output:
```python
[0,1]
```

Explanation:
- "leet" contains 'e' → index 0
- "code" contains 'e' → index 1

---

## Example 2

Input:
```python
words = ["abc","bcd","aaaa","cbc"]
x = "a"
```

Output:
```python
[0,2]
```

---

# Approach

- Create an empty list `ans`
- Traverse through the indices of `words`
- Check if character `x` exists in each word using `in`
- If present, append the index to `ans`
- Return `ans`

---

# Complexity Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`

---

# LeetCode Link

https://leetcode.com/problems/find-words-containing-character/
