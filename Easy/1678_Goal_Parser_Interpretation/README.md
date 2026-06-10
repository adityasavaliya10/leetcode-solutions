# 1678. Goal Parser Interpretation

## Problem

You own a Goal Parser that can interpret a string `command`.

The command consists of the following patterns:

- `"G"` -> `"G"`
- `"()"` -> `"o"`
- `"(al)"` -> `"al"`

The interpreted strings are then concatenated in the original order.

Given the string `command`, return the Goal Parser's interpretation of `command`.

---

## Example 1

Input:

```python
command = "G()(al)"
```

Output:

```python
"Goal"
```

Explanation:

```text
G     -> G
()    -> o
(al)  -> al
```

Result:

```text
Goal
```

---

## Example 2

Input:

```python
command = "G()()()()(al)"
```

Output:

```python
"Gooooal"
```

---

## Example 3

Input:

```python
command = "(al)G(al)()()G"
```

Output:

```python
"alGalooG"
```

---

# Python Solution

```python
class Solution(object):
    def interpret(self, command):
        command = command.replace("()", "o")
        command = command.replace("(al)", "al")

        return command
```

---

# Approach

- Replace every `"()"` with `"o"`
- Replace every `"(al)"` with `"al"`
- Return the modified string

---

# Built-in Function Used

### `replace()`

Replaces all occurrences of a substring with another substring.

Example:

```python
text = "hello world"
print(text.replace(" ", "-"))
```

Output:

```python
hello-world
```

---

# Dry Run

Input:

```python
command = "G()(al)"
```

After first replacement:

```python
"Go(al)"
```

After second replacement:

```python
"Goal"
```

Return:

```python
"Goal"
```

---

# Complexity Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`

where `n` is the length of the string.

---

# Concepts Used

- Strings
- replace()
- Variable Updating

---

# LeetCode Link

https://leetcode.com/problems/goal-parser-interpretation/
