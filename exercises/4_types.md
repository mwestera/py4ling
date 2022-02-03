# Python for linguists


## 4. Types (`type`, and `int`, `str`, `float`, `bool`...)

**4.1.** What does the built-in function `type` do? Apply it at least to the expressions `4`, `238`, `-6`, `5.3`, `3 ** 4`, `'apple'`, `'apple' * 5`, `True`, `False`, `'True'`, `'False'`, `'987'` (note the quotation marks), `print` and `max`.

**4.2.** You can _convert_ between types by using `int`, `str`, `float`, `bool`, for instance `int('400')` constructs a string `'400'` from the integer `400`, and `bool(0)` constructs the boolean `False` from the integer `0`. Try to convert between different types, and use `type` to check the result. What happens for conversions that don't make sense, e.g., `int('apple')`, `float('')`?

**4.3.** Try `bool('True')` and `bool('False')`. Is the result what you expected? Try to understand why this is. Can you guess what string do you need to feed to `bool` to get `False`?

**4.4.** What happens if you try to append a number to a string by doing `'apple' + 5`? Can you fix this by using `str`?

**4.5.** What happens if you try to divide an integer number such as `5` by a floating point number such as `3.14`?

**4.6.** Is `5.0000` a float or an int? What do you expect will be the value of `5.0000 == 5`?

**4.7.** If you get a user's input using `input`, what is the type of the resulting object? Does this depend on what the user enters?

**4.8.** In a Python script, write a program that gets a number from the user, multiplies it times 5, and prints the result.

**4.9.** While the Python console is useful for trying out a single command, writing longer programs is much more convenient to do in a file in the editor. Can you think of some reasons why?

- - - - - -
**Something to keep in mind:** When you are asked to 'write a program', you can either create a new `.py` file (and make sure you subsequently run the new file), or continue working in an existing file from a previous exercise. As long as the previous code doesn't give errors, take too long to run, etc., continuing in the same file is fine! Later we will learn how to better structure your files and code. For now, make sure to choose sensible file names, and always add a **comment** with the exercise number(s) above each chunk of code, e.g., `# Ex 1.23`.
- - - - -

**4.10.** Write a program that gets one number from the user, then another one, and prints the result of dividing the first by the second. Try it out a couple of times. What happens if you run the program, first enter 9 and then 0?

**4.11.** To test if an object is of a certain type, use `isinstance`, for instance `isinstance(500, int)` and `isinstance('apple', str)`. What is the type of `isinstance` itself?

**4.12.** Types form a hierarchy, as you would expect, e.g., just like a mammal is also an animal, a string (type `str`) is at the same time also an object (type `object`), which is a more general, super-type. Test this with `isinstance('apple', str)` and `isinstance('apple', object)`. When you use `type`, it looks only at its lowest type in the hierarchy. Verify this by comparing `isinstance('apple', object)` to `type('apple') == object`.

**4.13.** What does this code do: `isinstance(bool == bool,bool)`? What is the output and why?

**4.14.** `help` is a built-in function that gives you information about other functions. Try `help(max)`, `help(min)` (pressing `q` lets you quit the help screen).

**4.15.** Use the `help` function to find out about the `round` function. Explore how to use it, with one and with two arguments.

**4.16.** Use `type` to test whether `round` changes a float into an int. Does it always do this?

**4.17.** Note that `print` can take multiple arguments, e.g., `print('apple', 'pear', 'banana')`. Use `help` to learn more about the `print` function. You will likely not understanding everything, but you can play around with the parameters `sep` and `end`.

**4.18.** Why doesn't `print('Hello', 'world!')` print `Hello, world!`?

**4.19.** Now that you have used the Python console for a while, enter `dir()` in the interpreter to show the 'directory', a list of names of all objects currently available (at least those in the _global scope_, about which we will learn later). As you will see, any variables previously created still exist (alongside some automatically created variables like `__name__`, about which we will learn later).

**4.20.** If you mistype `primt('apple')` instead of `print('apple')`, you would normally get the informative error _Name is not defined_ to notify you of this mistake: the name `primt` does not appear in the `dir()`. But what if you defined a variable `primt = 5` long ago and you forgot about it? If you then make the typo `primt('apple')`, the error you get will be much harder to understand (unless you remember you still had the `primt` variable hanging around from earlier).

- - - - - -
**Something to keep in mind:** If you keep too many old names hanging around in the interpreter, this can make it more difficult to _detect mistakes_. To reduce this problem, occasionally restart your Python console (especially if you keep getting unexpected results). When you run code from python scripts (instead of the interpreter directly) this problem is less likely to occur, as each time you run a script, Python starts from scratch. However, if keep working in the same file for too long, the problem can reappear. (To help with the latter, programmers _encapsulate_ chunks of code; we will learn about this later.)
- - - - -

**4.21.** In a Python script, write a program that asks for the user's age in years and prints several things: their age in months, their age in weeks, their age in days, their age in hours, their age in minutes, and their age in seconds; you can ignore leap years (and make other simplifying approximations).

**4.22.** Write a program that uses `input` to ask the user for the time now (in hours), and subsequently asks for the number of hours to wait. Your program should store each user response in a variable, and print what the time will be on the clock when the alarm goes off.

