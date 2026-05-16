# Kids With the Greatest Number of Candies 

This repository contains my Python solution to the LeetCode problem **1431. Kids With the Greatest Number of Candies**.

##  Problem Statement

Given an array `candies`, where each element represents the number of candies a child has, and an integer `extraCandies`, determine for each child whether they can have the greatest number of candies among all children if they are given all the extra candies.

Return a list of boolean values:
- `True` if the child can have the greatest number of candies.
- `False` otherwise.

##  Approach

1. Find the maximum number of candies currently owned by any child.
2. Iterate through each child.
3. Add `extraCandies` to the child's candies.
4. Check if the total is greater than or equal to the maximum.
5. Append `True` or `False` to the answer list.
