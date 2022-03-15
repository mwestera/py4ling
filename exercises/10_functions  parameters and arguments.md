# Python for linguists


## 10. Functions, parameters and arguments

_When we called a function so far, we often simply passed values or variables in as arguments, but sometimes we used a different syntax, such as `sep='-'` in `print('apple', sep='-')`, known as a 'keyword argument'. We have also encountered the notion of a 'default value', on which a function falls back if a certain argument is omitted. This section clarifies such notions, and lets us practice with the different ways of defining and calling functions, which are surprisingly varied but also -- once you understand -- a systematic consequence of one or two simple rules. Along the way we will learn some facts about what functions _are_, and why in Python functions are considered 'first-class citizens'._

**10.1.** Define again the simple function `print_spam` we used in earlier sections (taking no arguments, simply printing `spam`). Explain (for instance using `type`) what the difference is between `print_spam` and `print_spam()`.

**10.2.** What happens if you assign a function to a variable, e.g., `shout_nonsense = print_spam`? Can you call the function using the new variable, instead of the original name?

**10.3.** Write a function `do_twice` that takes a function `func` as a parameter and calls that function twice. Having done that, calling `do_twice(print_spam)` should execute `print_spam()` twice. What happens if, instead, you accidentally do `do_twice(print_spam())`? Why?

- - - - - -
**Something to keep in mind:** In Python, a function is _not_ a piece of code, and calling a function is _not_ a matter of sending the interpreter to the lines in your file where the function is defined. Rather, in Python **functions are objects in their own right**. A `def`-clause is an instruction to the Python interpreter to create such an object and assign it to a variable with the same name as the function. In Python tutorials you'll often read that 'functions in Python are first-class citizens', to mean exactly this. Accordingly, functions, just like the other objects we have worked with so far (strings, ints, lists), can be (re)assigned to variables and passed around as arguments.
- - - - -

**10.4.** Define a function `do_twice_with_argument` that takes two arguments, a function `func` and a value `arg`, and calls the function twice with that argument. The command `do_twice_with_argument(print, 'test')` should result in `test` being printed twice.

**10.5.** Can you predict the outcome of `do_twice_with_argument(do_twice, print_spam)`? Test your prediction and make sure you understand what is going on. (In between these exercises, it is advisable to print an empty line to keep track of which output comes from which exercise.)

**10.6.** Generalize the previous functions to `do_multiple` and `do_multiple_with_argument`, by adding a parameter `n` to each, with the effect that the function `func` will be executed `n` times (`range` can be useful here).

**10.7.** As objects, functions carry some information along with them, such as the `__doc__` attribute containing the function's docstring (shown when `help` is called on the function, as we did earlier), and `__name__` storing the function's name. Try `print(print_spam.__name__)`. (Can you explain what happens if you do `print(print_spam().__name__)` instead?)

**10.8.** What happens to the `__name__` attribute of a function if you assign a function to a new variable, and retrieve the `__name__` property from that new variable?

**10.9.** Function objects also offer various methods (similar to strings having methods like `upper` and `capitalize`, and lists having `append` and `index`). Calling a function like `print('apple')` is in fact shorthand for invoking the `__call__` method of the function object, i.e., `print.__call__('apple')`. Verify that this is the case, and also test it for a couple of functions you yourself defined.

- - - - - -
**Something to keep in mind:** It may seem like we use 'argument' and 'parameter' interchangeably, but there is a subtle difference. When you _define_ a function, you specify its **parameters** in the header of the `def`-clause. When you _call_ a function, you can provide it with **arguments**. The called function will use the provided arguments as values for its parameters. This requires that Python is able to match each argument (of the function call) with the correct parameter (in the function definition) -- otherwise it isn't clear what your function call is requesting. The following exercises teach you more about how Python decides which arguments are used to set which parameters.
- - - - -

**10.10.** When calling a function, you have seen that sometimes arguments are simply given as a value, and sometimes as a `parameter=value` expression, a so-called **keyword argument** (e.g., `print('apple', end='')` uses both). In Python, you can often choose how to pass values as arguments to a function: the value on its own, or as a keyword argument `parameter=value`. Look carefully at the following code, predict the outcomes and test your predictions.

