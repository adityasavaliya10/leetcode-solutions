# 13. Roman to Integer

## Problem

Roman numerals are represented by seven different symbols:

| Symbol | Value |
| ------ | ----: |
| I      |     1 |
| V      |     5 |
| X      |    10 |
| L      |    50 |
| C      |   100 |
| D      |   500 |
| M      |  1000 |

Normally, Roman numerals are written from largest to smallest and their values are added together.

However, when a smaller numeral appears before a larger numeral, its value is subtracted instead of added.

Given a Roman numeral string `s`, convert it to an integer.

---

## Example 1

Input:

```python
s = "III"
```

Output:

```python
3
```

Explanation:

```text
I + I + I = 1 + 1 + 1 = 3
```

---

## Example 2

Input:

```python
s = "LVIII"
```

Output:

```python
58
```

Explanation:

```text
L = 50
V = 5
I = 1
I = 1
I = 1

50 + 5 + 1 + 1 + 1 = 58
```

---

## Example 3

Input:

```python
s = "MCMXCIV"
```

Output:

```python
1994
```

Explanation:

```text
M  = 1000
CM = 900
XC = 90
IV = 4

1000 + 900 + 90 + 4 = 1994
```

---

# Python Solution

```python
class Solution(object):
    def romanToInt(self, s):
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0

        for i in range(len(s)):
            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]

        return total
```

---

# Approach

* Store the value of each Roman numeral in a dictionary.
* Create a variable `total` and initialize it to `0`.
* Loop through every character in the string.
* If the current Roman numeral is smaller than the next one, subtract its value from `total`.
* Otherwise, add its value to `total`.
* Return the final value of `total`.

---

# Dictionary Used

```python
roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
```

This dictionary lets us quickly find the integer value of any Roman numeral.

Example:

```python
roman["X"]
```

Output:

```python
10
```

---

# Dry Run

Input:

```python
s = "MCM"
```

Start:

```python
total = 0
```

### First Character

```text
M = 1000
```

Next character:

```text
C = 100
```

Since:

```python
1000 < 100
```

is `False`, add `1000`.

```python
total = 1000
```

---

### Second Character

```text
C = 100
```

Next character:

```text
M = 1000
```

Since:

```python
100 < 1000
```

is `True`, subtract `100`.

```python
total = 900
```

---

### Third Character

```text
M = 1000
```

There is no next character, so add it.

```python
total = 1900
```

Return:

```python
1900
```

---

# Complexity Analysis

* **Time Complexity:** `O(n)`

  We visit each character once.

* **Space Complexity:** `O(1)`

  The dictionary always contains exactly 7 key-value pairs.

---

# Concepts Used

* Strings
* Dictionaries (`dict`)
* Loops
* Conditions (`if` / `else`)
* String Indexing
* Comparison Operators

---

# LeetCode Link

https://leetcode.com/problems/roman-to-integer/
