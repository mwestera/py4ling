# Python for linguists


## 6. Defining and calling functions (`def`, `return`)

**6.1.** In a python script, enter the following code to define a function with the name `print_spam` and subsequently _call_ it (do you remember why there is a backslash in the strings at `I\'m`?):

```python
print('I\'m going to define a function.')

def print_spam():
    print('spam')


print('Now I\'m going to call the function, pay attention:')
print_spam()
```


**6.2.** A function definition is a clause, just like an if-clause and a for-clause. What is its head and what is its suite/body?

**6.3.** What happens in the above example if there is only one empty line after the function definition? What if there is no empty line after the function definition? What if the last two print statements in the above example are indented too?

**6.4.** What happens if you define a function but don't call it? What happens if you forget the parentheses in the function call, i.e., `print_spam`?

**6.5.** Can a function contain multiple statements in its body? Can you call the same function multiple times?

**6.6.** What did you think will happen if your script calls a function _before_ defining it (i.e., in the .py file, the definition comes after the call)? Test your expectation.

**6.7.** What happens if you change the name of the function in the definition, but forget to update the function call?

**6.8.** When defining a function, you can give it **parameters**, enabling it to be called with **arguments**. Make sure you understand the following:

```python
def print_twice(word):
    print(word)
    print(word)


print_twice("bla")
```


**6.9.** What happens if you accidentally call the original `print_spam`, which has no parameters, with an argument, e.g., `print_spam('testing')`?

**6.10.** Define and call a function `print_inverted` that is given a word, and prints the word back-to-front (e.g., _apple_ is printed as _elppa_).

**6.11.** Does a function definition (a def-clause) follow the same indentation rules as an if-clause and a for-clause?

**6.12.** Functions can not only take inputs and do stuff, they can also output stuff, using the `return` keyword. The following code does not print `aaah!`. Make the program print `aaah!` without changing the function definition.

```python
def create_scream():
    return 'aaah!'


create_scream()
```


**6.13.** Define and call a function `invert` that takes a word, and returns a new string containing that word back-to-front (that is, like `print_inverted`, but instead of printing the inverted word, it returns it). When calling the function, assign the returned value to a variable and print it.

**6.14.** What do you expect `type(create_scream())` and `type(invert())` to be? And what is the type of a function call that does not return anything, e.g., `print_spam()` above?

**6.15.** Explain the difference between `type(create_scream())` and `type(create_scream)`; and between `type(print_spam())` and `type(print_spam)`.

**6.16.** What happens if a single function contains multiple different `return` statements (e.g., `return 'haha!'` and `return 'hehehe...'`)?

**6.17.** Define and call a function that both prints a string and returns another string (against recommended practice).

- - - - - -
**Something to keep in mind:** As a rule of thumb, every function should either _compute_ stuff (return a new object) or _do_ stuff (e.g., print stuff, modify an existing object), not both. Functions that return stuff are sometimes called fruitful functions; functions that only do stuff are sometimes called procedures. A function that does both is said to have _side effects_, which is considered an anti-pattern in programming.
- - - - -

**6.18.** Functions can also have multiple parameters, hence be called with multiple arguments. Write a function that takes three numbers and returns their sum, and a function that takes three numbers and returns their average.

**6.19.** What happens if you define a function with one parameter (like `invert` above), but wrongly call the function as if it has two parameters (e.g., `invert('abc', 'def')`)? What if you call it with no arguments (`invert()`)?

**6.20.** Write a function `is_palindrome` that takes a word, and checks if it is a palindrome, returning `True` or `False` accordingly. Can you implement a version that uses your `invert` function from above?

**6.21.** Write a `compare` function with two parameters `a` and `b`, that returns `1` if `a > b`, `0` if `a == b`, and `-1` if `a < b`. Examples:
- `compare(5, 4) == 1` 
- `compare(7, 7) == 0` 
- `compare(2, 3) == -1`

**6.22.** Write a function called `hypotenuse` that returns the length of the hypotenuse (Dutch: 'schuine zijde') of a right triangle, given the lengths of the two legs adjacent to the right angle as parameters. Examples: `hypotenuse(3, 4) == 5.0`, `hypotenuse(24, 7) == 25.0`.

**6.23.** It is easy to misunderstand or forget what a function is supposed to be doing, even if you yourself wrote it. To avoid this you should _document_ your code. Adding informative (non-redundant, non-avoidable) `#`-comments is one way. Another, very important way to document your code is with so-called **docstrings** (documentation strings): a string object that occurs in the first line(s) of a function definition. Try this:

```python
def sum_three_numbers(a, b, c):
	"""Takes three integers or floats and returns their sum."""
	return a + b + c
```


**6.24.** Python internally handles docstrings by storing them as properties of the function, in a special field `___doc__`. Try `print(sum_three_numbers.__doc__)`. Docstrings are accessed, for instance, by the `help` function; try `help(sum_three_numbers)` (remember you can press `q` to quit the help).

**6.25.** Docstrings are customarily defined using three double-quotation marks (`"""..."""`). Do you remember how they handle newlines? Can you also also define docstrings using single double-quotation marks (`"..."`), i.e., does the `help` function still pick it up? What about using three single-quotation marks (`'''...'''`) or a single single-quotation mark (`'.'`)?

- - - - - -
**Something to keep in mind:** Always start your function definition with a docstring, explaining at least what arguments the function takes and what it does or returns. When programming, you can even write the docstring prior to writing the body of the function definition.
- - - - -

**6.26.** Add docstrings to all the functions you defined so far.

**6.27.** Write a function called `is_even` that takes an integer `n` as an argument and returns `True` if the argument is an even number and `False` if it is odd.

**6.28.** Now write the function `is_odd` that returns `True` when its integer argument `n` is odd and `False` otherwise.

**6.29.** Write a function `is_factor` with integer parameters `f`, `n` that makes the following true: 
- `is_factor(3, 12)` 
- `not is_factor(5, 12)` 
- `is_factor(7, 14)` 
- `not is_factor(7, 15)` 
- `is_factor(1, 15)` 
- `is_factor(15, 15)` 
- `not is_factor(25, 15)`.

**6.30.** Write `is_multiple` to satisfy these statements: 
- `is_multiple(12, 3)` 
- `is_multiple(12, 4)` 
- `not is_multiple(12, 5)` 
- `is_multiple(12, 6)` 
- `not is_multiple(12, 7)`.

**6.31.** Write the function `farenheit_to_celcius` designed to return the integer value of the nearest degree Celsius for given temperature in Fahrenheit, and its inverse `celcius_to_farenheit`. Extract suitable test cases from a conversion table on the web.

**6.32.** Write a function `is_determiner` that checks if a given word is an English determiner (for practice reasons, try to do this without first storing an inventory of determiners in a _list_, which will be properly introduced in the next section). It should return True or False accordingly.

**6.33.** In PyCharm and many other IDEs you can ctrl+click (or cmd+click) on a function call, to jump to the place in the code where the function is defined. Clicking on a variable in this way brings you to the place where it is first assigned. It is true also for built-in functions, and functions imported from other modules, in which case PyCharm takes you to the corresponding source files as well. Try ctrl+click a bunch of times on different functions and variables.