```python
def print_diff(a, b):
    print(a - b)

print_diff(5, 2)
print_diff(a=5, b=2)
print_diff(b=2, a=5)
print_diff(2, 5)
print_diff(a=2, b=5)
print_diff(b=5, a=2)
```


**10.11.** Arguments passed _without_ the parameter name are also called **positional arguments**. Given the previous example, do you understand why?

**10.12.** Given your answer to the preceding question, try to predict which of the following works fine, and which one crashes. Test your prediction and make sure you understand what is going on.

```python
print_diff(5, b=2)
print_diff(2, a=5)
```


**10.13.** Although positional and keyword arguments can be mixed, no positional argument can _follow_ a keyword argument. Try `print_diff(a=5, 2)` to see what error you get. Here is an intuitive explanation: argument order (for positional arguments) is determined by counting left-to-right, so if a keyword argument indicates 'order doesn't matter here', then the order of any arguments to the right of it cannot be relied upon either, hence any arguments to the right of it must also be given as keyword arguments.

**10.14.** Although typically one can choose whether to call a function with positional or keyword arguments or both, sometimes programmers may decide that certain (or even all) arguments _must_ be passed as keyword arguments. This is the case, for instance, for functions that permit any number of positional arguments, such as the built-in function `print`, e.g., `print('apple', 'pear', 'banana')` prints all three. Explain why it follows from this feature of `print`, that the additional `sep` and `end` parameters of `print` must _always_ be given as keyword arguments, by considering what happens if you don't:

```python
print('apple', 'pear', 'banana', sep='-', end='.')
print()  # print newline for clarity
print('apple', 'pear', 'banana', '-', '.')
```


**10.15.** Another reason why programmers sometimes choose to enforce the use of keyword arguments is _explicitness_. For instance, in the Seaborn library for creating plots, all parameters of a function like `scatterplot` must be specified with keyword arguments (e.g., `scatterplot(data=tweets, x='date', y='sentiment')`). Explain in what sense keyword arguments are more explicit than positional arguments.

**10.16.** For the sake of completeness, the way to let functions take any number of positional arguments (like `print`) and/or enforce the use of keywords for explicitness (like `scatterplot`), is through the use of an asterisked parameter `*` in the function definition header, which essentially 'eats up' any positional arguments given when the function is called; as a consequence, any parameters occurring after the asterisked parameter _must_ be specified with keywords. Try the following to better understand this:

```python
def some_weird_function(*a, b, c):
    print('a:', a)
    print('b:', b)
    print('c:', c)

# some_weird_function(1, 2, 3)     # will complain that `b` and `c` are not given values, as all positional arguments are eaten up by `*a`.
some_weird_function(1, b=2, c=3)    # this one works fine
some_weird_function(1, 2, 3, 4, b=5, c=6)   # this also works fine
```


**10.17.** Reflect on the role of the asterisk in the definition of the built-in `print` function:

```python
def print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False):
```


- - - - - -
**Something to keep in mind:** When you _define_ a function, you can specify **default values** for some or all of the parameters, using `parameter=value` syntax in the header of the function definition (not to be confused with the same `parameter=value` syntax used when _calling_ a function to specify keyword arguments!). Parameters with default values can be omitted from the function call, in which case the default value is used.
- - - - -

**10.18.** Explain how the foregoing is illustrated by the following code:

```python
def multiply_and_add(a, b, c=1):
    print(a * b + c)

multiply_and_add(2, 3)
multiply_and_add(2, 3, 4)
```


**10.19.** Explain how by specifying or omitting default values in your function _definition_, you can effectively make certain arguments **mandatory** and others **optional** when calling the function.

**10.20.** Define a function `subtract` with three parameters: two mandatory numbers `a` and `b`, and one optional boolean `absolute`, where the latter has default value `False`. The call `subtract(3, 5)` should evaluate simply to the difference `3 - 5`, i.e., `-2`. The call `subtract(3, 5, True)` should evaluate instead to the absolute (positive) value of the difference, i.e., `2`.

