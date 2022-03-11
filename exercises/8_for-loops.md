# Python for linguists


## 8. For-loops (`for`)

**8.1.** Another keyword that can create clauses is `for`. Try to understand what it does, with the following code. First make sure the variable `names` is still assigned the list of names `['Alf', 'Beth', 'Chris', 'Dave', 'Esra']`.

```python
for name in names:
    print(name)
```


**8.2.** Is indentation meaningful in the case of for-clauses, too? Verify this empirically.

**8.3.** After executing the above code, do you expect that the variable `name` has a value? If so, which value? Test this and make sure you understand what is going on.

**8.4.** Write a program that loops over the list `names` from above and prints each element twice, using a `for`-loop with two `print` statements in its body.

**8.5.** What happens if the variable `name` already exists before executing the for-loop? (Perhaps this was already the case in the previous exercises.)

**8.6.** Write a function `print_multiple` that is given a list, and prints each element of the list, each on a new line.

**8.7.** Write a function `print_multiple_oneline` that is given a list, and prints all list elements on a single line, concatenated with dashes in between. You can either first compose a long string and call `print` only once at the end, or use repeated `print` statements and control the layout with the help of its `end` parameter.

**8.8.** Modify the original `print_multiple` to take an additional boolean argument `oneline`, such that `print_multiple([1, 2, 3], True)` prints all numbers on one line, and `print_multiple([1, 2, 3], False)` prints each number on a new line.

**8.9.** You can also initialize a variable outside the for-loop, and then modify or reassign something to it on each iteration within the for-loop. Use this to write a function that takes a list `numbers`, and loops through it to compute the sum of the squares of the numbers, returning it in the end. For example a call with `[2, 3, 4]` as an argument should return the result of 4+9+16 which is `29`

**8.10.** Define a function `length` that takes a list as input and returns its length, _without_ using the built-in function `len`.

**8.11.** Write a function that takes a list of words and concatenates them, placing one after the other with dashes `-` in between, and returns (not prints) the resulting string. (Try not to use built-in functions other than those introduced so far.)

**8.12.** Generalize the preceding function to allow changing the separator (e.g., dash, space, underscore) by giving the function an extra parameter `sep`.

- - - - - -
**Something to keep in mind:** After defining a function, make sure to _test_ it thoroughly by calling it with various arguments. After verifying that it works, you can easily comment out (with `#`) the test function calls, while leaving the function definition itself untouched. This lets you conveniently work in a single file for all the exercises, without all the previous functions being called every time you test the latest function. Later we will learn how to separate the test calls from the function definitions.
- - - - -

**8.13.** Can you use an if-clause within a for-loop? Write a function to count how many odd numbers are in a list, returning the result.

**8.14.** Define a function that sums up all the even numbers in a list, returning the result.

**8.15.** Define a function that sums up all the negative numbers in a list, returning the result. As always, try to use a clear, transparent function name.

**8.16.** Write a function that takes a list of numbers, multiplies each element by 3 and appends the results to a new list. Does the new list have the same number of elements as the original list?

**8.17.** Write a function that takes a list of words, and an integer, and counts how many words in the list have a length of at least that integer.

**8.18.** One way to escape a loop early, at least inside a function definition, is the `return` statement. Write a function that sums all the elements in a list up to, and including, the first even number, and then returns the result right away (skipping the rest of the list). (What if there is no even number in the list?)

**8.19.** Extend the previous function with a boolean parameter `inclusive`: setting it to False should result in summing up to, but _excluding_, the first even number.

**8.20.** Write a function that counts how many words occur in a list up to (and including) the first occurrence of the word _the_.

**8.21.** Just as you can loop through a list, you can loop through the characters of a string. Write a function `even_vowel_count` that uses a loop to count the number of vowels in a string, and returns a boolean that indicates whether that number is even or not.

**8.22.** Did you remember to add docstrings to your functions?

**8.23.** Write a function that counts the number of even digits in a number `n`, e.g., the number `5671238` has 3 even digits (6, 2 and 8).

**8.24.** The keyword `for` also appears in a powerful and 'Pythonic' pattern called **list comprehension**. With a single line of code, it lets you construct a new list from an old one by changing or filtering the original elements. Try to predict (and test) what the following do:
- Let `numbers = [9, 5, 8, 3, 2, 6]`, and try `[n for n in numbers if n > 4]` 
- Assuming you still have `names` assigned: `[s[0] for s in names]` (if you were to assign the result to a variable, what would be a fitting variable name?) 
- `[name[::-1] for name in names]` 
- `[s for s in names if s[0].lower() in 'aeiou']` (try to describe what this means, in plain English)

**8.25.** Use list comprehension to take a list of words, and construct a list of the same words but in full capitals. Does your code demonstrate that strings are mutable? Does it demonstrate that lists are mutable?

**8.26.** Use list comprehension to take a list of numbers, and return a list of squares of those numbers, but only of those numbers which were even.

**8.27.** Use list comprehension to create a list containing all names in the list `names` that are at least 3 characters long. Also use list comprehension to create a list of integers that indicate, for each name in the original `names`, how many characters it contains.

- - - - - -
**Something to keep in mind:** With list comprehension a _lot_ can be done in a single, compact line of code, and with great power comes great responsibility. Compact code is never in itself a goal; code must be _readable_ above all else. Therefore, use list comprehension only if you think this makes the code more readable than e.g. a multi-line `for`-loop. This is only the case, typically, if the modification or filtering condition you want to apply is sufficiently simple. In general: don't write 'clever' code; write _clear_ code.
- - - - -

**8.28.** Redo the previous two exercises _without_ list comprehension, by using an ordinary multi-line for-loop. Which version do you find more readable?

**8.29.** Use list comprehension to write a function that takes two lists, `source` and `filter`, and returns a new list that is exactly like `source` but with all elements removed that are not in `filter`. Test at least an example where the resulting list should be equivalent to the filter, and an example where it should not be.
