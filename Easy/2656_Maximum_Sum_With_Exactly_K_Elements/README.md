# 2656. Maximum Sum With Exactly K Elements

## Problem

You are given an integer array `nums` and an integer `k`.

You must perform exactly `k` operations.

In each operation:

1. Choose the largest element from the array.
2. Add it to your answer.
3. Increase that element by `1`.
4. Put it back into the array.

Return the maximum possible sum after performing exactly `k` operations.

---

## Example 1

Input:

```python
nums = [1,2,3,4,5]
k = 3
```

Output:

```python
18
```

Explanation:

* Pick `5` → Sum = `5`, number becomes `6`
* Pick `6` → Sum = `11`, number becomes `7`
* Pick `7` → Sum = `18`, number becomes `8`

Return:

```python
18
```

---

## Example 2

Input:

```python
nums = [5,5,5]
k = 2
```

Output:

```python
11
```

Explanation:

* Pick `5` → Sum = `5`, number becomes `6`
* Pick `6` → Sum = `11`

Return:

```python
11
```

---

# Python Solution

```python
class Solution(object):
    def maximizeSum(self, nums, k):
        maximum = max(nums)
        total = 0

        for i in range(k):
            total += maximum
            maximum += 1

        return total
```

---

# Approach

* Find the largest number in the array using `max()`.
* Store it in the variable `maximum`.
* Create another variable `total` to store the answer.
* Repeat exactly `k` times:

  * Add `maximum` to `total`.
  * Increase `maximum` by `1`.
* Return `total`.

---

# Built-in Functions Used

## `max()`

Returns the largest element in a list.

Example:

```python
nums = [4,8,2,9]

print(max(nums))
```

Output:

```python
9
```

---

# Dry Run

Input:

```python
nums = [1,2,3,4,5]
k = 3
```

Start:

```python
maximum = 5
total = 0
```

### Iteration 1

```python
total = 5
maximum = 6
```

### Iteration 2

```python
total = 11
maximum = 7
```

### Iteration 3

```python
total = 18
maximum = 8
```

Return:

```python
18
```

---

# Why don't we update the array?

Suppose the array is:

```python
[1,2,3,4,5]
```

After choosing `5`, it becomes:

```python
[1,2,3,4,6]
```

The same element is still the largest.

Next it becomes:

```python
7
```

Then:

```python
8
```

So instead of changing the array every time, we only keep track of the current largest value using:

```python
maximum += 1
```

This makes the solution simpler and more efficient.

---

# Complexity Analysis

* **Time Complexity:** `O(n + k)`

  * `O(n)` to find the maximum element.
  * `O(k)` to perform the operations.

* **Space Complexity:** `O(1)`

---

# Concepts Used

* Arrays (Lists)
* `max()`
* Loops
* Variables
* Simulation
* Arithmetic Operations

---

# LeetCode Link

https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/
