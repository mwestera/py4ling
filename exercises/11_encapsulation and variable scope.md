# Python for linguists


## 11. Encapsulation and variable scope

**11.1.** Earlier we saw what happens if you call a function before defining it. Try this again.

**11.2.** The foregoing exercise should have resulted in an error. A Python program will terminate when an error is encountered (or more accurately: when an exception is _raised_ and not _caught_ somewhere higher up). Nevertheless, you may occasionally have seen noticed printed output appearing _after_ (i.e., below) an error message. Try to reproduce this oddity: Write some code that prints a bunch of stuff and then, at the end, does something illegal (e.g., reference a function before it is defined). Run it to verify that the error message can (at least sometimes) appear in the output before (i.e., above) the printed message. (If this never happens, perhaps your system is configured in a way that prevents this.)

- - - - - -
**Something to keep in mind:** The command `print` sends content to the **standard output stream**, while error messages go through a separate **error stream**. Each stream is 'buffered', meaning messages are first stored in a 'buffer' that is then, periodically, 'flushed' onto the Run output window on your screen -- only _then_ do you see the output. It can happen that the error buffer is flushed _before_ the standard output buffer, and thereby cause an error message to appear _before_ certain printed messages, even if the error was in fact encountered a few nanoseconds _after_ the last `print` command. This is a technicality, but knowing about this can prevent confusion about the (apparent) source of an error.
- - - - -

**11.3.** If in the previous exercise you were able to let an error message appear before the printed messages, now add `flush=True` as an extra argument to your `print` statements (or at least the last one before the error) and try again. The error message should now consistently appear last (i.e., at the bottom of your output). This is because `flush=True` tells Python to flush the standard output buffer immediately, i.e., as soon as the `print` command is given. Although you won't normally need to use `flush=True`, you can use it in the following exercises if you find the order of print and error messages in your output confusing.

**11.4.** Define a function `invert` that takes a string and returns the inverted string, and then define a function `print_inverted` that takes a string and (inside its definition) calls the `invert` function to invert it, and finally prints the result (with `flush=True` for clarity). The point here is that we have one function (`print_inverted`) that, in its definition body, references another (`invert`). Does the order in which the two functions are defined matter? Formulate a prediction, then test it. Try to form a hypothesis about why this might be.

**11.5.** Test and (if needed) refine your hypothesis about the order of function definitions and function calls, by comparing the following two programs. For this, make sure that you try each version _on its own_, for instance by placing each in a separate file, or by commenting-out one version when you run the other and vice versa.

```python
# The first program:

def print_sum(a, b):
    print(add_numbers(a, b), flush=True)

def add_numbers(a, b):
    return a + b

print_sum(1, 3)

# The second program (make sure you try the two programs separately):

def print_sum(a, b):
    print(add_numbers(a, b), flush=True)

print_sum(1, 3)

def add_numbers(a, b):
    return a + b
```


- - - - - -
**Something to keep in mind:** A Python script is interpreted **top-to-bottom**. To understand this, it is important to recall from the previous section that functions are _not_ pieces of code, and calling a function does _not_ mean 'sending the interpreter to the line where the function is defined'. Rather, functions are objects, that are created and stored in working memory when the interpreter (going top-to-bottom) encounters a `def`-clause, and to call a function is to invoke a method of the function object that is in working memory (i.e., no need to interrupt the top-to-bottom interpretation to 'go to the line where the function is defined').
- - - - -

**11.6.** The difference between defining and calling a function explains why in the body of one function definition, you can reference some other function even if that function's definition comes later in the file, as long as the containing function isn't _called_ before the referenced function is defined. In light of this, review your understanding of the preceding two exercises.

**11.7.** Write a function `time_to_secs` that takes three arguments -- hours, minutes, seconds -- and converts the time these jointly represent to a total number of seconds, which it returns as output. If necessary extend `time_to_secs` so that it can cope with real (i.e., non-integer, or floating point) values as inputs. It should always return an integer number of seconds ('truncated', or rounded down).

**11.8.** Write three functions that are the partial _inverses_ of `time_to_secs`: 
 1. `hours_in` returns the whole integer number of hours represented by a total number of seconds; 
 2. `leftover_minutes_in` returns the whole integer number of _left over_ minutes in a total number of seconds once the hours have been taken out; 
 3. `leftover_seconds_in` returns the left over seconds in a total number of seconds, once the hours and minutes have been taken out. 

 You may assume that the total number of seconds passed to these functions is an integer.

**11.9.** Write a single function that is the inverse of `time_to_secs`. It should use the preceding three auxiliary functions to obtain hours, minutes and seconds, and return these values together as a _tuple_ like this (we will learn about tuples later): `return hours, minutes, seconds`. Does the order matter in which the various function definitions appear in your file? What about the position of the function calls?

