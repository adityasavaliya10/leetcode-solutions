# 509. Fibonacci Number

## Problem Statement

The Fibonacci numbers are defined as follows:

- `F(0) = 0`
- `F(1) = 1`
- `F(n) = F(n - 1) + F(n - 2)`, for `n > 1`

Given an integer `n`, return `F(n)`.

├── fib(3)
│   ├── fib(2)
│   │   ├── fib(1) = 1
│   │   └── fib(0) = 0
│   │   => fib(2) = 1
│   └── fib(1) = 1
│   => fib(3) = 2
└── fib(2)
    ├── fib(1) = 1
    └── fib(0) = 0
    => fib(2) = 1

fib(4) = 2 + 1 = 3
