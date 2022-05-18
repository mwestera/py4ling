---
geometry: "left=3cm,right=3cm,top=2.5cm,bottom=2cm"
---

### Name: ________________

## Python for Linguists

### Mini-exam 11


**Question 1. [6 points]** What do the following expressions evaluate to? Please write the result next to (or under) each expression.

---

```python
list(enumerate('abc'))


list(zip(range(5), 'abc'))


list(enumerate(range(3)))


list(zip(range(2), range(3)))


list(zip('abc', 'def'))


list(zip(range(0, 6, 2), range(1, 7, 2)))


```

**Question 2. [3 points]** Suppose `number` contains an integer. Write a _single-line_ expression, using `any` and `range`, that evaluates to True if `number` is a prime number, and False otherwise. (Recall that you can use `m % n == 0` to mean: `m` is divisible by `n`.)