**11.10.** In an earlier section you defined functions `bigrams` and `trigrams`. (Copy these to your current code file if necessary, along with `tokenize` on which they rely.) To refresh your memory, also define a function `quadrigrams`, for sequences of four words. The definitions of these functions likely contain considerable overlap. Avoid this by defining a function `ngrams` that takes a text and a number `n`, returning a list of n-grams in the text (bigrams if `n == 2`, trigrams if `n == 3`, etc.); redefine the original functions `bigrams`, `trigrams` and `quadrigrams` as, essentially, shortcuts for `ngrams`.

- - - - - -
**Something to keep in mind:** Streamlining your code is called **refactoring**, one aspect of which is dividing your code into functions, sometimes called **chunking**. One rule of thumb for refactoring/chunking is **Don't Repeat Yourself** (DRY), i.e., consider defining a function when you find you are repeating chunks of code. Another is the **Single Level of Abstraction Principle** (SLAP): a function should do a single thing at a single level of abstraction. The latter is related to the ideal of **Separation of Concerns** (SoC), e.g., when you're defining an `ngrams` function, you shouldn't need to worry about how to tokenize a text, and vice versa).
- - - - -

**11.11.** Can you think of some reasons why it is (often) a good idea to try to avoid repeated chunks of code, i.e., why the DRY principle is a useful guideline?

**11.12.** Our client requests that we add a boolean parameter `as_strings` to the function `ngrams`, with default value `False`. If this boolean is set to `True`, the n-grams in the returned list should be represented as single strings, not lists of strings (e.g., `'the cat eats'` instead of `['the', 'cat', 'eats']` to represent a trigram). Make the required change. What is an advantage of having refactored your code in terms of the `ngrams` function?

