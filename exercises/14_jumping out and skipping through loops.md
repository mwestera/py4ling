# Python for linguists


## 14. Jumping out and skipping through loops (`break`, `while`, `continue`, `range`)

**14.1.** We have seen before that `return` can be used (inside a function) to escape a loop when some condition has been met, causing the rest of the elements looped over to be skipped. Escaping a loop early is an important programming pattern to acquire, as it often results in cleaner and more efficient code. As a warming up, review your own solutions to the exercises of section 8 that involved this pattern.

**14.2.** What is wrong with the following function? Can you fix it? **Note:** In this and the following exercises, for the sake of practicing the main topics of this section, stick to the multi-line loop structure (e.g., don't use list comprehension, `sum`, or `any` and `all`, about which we will learn in a later section).

```python
def has_any_odd(numbers):   # Note: The docstring is a lie.
    """
    Returns True if the list of numbers has any odd number; False otherwise.
    """
    for number in numbers:
        if number % 2 == 1:
            return True
        else:
            return False
```


**14.3.** Write a function `has_any_vowel` that takes a _string_ as argument, and returns `True` if it contains at least one vowel, and `False` if it contains no vowels. Does your function ever inspect more list elements than necessary to reach a conclusion? If so, try to streamline your function.

**14.4.** Write a function `has_only_odd` that takes a list of integers as argument, and returns `True` if all numbers in the list are odd, and `False` otherwise.

**14.5.** Write a function `has_three_odd` that takes a list of integers as argument, and returns `True` if, and only if, at _least_ three numbers in the list are odd.

**14.6.** Write a function `has_at_most_n_vowels` that takes a list of strings and a number `n` as argument, and returns `True` if, and only if, there are no more than `n` vowels in the list of strings (also looking inside individual strings).

- - - - - -
**Something to keep in mind:** Whereas `return` lets you escape from a function (hence also from any intervening loop), `break` is more specialized: it lets you escape only the immediately enclosing loop, nothing else. This means that `break` is in many cases more suitable than `return`; we will review some cases below, after some initial practice.
- - - - -

**14.7.** Execute the following code and try to understand the output:

```python
names = ['Alf', 'Beth', 'Chris', 'Dave', 'Esra']

for name in names:
    print('Checking:', name)
    if name[0].lower() not in 'aeiou':
        print('Got one!')       # Beth is the first consonant person, and the only printed name
        break
```


**14.8.** How many names do you expect this loop to print? Test your expectation.

```python
for name in names:
    print(name)
    break
```


**14.9.** And this one?

```python
for name in names:
    break
    print(name)
```


**14.10.** Try to predict the output of the following program, then test your expectation:

```python
for name in names:
    if len(name) > 4:
        break
    print(name)
```


- - - - - -
**Something to keep in mind:** As mentioned, `break` can often be more suitable than `return` for escaping a loop. For one, `return` is only available inside a function (but most code should be organized in functions so that's not a real limitation). In addition, `return` is not suitable for escaping a loop if the function should still do some further processing _after_ escaping the loop (see next exercise), instead of return right away. Relatedly, if `return` occurs inside nested loops, it escapes _all_ enclosing loops at once, whereas `break` escapes only the directly enclosing loop. Some programmers take a more principled stance: `break` would be preferable in almost all cases because it results in cleaner code, as it wears its purpose on its sleeve: `break` was _designed_ for breaking out of loops.
- - - - -

**14.11.** Write a function `print_until_vowel` that takes a list of strings, and prints all strings until one is encountered that begins with a vowel, in which case it should break out of the loop and end by printing `Done!` (the latter makes `break` more suitable than `return` in this case).

**14.12.** To practice with 'default arguments' from an earlier section: give your function `print_until_vowel` a boolean parameter `inclusive`, with `True` as a default value. If this parameter is set to True, the string that begins with a vowel should also itself be printed; if it is set to False, only the strings that precede it should be printed.

**14.13.** Write code with nested loops to illustrate one of the differences between `return` and `break` mentioned above: that `return` escapes all enclosing loops, whereas `break` escapes only the directly enclosing loop.

**14.14.** What happens if you use `break` in some other place in your code, not inside a loop?

**14.15.** What is wrong with the following code (analogous to the example with `return` above)? Can you fix it? (Maintaining the printout of 'Zero odd numbers here!' in the negative case can be a bit tricky.)

```python
def print_whether_has_any_odd(numbers): # the docstring is a lie
    """
    Prints whether or not the list contains an odd number, and 'Done!' afterwards.
    """
    for number in numbers:
        if number % 2 == 1:
            print('It has an odd number!')
            break
        else:
            print('Zero odd numbers here!')
            break
    print('   ...really!')    # this final command is mainly why we use break to escape the loop, not return
```


**14.16.** Fixing the preceding code is easier if you know that `for` clauses can actually be combined with an `else` clause, just like `if` can. Consider the following fix, and notice the indentation ensuring that the `else` belongs with the `for`, not with the `if`. Does it work correctly?

```python
def print_whether_has_any_odd_2(numbers):
    for number in numbers:
        if number % 2 == 1:
            print('It has an odd number!')
            break
    else:
        print('Zero odd numbers here!')
    print('   ...really!')
```


- - - - - -
**Something to keep in mind:** Similar to if-clauses, for-loops can have an `else`-clause too. The else-clause of a for-loop is executed only if the for-loop finishes _without_ any `break`. Typically (but not always) `break` represents that some target element, that meets some criterion, has been found (e.g., the first odd number, the third name that begins with a vowel...). Therefore, you can often read the `else`-clause of a for-loop as "if no such element was found...". (If you pronounce it simply as 'else', it can be confusing.)
- - - - -

**14.17.** Can a single loop contain multiple `break` statements, e.g., in different if-clauses? Can you think of an (imaginary) use-case where one might need this?

**14.18.** _(You can do this and the next two exercises all at once, or one at a time.)_ A rich client needs four functions, that each take a nested _list of lists_ of numbers as parameter and return a boolean. One checks if _some_ (any) inner list contains an odd number (return True if so, False otherwise). The second checks if some inner list contains _only_ odd numbers. The third checks if _each_ inner list contains an (any) odd number. The fourth checks if _each_ inner list contains _only_ odd numbers. Implement a first version of these functions, where each function is self-contained and does _not_ rely on auxiliary functions (e.g., `has_any_odd` from before). Each function will, therefore, contain nested loops.

**14.19.** Our client cares a lot of about efficiency (but insists on using Python). Do all of your loops escape early where possible?

**14.20.** Our client also cares a lot about readability, and hates repetition. Improve the four functions such that each contains only a single (non-nested) loop, within which some auxiliary function is called that does the rest (e.g., `has_any_odd` from before, and you may need to define another).

**14.21.** Besides `break` (and to some extent `return`), another keyword that helps you control your loops is `continue`. It lets you skip an element. Can you predict what the following code prints? Test your prediction and verify your understanding.

```python
for i in range(10):
    if i % 2 == 0 or i % 5 == 0:
        continue
    print(i)
```


**14.22.** What `continue` achieves can also be done with an if-clause alone, without `continue`. Show this by re-implementing the above `for i in range(10)` example _without_ using `continue`.

**14.23.** The foregoing notwithstanding, sometimes `continue` is considered preferable to a plain if-clause. A typical use case is to filter out cases that don't need to be processed, right at the start of the body of a for-loop. This is particularly desirable if the body of your loop is substantial. Compare program 1 and 2 in the code below (verify that the result is the same). In Program 1 the body is more deeply nested (under the if-clause), which means more stuff to keep in working memory as you try to understand the code. In Program 2, the body is less deeply nested, and `continue` directly, transparently signals that certain cases can simply be ignored, which is easier on our working memory.

```python
# Program 1, not using continue:
for i in range(1000):
    if i % 3 == 0:
        print(i)
        ... # imagine a substantial program here

# Program 2, using continue:
for i in range(1000):
    if i % 3 != 0:
        continue        # exception-status immediately clear

    print(i)
    ... # main program is now not as deeply nested, which is also nice
```


<br>**_Looping with `while`_**

**14.24.** The `while` keyword lets you loop in a way that is different from for-loops. Run the following and make sure you understand what's happening. As before, try to break it in various ways.

```python
counter = 0
while counter < 10:
    print(counter)
    counter += 1
```


**14.25.** Write a program that does the same, but using a `for`-loop instead of the `while`-loop above (this is not just a matter of replacing the keyword; more things have to change).

- - - - - -
**Something to keep in mind:** For the above use-case, where you know in advance how often to repeat something, for-loops are normally the way to go. But **while-loops** can be convenient if you don't quite know how long to loop, e.g., until some unpredictable condition is met, such as a particular user input. We will see some examples of this.
- - - - -

**14.26.** If a program keeps on running, do you know how to intervene to stop it? In the Python Console this is often the keyboard shortcut `ctrl`+`c` or `cmd`+`c`; when executing a script it may be `ctrl`+`F2`, but the PyCharm IDE also has a visual stop button for this (red square).

**14.27.** In the above while-loop, replace the condition (`counter < 10`) simply by `True`. What do you expect will happen? Do you see the importance of the previous exercise?

**14.28.** Write a function that repeatedly gets numbers from the user (using the `input` function), until the user enters _done_. Once _done_ is entered, print out the total, count, and average of the numbers. You can assume the user will only enter either `done` or a valid number.

**14.29.** Write a number guessing game. Start your program with `import random`. Write a function that contains `number = random.randint(100)` (what does it do?), followed by a loop asking the user to guess that number. Upon each guess (you can assume the user enters only valid numbers), the program prints whether it is too high or too low, or, if the guess is exactly right, exit the loop and print _Congratulations! You won in [n] guesses!_ where _n_ is the number of guesses.

**14.30.** Use `continue` to make your number guessing game, from the exercise above, more user-friendly: if the user enters anything other than a number, skip ahead (with the effect of asking for new input right away). You can use the string method `is_numeric`, which returns True if the string contains only numeric digits.

<br>**_Looping over `range`_**

**14.31.** We have already used `range` to loop over a range of integers, e.g., `for i in range(10):`, but `range` is quite a bit more flexible. Execute `help(range)` in the Python console for more information (and remember to press `q` to quit). As you can see, you can construct a range with up to three arguments. What do the other arguments do? E.g., what happens if you loop over `range(3, 50, 5)`? And what about `range(100, 5, -3)`? Is there a relation between the three arguments of `range`, and the three integers you can specify when slicing a string or list?

**14.32.** Write a function that counts down from 10 to 1, and then prints _Lift off!_. (Consider printing all numbers on the same line, to more easily keep an overview in your printed output. Also consider adding `flush=True` to a print statement now and then, so you don't have to scroll all the way up to see an error message.)

**14.33.** Generalize the preceding function by providing it a start and a step parameter, where the default start is 10 and the default step is -1. Use it to count down from 20 in steps of 2.

**14.34.** Define a function that uses nested loops to print all pairs of numbers, each between 0 and 10 (inclusive), where the first is odd and the second is even. Did you use if-clauses inside the loops, or did you solve it with particular `range` objects instead?

**14.35.** Define a function that uses nested loops to print all pairs of numbers, each between 0 and 10 (inclusive), where the second is higher than the first -- but, for the sake of practice, _without_ using an `if`-statement (hint: the inner loop can use a range of which the starting point is determined by the outer loop). (Can you reason about how many such pairs there will be?)

- - - - - -
**Something to keep in mind:** When you need to loop over a range of numbers in a particular way, choosing a smart `range` can sometimes result in more readable code than using if-statements inside the loop, especially in list comprehensions.
- - - - -

**14.36.** Write a function that takes a list, and returns a new list containing all elements that occurred at even indices (0, 2, 4, ...) in the original list. Write a version that uses a multi-line loop, and a version with only list comprehension.

**14.37.** Write a function that takes a list and returns a new list containing all non-overlapping _pairs_ of elements in the original list. So for input `[1, 2, 3, 4, 5, 6]` it would return `[(1, 2), (3, 4), (5, 6)]`. Try two variants: a multi-line loop and list comprehension. Which do you find more readable in this case?

**14.38.** Generalize the foregoing function with an integer parameter `n`, returning the list of non-overlapping n-tuples (pairs, triples, quadruples, etc.). This is likely too complex for a single-line list comprehension. Moreover, you will likely need two `range` objects, one for looping through the list, one for constructing each tuple (from index `i` to index `i + n`). Remember from the previous section that constructing a tuple using list comprehension requires an explicit `tuple(...)` expression.

**14.39.** Can you create a `range` with non-integer steps, e.g., 0.1? What about using a float as a starting point or end point, is that allowed? Can you think of a more indirect way to nevertheless achieve such things (e.g., float steps or start/end points) whilst still using `range`?

**14.40.** Define a function that takes an integer parameter `n` and uses a _single_ loop to repeatedly, `n` times, print the numbers 0, 1, 2, ..., 23 (as if `n` days pass on a 24-hour clock).

**14.41.** Remember that objects can sometimes be converted from one type to another. A `range` object can be converted to a `list`, e.g., `list(range(100))`. Try this. Can you also convert a list back to a range? What happens if you try, and why might this be?

**14.42.** In the Python console compare `x = range(9999)` to `x = list(range(9999))` (without printing the result). Keep increasing nines and try again, e.g., `99999`, `999999`, `9999999`, and beyond (take it easy, don't crash your computer). At some point you will notice that the version `x = list(range(999...9)` gets much slower, while the version `x = range(999...9)` remains fast. Why would this be?

**14.43.** If you do `import sys`, you can access various operating-system-related functions in Python. One of these is the function `sys.getsizeof`. First call `help` on this function to read what it does. Then use the function to compare `range(9)` to `range(9999)`, and `list(range(9))` to `list(range(9999))`. Do your findings align with your answer to the previous exercise?

**14.44.** We have a micro-computer with a tiny display of 8 by 8 pixels, each of which can only be either on or off. We received what appears to be a secret message: `0000000000110110011111110011111000011100000010000000000000000000`. Write a function that takes such strings and prints them to a (simulated) 8 by 8 display, each pixel represented by a one-character space, rendering a `0` as an empty space ` `, and a `1` as a hashtag `#` (use a dictionary to implement this mapping, rather than if-statements). If you like, compose your own reply.

<br>**_Wrapping up_**

**14.45.** To conclude this section, in the Python console enter `import keyword` and then print `keyword.kwlist` (we will learn the details of `import` later). For which of these keywords do you already know some purpose? Try to summarize your understanding, especially of the keywords central to this section (`break`, `continue`, `return`, `for`, `while`): what is the purpose of each of these keywords?

- - - - - -
**Something to keep in mind:** **Keywords** are core language constructs handled by the syntactic parser before Python code is interpreted. Keywords are _reserved_ and cannot be used as ordinary variables, e.g., reassigned new values. **Built-ins** are commonly used, preloaded functions (e.g., `print`, `round`) and classes (e.g., `list`, but also various error classes such as `TypeError` -- if you encounter a TypeError, it is an instance of this class).
- - - - -

**14.46.** Test that keywords are indeed special, reserved expressions, by showing that trying to assign something to a keyword leads to an error.

**14.47.** Unlike keywords, built-ins are assigned to ordinary variables, hence these can be reassigned new values. For instance, try `print = 'bla'` and subsequently try to print something, like `print('apple')`. Overriding builtins like this is not a good idea. (If you did this in the Python console, consider restarting it now to prevent confusing your future self.)

**14.48.** Built-in functions are in fact shortcuts for objects you can also find in `__builtins__`. Try printing `__builtins__`. Depending on implementation it is either of type `module` (the type of thing that results from `import`, about which we will learn later) or a dictionary. In fact, in PyCharm, `__builtins__` in the Python Console is equivalent to `__builtins__.__dict__` in a script. Do `print(dir(__builtins__))` in a script (`dir` lists the contents of a module), or `print(list(__builtins__))` in the Python console (to list the keys of the dictionary). For which of the built-ins do you already know some purpose?

