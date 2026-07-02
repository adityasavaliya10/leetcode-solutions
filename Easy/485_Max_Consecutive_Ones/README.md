# 485. Max Consecutive Ones

## Problem

Given a binary array `nums`, return the maximum number of consecutive `1`s in the array.

A binary array contains only `0`s and `1`s.

---

## Example 1

Input:

```python
nums = [1,1,0,1,1,1]
```

Output:

```python
3
```

Explanation:

The consecutive groups of `1`s are:

```text
1 1 | 0 | 1 1 1
```

The longest group contains **3** consecutive `1`s.

---

## Example 2

Input:

```python
nums = [1,0,1,1,0,1]
```

Output:

```python
2
```

Explanation:

The consecutive groups of `1`s are:

```text
1 | 0 | 1 1 | 0 | 1
```

The longest group contains **2** consecutive `1`s.

---

# Python Solution

```python
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        current = 0
        maximum = 0

        for num in nums:
            if num == 1:
                current += 1

                if current > maximum:
                    maximum = current
            else:
                current = 0

        return maximum
```

---

# Approach

* Create two variables:

  * `current` to count the current consecutive `1`s.
  * `maximum` to store the largest count found so far.
* Loop through every number in the array.
* If the number is `1`, increase `current` by `1`.
* If `current` becomes greater than `maximum`, update `maximum`.
* If the number is `0`, reset `current` to `0` because the consecutive sequence has ended.
* Return `maximum`.

---

# Dry Run

Input:

```python
nums = [1,1,0,1,1,1]
```

Start:

```python
current = 0
maximum = 0
```

Iteration 1:

```python
num = 1
```

```python
current = 1
maximum = 1
```

Iteration 2:

```python
num = 1
```

```python
current = 2
maximum = 2
```

Iteration 3:

```python
num = 0
```

```python
current = 0
maximum = 2
```

Iteration 4:

```python
num = 1
```

```python
current = 1
maximum = 2
```

Iteration 5:

```python
num = 1
```

```python
current = 2
maximum = 2
```

Iteration 6:

```python
num = 1
```

```python
current = 3
maximum = 3
```

Return:

```python
3
```

---

# Complexity Analysis

* **Time Complexity:** `O(n)`

  We visit each element exactly once.

* **Space Complexity:** `O(1)`

  Only two variables (`current` and `maximum`) are used.

---

# Concepts Used

* Arrays (Lists)
* Loops
* Conditions (`if` / `else`)
* Variables
* Counting
* Finding the Maximum Value

---

# LeetCode Link

https://leetcode.com/problems/max-consecutive-ones/