**11.13.** Remove your functions `ngrams` and `tokenize` from your current working file, and move them to a new, empty Python file you call `text_utils.py` (in the same directory as your current working file). We will be importing `text_utils.py` as a module, so make sure it contains only function definitions, no function calls. Having made this change, your `bigrams`, `trigrams` and `quadrigrams` functions (which remained in your main working file) will no longer work (test this!), as after the above refactoring they rely on `ngrams`. To restore them, place `import text_utils` (note without the `.py`) at the top of your current working file, and replace every reference to `ngrams` by a relative reference to `text_utils.ngrams`. Verify that everything now works properly again. Future sections will likewise rely on `import text_utils` for easy access to `ngrams` and `tokenize` (or else we'd have to duplicate the code into each new file).

- - - - - -
**Something to keep in mind:** The `import` keyword lets us use not only existing modules (such as `random` or `math`), but also reuse our own Python files. It is generally advisable that files that are imported only _define_ functions, not _call_ them, lest the import has 'side effects'. We will learn more about `import` and modules later.
- - - - -

**11.14.** Define a function `filter_by_twos` that takes a list, and returns a new list containing every second element (so given `['a', 'b', 'c', 'd', 'e', 'f']` it will return `['b', 'd', 'f']`). Define another function `filter_by_threes` that does the same but for every _third_ element (for the same example, it will return `['c', 'f']`). There is likely some code repetition (or a lot, depending on how concise your code is). Define a generalized function `filter_by_n` that takes an additional argument `n` and returns a list with every `n`th element, then redefine your original functions in terms of this, as shortcuts.

**11.15.** In section 10 you defined `turn_clockwise` and `turn_counterclockwise`, taking a string representation of a direction (`N`, `E`, `S`, `W`) and returning a string representation of the new direction after turning. (Copy these to your current file if needed; we won't use them later so no need to put them in a separate module.) There is likely considerably overlap between the two functions. If so, try to minimize overlap, for instance by defining a generalized function `turn` that can turn in both directions depending on whether a given integer argument is negative or positive.

<br>**_Encapsulation and variable scope_**

**11.16.** Another reason for chunking your code into functions is **encapsulation**: variables assigned inside a function, are not accessible outside it. This keeps the number of accessible variables at a given place in your code smaller, which helps prevent certain types of programming errors. Explain how the following code illustrates encapsulation. (Remember we add `flush=True` to a print statement to flush the print buffer directly, in order for printed output and error messages to appear in order of execution.)

```python
def some_function():
    b = 123
    print('inside the function, b =', b, flush=True)

some_function()
print('outside the function, after calling the function, b =', b)
```


**11.17.** In the previous example, what happens if you assign something to `b` also in the global scope, before the function definition? For instance, add  `b = 789` (a different value) above the definition of `some_function`.

**11.18.** And what happens if you now remove the line `b = 123` from the function (while keeping `b = 789` above the function definition)? What gets printed? This and the foregoing exercises show that there is some kind of asymmetry between local scope and global scope with regard to variable accessibility. Try to formulate in your own words what this asymmetry is (further below it will be stated in more precise terms).

**11.19.** Unlike `def`-clauses (function definitions), `if`-clauses do not create a local scope, i.e., do not encapsulate the variables assigned within it. Explain how the following example demonstrates this:

```python
if 1 + 1 == 2:
    x = 'test'
    print('inside the if:', x)

print('outside the if:', x)
```


**11.20.** Does the following example demonstrate that `for`-clauses likewise do not encapsulate their variables?

```python
for x in [1, 2, 3]:
    print('inside the for:', x)

print('outside the for:', x)
```


**11.21.** Does the following code show that `if`-clauses do create a local scope after all? Or does it show something else?

```python
if 1 + 1 == 3:      # Notice the 3!
    x = 'test'
    print('inside:', x)

print('outside:', x)
```


**11.22.** What about an `if`-`elif`-`else` compound clause? Are variables assigned in the initial `if`-clause accessible in subsequent `elif` and `else` clauses? (Does the question even make sense?)

**11.23.** The built-in functions `locals` and `globals` give you a _dictionary_ containing all local/global variables and their values. We will learn about dictionaries later, but you can already try them out by running the code below. Note that among the global variables are many 'dunder' (double underscore) variables like `__name__` that Python relies upon for bookkeeping, so you may need to scroll to the right to see the variables you yourself assigned.

```python
a = 3
b = 4

def my_function(c):
    d = 6
    e = 7
    print('inside my_function, locals = ', locals())
    print('inside my_function, globals =', globals())

my_function(5)
```


**11.24.** In the above example, the local scope also contains a variable `c`. Where does it come from, i.e., where is it assigned its value? (Recall the ctrl+click exercise of the previous section.)

**11.25.** Modify the above example to print `globals()` and `locals()` also from _outside_ the function definition, e.g., put the print statements below the function call. What does this demonstrate?

- - - - - -
**Something to keep in mind:** When Python enters a local scope (e.g., function definition), `locals()` is initially empty. If a variable is _assigned_ a value inside a local scope (e.g., inside a function definition), this variable+value will be stored in `locals()`, not `globals()`. When a variable's value is _retrieved_ inside a local scope, Python will first try to find it in the `locals()` dictionary, and only if it does not find the variable there it will look in `globals()`. (Actually there are two other 'namespaces' in which Python will search for a variable: Python indeed first looks in the local scope, but then it checks the immediately 'enclosing scope' (e.g., if the function is itself contained in a function or class), before considering the global scope, and finally it looks among the `__builtins__`, for built-in functions such as `len` and `print`.)
- - - - -

**11.26.** We have seen that variables defined inside functions can have the same name of an existing variable from outside the function, without the latter being affected. Explain exactly how this can be.

**11.27.** For every place in the following code where the value of a variable is retrieved, determine the place where its value at that point was assigned. Take into account mutability: mutable objects like lists can be changed _without_ this involving reassigning the variable. While you're at it, a good exercise is to try to predict the exact output of this program.

```python
students = ['ann', 'beth', 'gemma']
more_students = ['dale', 'ebba']
message = 'Hello!'

def print_students(students):
    students = [name.capitalize() for name in students]
    for student in students:
        print(message, student)

students[1] = 'elisabeth'
all_students = students + more_students
all_students.append('philip')
print_students(all_students)

if len(all_students) > 3:
    message += ' Nice crowd!'
    print(message, flush=True)
```


**11.28.** The above 'something to keep in mind' left out an important detail: when a variable is assigned a value _anywhere_ in the local scope, then that variable becomes _strictly local_ to that scope, meaning Python will _only_ try to find it in `locals()`, and _never_ look for that variable in`globals()`, _even if the lookup in locals() fails_. This can cause surprising behavior. Try to predict what the following code does, test your prediction, and reconcile your findings with the rules for encapsulation explained so far.

```python
a = 5

def erroneous_function():
    print(a)
    a = 8

erroneous_function()
```


**11.29.** What might one naively expect the following function to print? Explain why this expectation is wrong, namely, why the following gives an error:

```python
b = 10

def bad_function():
    b += 3
    print(b)

bad_function()
```


**11.30.** The foregoing exercises reveal that a variable inside a function is either local or global, _never_ local on some lines (in the function) and global on other lines (in that same function). Can you think of a possible benefit of this all-or-nothing behavior?

**11.31.** Try to predict the entire printed output of the following program, and test your prediction:

```python
x = 6

print(x)

def first_function(x):
    print(x)

def second_function():
    print(x)

def third_function(y):
    x = y - 3
    print(x)

print(x)
first_function(3)
print(x)
second_function()
print(x)
third_function(x)
print(x)
```


**11.32.** Does the foregoing mean that there is _no_ way to have a function assign a value to a global variable? Well, you may not ever need this, but there is a way: for a given variable `x`, typing `global x` at the top of the body of a function definition will make sure that `x` in that function serves as a global variable, even if you assign something to `x` in that function later (result: it will assign to a global variable). Play around with this if you like. But the more important take-away of this section is how Python governs variable scope (hence, why something like the `global` keyword would be needed in the first place) -- try to summarize that.