**10.21.** Look up the function `tokenize` from the previous section, and if needed copy the code to your current working file. Note that it effectively removes spaces from the input text, returning only the tokens. This makes it harder to reconstruct the original text by re-concatenating all the tokens, which in some cases might be a desirable functionality. For this reason, add an optional parameter to the function, `keep_spaces` with default value `False`. When the default is overriden (i.e., when the function is called with the additional argument `True`), the returned tokens should have their spaces still attached. For example, `tokenize('The cat sleeps.', True)` should evaluate to `['The ', 'cat ', 'sleeps', '.']` (note the spaces). Also verify that omitting the optional argument results in the original behavior.

- - - - - -
**Something to keep in mind:** While the syntax of specifying default values (`parameter=value`) looks similar to the syntax of keyword arguments explained at the start of this section, the two notions -- default value and keyword argument -- are conceptually _very_ different. Default values are an aspect of function _definitions_, while keyword arguments are an aspect of function _calls_. Whether a parameter is given a default value when _defining_ the function, has nothing directly to do with whether you should use positional or keyword arguments when _calling_ the function.
- - - - -

**10.22.** To illustrate the preceding explanation, verify that the optional arguments of the `subtract` and `tokenize` functions from above can be passed both as a positional argument and as a keyword argument.

**10.23.** Try to predict the printed output of the following function calls, and test your understanding:
- `multiply_and_add(2, 3, 5)` 
- `multiply_and_add(a=2, b=3, c=5)` 
- `multiply_and_add(c=5, a=2, b=3)` 
- `multiply_and_add(2, b=3)` 
- `multiply_and_add(2, b=3, c=5)` 
- `multiply_and_add(a=2, b=3)` 
- `multiply_and_add(b=3, a=2)`

**10.24.** In function definitions, parameters without default values should come before parameters that have defaults. Try this with an example that violates the rule, e.g., `def my_function(a, b=1, c): ...`.

**10.25.** Given the preceding rule that parameters with defaults should come before parameters without defaults in the function definition, how come the function call `multiply_and_add(c=5, a=2, b=3)` is allowed?

**10.26.** Default values are assigned only once, at the start, when the function is defined; _not_ each time the function is called. This can lead to puzzling behavior when you use a _mutable_ object like a list as default argument: since it is mutable, it can be changed, thereby causing the default value to change. For example, consider the function below and what it is _supposed_ to do, according to the docstring, if no list argument is given. Explain what goes wrong, taking into account the mutability of the default argument.

```python
def append_to(element, l=[]):       # note: the docstring is a lie
    """
    Appends the element to the provided list, returning it, or to an empty list if none was provided (resulting in [element]).
    """
    l.append(element)
    return l

print(append_to('cat', ['dog', 'horse']))
print(append_to('cat'))
print(append_to('cat', ['mouse']))
print(append_to('cat'))
```


**10.27.** When entering the above code in PyCharm, the editor will likely immediately warn you that 'Default argument value is mutable'. PyCharm may even offer you to automatically fix it, which will result in code like the following. Try to understand how this fix works, i.e., how it avoids the problem illustrated in the previous exercise:

```python
def append_to2(element, l=None):
    """
    Appends the element to the provided list, returning it, or to an empty list if none was provided (resulting in [element]).
    """
    if l is None:       # Equivalently, replacing the whole if-clause:  l = l or []
        l = []
    l.append(element)
    return l

print(append_to2('cat', ['dog', 'horse']))
print(append_to2('cat'))
print(append_to2('cat', ['mouse']))
print(append_to2('cat'))
```


- - - - - -
**Something to keep in mind:** The fact that a function's default values are created only once, when the function is defined, reflects that (in Python) functions are not pieces of code but objects, created only once, when the interpreter reads the definition to create the function object.
- - - - -

**10.28.** We have already seen that functions, as objects in their own right, have various properties that you can inspect, such as `__doc__` and `__name__`. Another property of functions is `__defaults__` (not for built-in functions though). Use this to inspect the default values of some of the functions defined above, e.g., `print(append_to.__defaults__)` and `print(multiply_and_add.__defaults__)`. For the problematic function `append_to`, compare its defaults before and after a call `append_to('cat')`.

**10.29.** In the previous section you defined `turn_clockwise` and `turn_counterclockwise`, to take directions like `'N'`, `'NW'`, and `'SE'` and return a new direction after turning. (Copy these to your current working file if needed.) Extend their functionality with an optional argument `n_turns` that has `1` as its default value, representing the number of 'turn steps' to take.

