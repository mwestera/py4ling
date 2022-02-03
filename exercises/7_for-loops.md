# Python for linguists


## 7. For-loops (`for`, `range`)

**7.1.** Another keyword that can create clauses, like `if`, is `for`. Try to understand what it does, with the following code. First make sure the variable `names` is still assigned the list of names `['Alf', 'Beth', 'Chris', 'Dave', 'Esra']`.

```python
for name in names:
    print(name)
```


**7.2.** Do for-clauses follow the same syntactic rules as if-clauses, e.g., with regard to indentation, the placement of the colon, and the effect of (lack of) newlines in between a for-clause and subsequent statements?

**7.3.** After executing the preceding code, what is now the value of the variable `name`? Do you understand why?

**7.4.** Write a program that loops over the list `names` from above and prints each element twice, using a `for`-loop with two `print` statements in its body.

**7.5.** In the previous example the variable `name` probably already existed before the for-clause was executed. Does this need to be the case? Try looping with a fresh variable.

**7.6.** Create a variable `num_names`, and loop over the list `names` again, this time incrementing the counter `num_names` by 1 for each element. Print `num_names` afterwards. Congratulations, you have re-implemented `len`!

**7.7.** Can you use an if-clause within a for-loop? Write a program to count how many odd numbers are in a list, printing the result.

**7.8.** Sum up all the even numbers in a list.

**7.9.** Sum up all the negative numbers in a list.

**7.10.** Write a program that takes a list of numbers, multiplies each element by 3 and appends the results to a new list. Does the new list have the same number of elements as the original list?

**7.11.** In the following example, how come the list `nums` doesn't change?

```python
nums = [1, 2, 3]
for x in nums:
    x *= 10

print(nums)
```


**7.12.** Write a program that prints all and only list elements with even indices (0, 2, 4, ...).

**7.13.** Count how many words in a list have length 5.

**7.14.** Sum all the elements in a list up to but not including the first even number. (What if there is no even number?)

**7.15.** Count how many words occur in a list up to and including the first occurrence of the word _the_. (What if _the_ does not occur?)

**7.16.** Write a program that counts the number of even digits in a number `n`.

- - - - - -
**Something to keep in mind:** In programming, an important part of the solution to any problem is often: how should I represent my data? For instance, should you represent a number as an int or as a string? If the goal is to do arithmetic, it makes sense to treat it as a number; but if the goal is to count digits, it can be helpful to first represent the number as a string.
- - - - -

**7.17.** Write a program that computes the sum of the squares of the numbers in the list `numbers`. For example a call with `numbers = [2, 3, 4]` should print the result of 4+9+16 which is `29`

**7.18.** Write a program that concatenates all words in the list `words = ['apple', 'pear', 'banana', 'strawberry']`, placing one after the other with dashes `-` in between.

**7.19.** Generalize the preceding program to allow changing the connector (e.g., dash, space, underscore) by assigning this to a variable `connector`.

**7.20.** It is often convenient (but equally often _not_ convenient!) to loop over consecutive numbers (0, 1, 2, 3, ...). A clumsy way to achieve this is to create a list of numbers and loop over those. Try this, and print each number.

**7.21.** A better way to loop over consecutive numbers is to use `range`, e.g., `for i in range(10)` loops over all integers from 0 to 9. Try this and verify that it works the same way.

**7.22.** Execute `help(range)` for more information (and remember to press `q` to quit). As you can see, you can construct a range with up to three arguments. What do the other arguments do? E.g., what happens if you loop over `range(3, 50, 5)`? And what about `range(100, 5, -3)`? Is there a relation between the three arguments of `range`, and the three integers you can specify when slicing a string or list?

**7.23.** Write a program that counts down from 10 all the way to 0, and then prints _Lift off!_.

**7.24.** Write a program that counts down from 10 down to -10 in steps of 2.

**7.25.** What happens if you iterate over an empty list? What happens if you iterate over an empty range, e.g., `range(0)`, or `range(56,56)`?

**7.26.** Can you think of advantages of using `range` instead of a list of numbers? Also consider limits of computer memory: what if you want to loop a billion gazillion times?

**7.27.** Can you create a `range` with non-integer steps, e.g., 0.1? What about using a float as a starting point or end point, is that allowed?

**7.28.** Remember that objects can sometimes be converted from one type to another. A `range` object can be converted to a `list`, e.g., `list(range(100))`. Try this. Can you also convert a list back to a range? What happens if you try, and why?

**7.29.** Compare `x = range(9999)` and to `x = list(range(9999))` (without printing the result). Keep increasing nines and try again, e.g., `99999`, `999999`, `9999999`, and beyond. At some point you will notice that the version `x = list(range(999...9)` gets much slower, while the version `x = range(999...9)` remains fast. Why would this be?

- - - - - -
**Something to keep in mind:** Try not to needlessly occupy memory and processing time: `range` lets you iterate over a sequence of integers without having to store the corresponding list of integers in memory.
- - - - -

**7.30.** Earlier we saw that if-clauses can be nested. What about for-clauses? Write a program that loops over the `names` list from earlier (`for name1 in names`), and nested within that loop, loops over the same list again (`for name2 in names`). In the body of the inner loop, print the two names stored in `name1` and `name2`, concatenated with a dash in between. What do you get?

**7.31.** Why did the inner loop use a different variable from the outer loop, namely `name2`? Modify the previous program to see what happens if the inner loop instead uses the same variable as the outer loop (i.e., `name`), and inside the inner loop simply print `name`. Do you understand what you see?

**7.32.** In the following example, how come the list `cities` doesn't change?

```python
cities = ['amsterdam', 'rotterdam', 'leiden', 'gouda']
for city in cities:
    city.capitalize()

print(cities)
```


**7.33.** What about now?

```python
cities = ['amsterdam', 'rotterdam', 'leiden', 'gouda']
for city in cities:
    city = city.capitalize()

print(cities)
```


**7.34.** Create nested loops to print all pairs of numbers between 0 and 10, but only if the first member is odd and the second even. Did you use an if-clause, or appropriate `range` objects?

**7.35.** Create nested loops to print all two-character strings where the first is a consonant and the second is a vowel.

**7.36.** Create nested loops to print all pairs of numbers between 0 and 10, where the second is higher than the first -- but crucially _without_ using `if`-statements!

**7.37.** Write a program that prints out the first `n` triangular numbers. For instance, with `n = 5`, it should print the result of 1+2+3+4+5, i.e., `15`.

**7.38.** Write a program which prints `True` when `n` is a prime number and `False` otherwise.

**7.39.** Create a _single_ (!) loop using `range` (without constructing a list first), that prints the numbers 0, 1, 2, ..., 23, repeating this five times. Remember how you handled the hours on a clock earlier?

**7.40.** Now program a clock with both hours and minutes, printing it as, e.g., `16:52`, and let it run for two 'days'. If it works, make it also display seconds, and run it for a few 'hours'.

- - - - - -
**Something to keep in mind:** When looping over a range of numbers in a particular way, choosing a smart `range` often results in more readable code than using if-statements inside the loop.
- - - - -

**7.41.** Can you change the setting of your clock to display times using `am` and `pm` instead of the 24-hour format, e.g., `4:52pm` instead of `16:52`?

**7.42.** Write a program that takes a list of words like `words = ['the', 'dog', 'is', 'in', 'the', 'garden']`, takes the length of each word, and prints the total sum of word lengths. Do you get the same number as `len('the dog is in the garden')`? Why (not)? What about `len(words)`?

