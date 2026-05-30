# 2469. Convert the Temperature

## Problem

You are given a non-negative floating-point number rounded to two decimal places, representing the temperature in Celsius.

You should convert Celsius into:

1. Kelvin
2. Fahrenheit

Return the result as an array `[kelvin, fahrenheit]`.

---

## Example 1

Input:

```python
celsius = 36.50
```

Output:

```python
[309.65000, 97.70000]
```

Explanation:

- Kelvin = 36.50 + 273.15 = 309.65
- Fahrenheit = 36.50 × 1.80 + 32.00 = 97.70

---

## Example 2

Input:

```python
celsius = 122.11
```

Output:

```python
[395.26000, 251.79800]
```

---


# Approach

- Convert Celsius to Kelvin using:

  ```text
  Kelvin = Celsius + 273.15
  ```

- Convert Celsius to Fahrenheit using:

  ```text
  Fahrenheit = Celsius × 1.80 + 32.00
  ```

- Return both values in a list.

---

# Complexity Analysis

- Time Complexity: `O(1)`
- Space Complexity: `O(1)`

---

# LeetCode Link

https://leetcode.com/problems/convert-the-temperature/
