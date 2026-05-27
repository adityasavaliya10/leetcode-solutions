# 1108. Defanging an IP Address

## Problem
Given a valid IPv4 IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

---

## Example 1

Input:
```python
address = "1.1.1.1"
```

Output:
```python
"1[.]1[.]1[.]1"
```

---

## Example 2

Input:
```python
address = "255.100.50.0"
```

Output:
```python
"255[.]100[.]50[.]0"
```

---



# Approach

- Use Python's built-in `replace()` function
- Replace every `"."` with `"[.]"`

---

# Complexity Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`

---

# LeetCode Link

https://leetcode.com/problems/defanging-an-ip-address/
