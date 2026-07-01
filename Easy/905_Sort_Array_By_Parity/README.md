# 905. Sort Array By Parity

## Problem

Given an integer array `nums`, move all the even integers to the beginning of the array, followed by all the odd integers.

Return any array that satisfies this condition.

---

## Example 1

Input:

```python
nums = [3,1,2,4]
```

Output:

```python
[2,4,3,1]
```

Explanation:

* Even numbers: `2`, `4`
* Odd numbers: `3`, `1`

The even numbers come first, followed by the odd numbers.

---

## Example 2

Input:

```python
nums = [0]
```

Output:

```python
[0]
```

---

# Python Solution

```python
class Solution(object):
    def sortArrayByParity(self, nums):
        even = []
        odd = []

        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        return even + odd
```

---

# Approach

* Create two empty lists:

  * `even` to store even numbers.
  * `odd` to store odd numbers.
* Loop through every number in `nums`.
* If the number is even (`num % 2 == 0`), add it to the `even` list.
* Otherwise, add it to the `odd` list.
* Return the combined list using `even + odd`.

---

# Built-in Functions Used

### `append()`

Adds an element to the end of a list.

Example:

```python
numbers = [2,4]
numbers.append(6)

print(numbers)
```

Output:

```python
[2,4,6]
```

---

# Dry Run

Input:

```python
nums = [3,1,2,4]
```

Start:

```python
even = []
odd = []
```

Iteration 1:

```python
i = 3
```

`3 % 2 != 0`

```python
odd = [3]
```

Iteration 2:

```python
i = 1
```

```python
odd = [3,1]
```

Iteration 3:

```python
i = 2
```

```python
even = [2]
```

Iteration 4:

```python
i = 4
```

```python
even = [2,4]
```

Return:

```python
even + odd
```

↓

```python
[2,4,3,1]
```

---

# Complexity Analysis

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

where `n` is the number of elements in the array.

---

# Concepts Used

* Arrays (Lists)
* Loops
* Conditions (`if` / `else`)
* Modulo Operator (`%`)
* `append()`
* List Concatenation (`+`)

---

# LeetCode Link

https://leetcode.com/problems/sort-array-by-parity/
