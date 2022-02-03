# Exercises

[Contribution guidelines for this project](pycharm.png)


### 1. Warming-up

**1.1.** In the Python interpreter, enter a print statement such as `print('Hello, world!')`.

**1.2.** In a print statement, what happens if you leave out one of the parentheses, or both?

**1.3.** If you are trying to print a string, what happens if you leave out one of the quotation marks? What if you leave out both?

> **Note:** Whenever you learn something new, stick with it for a while to explore different variants and ways to break it. By consciously introducing errors and learning to recognize what happens, you will become good at diagnosing the problem when you make unintentional mistakes later.

**1.5.** Try both single and double quotation marks around the string: `print('cheese')` and `print("cheese")`. What happens if you mix different types of quotation marks?

**1.6.** What happens if you enter `primt('cheese')`? What happens if you enter `print('cheeze')`? Can you explain why?

**1.7.** Try using the python interpreter as a calculator, using numbers and operators like + and -. Which operators does Python recognize? What does `**` do? What does `//` do? And `%`?

**1.8.** What happens if you put a minus sign before a number? What happens if you put a plus sign before a number? What about `2++2`?

**1.9.** In math notation, leading zeros are ok, as in `09`. What happens if you try this in Python?

**1.10.** What happens if you have two values with no operator between them?

**1.11.** How many seconds are there in 42 minutes 42 seconds?

**1.12.** How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.

> **Note:** Some of these exercises are about language, or at least about strings like words and sentences; but most aren't. The initial purpose for these exercises is to get you to think like a programmer. Later we will learn how to apply this way of thinking specifically to language.

**1.14.** If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per kilometer in minutes and seconds)? What is your average speed in kilometers per hour?

**1.15.** We've seen that `n = 42` is legal. What about `42 = n`? And how about `x = y = 1`? If it is legal, what is the result (try printing the variables)?

**1.16.** In math notation you can multiply variables _x_ and _y_ like this: _xy_. What happens if you try that in Python? Why?

**1.17.** What is the area of a circle with radius 3? What is the volume of a sphere with radius 5?

**1.18.** First enter `n = 42`. Then try each of the following. Is it legal, and if so, what does it do? 1. `n = 100`, 2. `n = n`, 3. `n = n + 3`, 4. `n -= 3`, 5. `n = 'n'`, 6. `'n' = n`.

**1.19.** Create a Python script containing `print('Hello, world!')` and run it.

**1.20.** Write and execute three lines of code that: (i) create a variable with the value 37; (ii) create another variable with the value 4; (iii) print out the result of multiplying those together.

**1.21.** Assign a string to a variable, then print it, and print it again. Now assign a different string to the same variable and print it again twice. What advantage of variables does this exercise illustrate?

**1.22.** In some languages every statement ends with a semi-colon, `;`. What happens if you put a semi-colon at the end of a Python statement?

**1.23.** What if you put a period at the end of a statement?

**1.24.** Print a string that contains single or double quotation marks, such as _She said: "Hello!"_ and _She said: 'Hello!'_. Can you get it to work? And how can you print a string that mixes single and double quotation marks?

**1.25.** Compare what happens in the Python interpreter, vs. running a Python script containing the same code; try at least `print('cheese')`, `'cheese'`, and `cheese` (without quotation marks).

**1.26.** Take a statement that runs (e.g., `print('Hello, world!')`), add one or more spaces in front of it and try to run it again. What happens? Unlike in many other programming languages, in Python indentation (whitespace at the start of lines) is meaningful. Later we will see cases where you _must_ indent.

**1.27.** Add parentheses to the expression `6 * 1 - 2` to change its value from `4` to `-6`.

**1.28.** In the Python interpreter enter `bruce + 4`. What happens? Next, assign a value to `bruce` so that `bruce + 4` evaluates to `10`.

**1.29.** Suppose the cover price of a book is €24.95, but bookstores get a 40% discount. Shipping costs €3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?

**1.30.** If I leave my house at 6:52 am and run 1 km at an easy pace (6:15 per km), then 3 km at tempo (4:42 per km) and 1 km at easy pace again, what time do I get home for breakfast?

**1.31.** `%` is the modulo operator, look it up if you need to. Evaluate each of the following numerical expressions a.-g. in your head, then use the Python interpreter to check your results: a. `5 % 2`, b. `9 % 5`, c. `15 % 12`, d. `12 % 15`, e. `6 % 6`, f. `0 % 7`, g. `7 % 0`. What happens? Why?

**1.32.** What do the built-in functions `max` and `min` do? For example, try `max(3, 4, 5)`, `max(10)`, and `min(5, -11, -2, 99)`.

**1.33.** In maths it is common to compare numbers or variables with _greater than_, _smaller than_, _not equal to_, and so on. Experiment with the operators `>`, `<`, `!=`, `>=`, `<=` to figure out what they do.

**1.34.** Put `not` in front of some of the expressions you tested, e.g., `not (3 >= 4)`. What does it do? What about `not True` and `not False`? Inspired by the operator `!=`, could you also use exclamation mark `!` instead of `not`?

**1.35.** Explore how boolean operators `and` and `or` work. Does `or` correspond to inclusive or exclusive _or_?

**1.36.** What is the difference between `not True or False` and `not (True or False)`, and why?

**1.37.** First enter `n = 42`, and then `n == 42`. What is the result? What about `n == 43`? What happens if you try to assign a new variable with `==`, e.g., `z == 123` (assuming you haven't used `z` before)?

**1.38.** Try to predict which one of these is legal, what the result is, and why: `fruit = 'apple'`, `fruit = apple`, `'fruit' = 'apple'`, `fruit == apple`, `'fruit' == 'apple'`, `'fruit' == apple`.

**1.39.** What does this code do: `a = 3 == 3`? What is the result and why? What’s the difference between that code snippet and this one: `a == 3 = 3`? Why does the latter produce an error?

> **Note:** Single `=` is used for assigning a value to a variable, while double `==` tests for equality. It matters how you read them, whether mentally or out loud. If you read both simply as _is_, you are prone to confuse yourself.

**1.41.** What do these expressions evaluate to? 1. `3 == 3`, 2. `3 != 3`, 3. `3 >= 4`, 4. `not (3 < 4)`.

**1.42.** Give the logical opposites of these conditions: 1. `a > b`, 2. `a >= b`, 3. `a >= 18 and day == 3`, 4. `a >= 18 and day != 3`.

**1.43.** Which of the following tests fail? Explain why. a. `3 % 4 == 0`, b. `3 % 4 == 3`, c. `3 / 4 == 0`, d. `3 // 4 == 0`, e. `3+4 * 2 == 14`, f. `4-2+2 == 0`, g. `len("hello, world!") == 13`.

**1.44.** You look at the clock and it is exactly 2pm. You set an alarm to go off in 51 hours. At what time does the alarm go off?

**1.45.** In the interpreter enter `name = input('What is your name?')`. What does it do? Enter something in the interpreter. Next, print the variable `name`.

**1.46.** In a Python script, write a program that asks for the user's age in years and prints several things: their age (ignoring leap years) in months, their age in weeks, their age in days, their age in hours, their age in minutes, and their age in seconds.

> **Note:** Use `input` to get input from the user in a very simple way. Later on we will learn about reading data from files or from the internet.

**1.48.** In a Python script write a program that uses `input` to ask the user for the time now (in hours), and subsequently asks for the number of hours to wait. Your program should print what the time will be on the clock when the alarm goes off.

### 2. Simple string operations

**2.50.** You know that Python can add and multiply numbers with `+` and `*`. Do these operations also work on strings? Try `'apple' + 'pear'`, `'apple' * 'pear'`, `'apple' * 5`, `'pear' + 5` and others. Which mathematical operations work on strings, and which ones don't? Which types of errors do you get?

**2.51.** How do you add two strings together with a dash "-" in between? And with a space in between? And with five spaces in between?

**2.52.** For the sentence _All work and no play makes Jack a dull boy_, first store each word in a separate variable, and, using these, print out the sentence on one line.

**2.53.** For each of the following, explain whether it's true or false (or neither...) and why: `'hat' == "hat"`, `hat == 'hat'`, `1/3 == .33`, `'three' > 'two'`, `2 + 2 = 4`.

**2.54.** What happens if you feed the built-in functions `max` and `min` a string as argument (e.g., `max('apple')`, `min('bonanza')`)? And what about multiple strings, `max('apple', 'aardvark', 'banana', 'zebra')`? Can you explain the result of `max('250')`? And `min('-852')`? And `max('123abc')`?

**2.55.** What does `len('apple')` do? Can you also get the length of a number, e.g., `len(3)`? What about a boolean? What about the length of the empty string?

> **Note:** To get the most out of these exercises, try not to use any built-in methods other than the ones mentioned in the exercises that came before. Later on, we will learn about convenient shortcuts for some of the things you are asked to do, as well as familiarize ourselves with powerful natural language programming libraries.

**2.57.** Assign a variable `name = 'Michael'`. What do each of the following do: `name[1]`, `name[2]`, `name[8]`, `name[-1]`, `name[-2]`, `name[1:3]`, `name[2:2]`, `name[-2:]`, `name[2:]`, `name[:2]`, `name[0]`, `name[2-4]`, `name[3-2]`, `name[1+1]`? The square brackets operator lets us do what is called _slicing_ the string.

**2.58.** Perhaps you'd expect to be able to change the string in `name` by replacing a character like this: `name[2] = 'b'`, expecting the result `Mibhael`. But this doesn't work; what does the error message say? This is because strings are not _mutable_: once you create a string, you cannot change it, only create a new one that is different. We return to mutability later.

**2.59.** What does `'0123456'[3]` do? What about `'1234567'[3]`?

**2.60.** What does `name[len(name)]` do? What about `name[len(name)-1]`? Why?

**2.61.** Predict the outcomes of `len('apple' * 5)` and `len('apple') * 5`, then test your expectation.

**2.62.** Python's string class provides various methods, including `upper` and `lower`. What would you expect them to do? As methods of the string class, you call them like this: `'apple'.upper()`.

**2.63.** For some arbitrary string assigned to variable `s`, is the following true: `s == s.upper().lower()`.

**2.64.** In a Python script write a program that uses `input` to ask for the user's name, and subsequently print _High [name], how are you?_

### 3. Types

**3.66.** What does the built-in function `type` do? Apply it at least to the expressions `4`, `238`, `-6`, `5.3`, `3 ** 4`, `True`, `False`, `'apple'`, `'apple' * 5`, `print` and `max`.

**3.67.** You can _convert_ between types by using `int`, `str`, `float`, `bool`, for instance `int('400')` turns the string `'400'` into the integer `400`. Try to convert between different types, and use `type` to check the result. What happens for conversions that don't make sense, e.g., `int('apple')`, `float('')`?

**3.68.** Try `bool('True')` and `bool('False')`. Is the result what you expected? Try to understand why this is. What string do you need to feed to `bool` to get `False`?

**3.69.** To test if an object is of a certain type, use `isinstance`, for instance `isinstance(500, int)` and `isinstance('apple', str)`. What is the type of `isinstance` itself?

**3.70.** Types form a hierarchy, as you would expect, e.g., just like a mammal is also an animal, a string (type `str`) is at the same time also an object (type `object`), which is a more general, super-type. Test this with `isinstance('apple', str)` and `isinstance('apple', object)`. When you use `type`, it looks only at its lowest type in the hierarchy. Verify this by comparing `isinstance('apple', object)` to `type('apple') == object`.

**3.71.** What does this code do: `isinstance(bool == bool,bool)`? What is the output and why?

**3.72.** `help` is a built-in function that gives you information about other functions. Try `help(max)`, `help(min)` (pressing `q` lets you quit the help screen).

**3.73.** Use the `help` function to find out about the `round` function. Explore how to use it, with one and with two arguments.

**3.74.** Use `type` to test whether `round` changes a float into an int. Does it always do this?

**3.75.** Note that `print` can take multiple arguments, e.g., `print('apple', 'pear', 'banana')`. Use `help` to learn more about the `print` function. You will likely not understanding everything, but you can play around with the parameters `sep` and `end`.

> **Note:** If you have used the Python interpreter for a while, enter `dir()`. As you will see, any variables previously created will still exist (alongside some automatically created variables like `__name__`). Having too many old variables stick around can make it difficult to understand what is happening. For this reason, try restarting your Python interpreter, and do this occasionally from now on.

### 4. If, else

> **Note:** From now on, you will often be writing chunks of multiple lines of code. For this, creating a Python script and running it, is much more convenient than working directly with the Python interpreter.

**4.79.** Execute `if 4+2 == 6: print('yes!')`. Now try to break it by modifying different things, for example, what if you replace `==` by `=`? (Undo that.) What if you remove the colon `:`? (Undo that.) What if you put `print('yes!')` on a new line? Can you make sense of the latter error and try to fix it?

**4.80.** Testing newlines:
```python
print("horrible")

import csv

```


**4.81.** Modify the body of your if-clause to have two statements instead of one, e.g., `print('yes!')` followed by `print('4+2 is indeed 6!')`. Do both statements need to be indented? What happens if one is indented more than the other? What if you properly indent the first statement below the `if`, but not the second statement? What happens if there is an empty line between the two statements, and the second statement is not indented?

**4.82.** In your Python editor (or the interpreter), can you indent with the 'tab' key? Do these appear as proper tabs (large spaces) or are they replaced by sequences of multiple normal spaces? If the latter, you're safe; if the former, you need to pay attention: you can indent either with tabs or with spaces, but don't mix them!

**4.83.** Write a program that takes a variable `n`, tests if its value is odd, and if not, adds 1 to it and prints _I've made it even!_. Subsequently, regardless of whether it was originally even or odd, the program should always print the resulting value of `n`.

**4.84.** With variable `name` containing a string, write a program that tests if the first letter is `a`, and, if so, prints _The first letter is 'a'!_. Only if the first letter is 'a', it should additionally test if the second letter is 'b', and if so, print _The word starts with 'ab'!_. Your second `if` can be nested under the first `if` -- make sure the indentation reflects this. Apply your program to a number of strings to test, such as _able_, _apple_ and _banana_.

> **Note:** Always remember: indentation in Python is meaningful. Look up Python's indentation rules if you are unsure.

**4.86.** Use `else` to write a program that tests whether the value of `n` is odd, and if so print _Odd!_, and if not print _Even!_. Did you use the correct indentation?

**4.87.** Use both `elif` and `else` to write a program that prints _Big!_ if the value of `n` is greater than 100, _Medium..._ if it is between 50 and 100, and _Small._ if it is between 0 and 50.z

**4.88.** We both flip a coin, the outcome of which is stored in two boolean variables. If both come up heads, print _We both won!_, if both come up tails, print _Play again._, if only the first comes up heads, print _Player one won._, if the second, print _Player two won._. Implement a version with nested `ifs`, and a version without nested `ifs`.

### 5. Lists and loops

**5.90.** Assign a variable `names = ['Alf', 'Beth', 'Chris', 'Dave', 'Esra']`. What does `type(names)` say?

**5.91.** Use square brackets `[` and `]` to create a list of numbers, a list of strings, and a list of both numbers and strings. Do these lists all have the same `type`?

**5.92.** Using the previous variable `names`, what do the following do: `names[1]`, `names[2]`, `names[8]`, `names[-1]`, `names[-2]`, `names[1:3]`, `names[2:2]`, `names[-2:]`, `names[2:]`, `names[:2]`, `names[0]`, `names[2-4]`, `names[3-2]`, `names[1+1]`?

**5.93.** Earlier we used `len` for strings. Does it also work on lists?

**5.94.** Assuming you still have the list of names assigned to `names`, what does `for name in names: print(name)` do?

**5.95.** After executing the preceding code, what is now the value of the variable `name`? Do you understand why?

**5.96.** Write a program that loops over the list `names` from above and prints each element twice, using a `for`-loop with two `print` statements in its body.

**5.97.** Assuming you still have the variable `names`, what does the `in` keyword do? Try at least `'Alf' in names` and `'Alwyn' in names`.

**5.98.** Somehow combine `in` with `not` to test whether _Alwyn_ is not in `names`.

**5.99.** What do you expect will happen if you do `names[len(names)]`? Try it!

**5.100.** You can change a list element at a given position (index) by assigning a new value using `=`, e.g., `names[3] = 'Nick'`. Print the resulting list.

**5.101.** In `names`, replace the last element by 'Suzy' and the first element by 'Bob'. Can you also use assignment to extend the list, by appending an element at the end?

**5.102.** Do you remember whether you can similarly change a string by assigning a character to a position, e.g., `name[2] = 'z'`? Try it, and compare this to how a list behaves. Lists are mutable, while strings are immutable.

**5.103.** But if strings are immutable, what about this: First run `x = 'abc'` and `print(x)`, and then `x = x.upper()` and `print(x)` again. Explain what's going on; is the string mutable after all?

**5.104.** Adding elements at the end of a list can be done, instead, with `append`, which is a method of the list class, hence you call it like `names.append('Ann')`. Try appending several names to `names`, and finally print the length of the resulting list.

**5.105.** Do you expect strings to have an `append` method? Why (not)? Try it.

**5.106.** Can you also create a list of lists?

**5.107.** Now do the same using a `while` loop.

**5.108.** When programming the `for`-loop, did you loop over indices (e.g., `for i in range(len(names)):` or over list elements (`for name in names`)?

**5.109.** Write a program to count how many odd numbers are in a list, printing the result.

**5.110.** Sum up all the even numbers in a list.

**5.111.** Sum up all the negative numbers in a list.

**5.112.** Write a program that prints all and only list elements with even indices (0, 2, 4, ...).

**5.113.** Count how many words in a list have length 5.

**5.114.** Sum all the elements in a list up to but not including the first even number. (What if there is no even number?)

**5.115.** Count how many words occur in a list up to and including the first occurrence of the word _the_. (What if _the_ does not occur?)

**5.116.** Write a program that prints out the first `n` triangular numbers. For instance, with `n = 5`, it should print the result of 5+4+3+2+1, i.e., `15`.

**5.117.** Write a program which prints `True` when `n` is a prime number and `False` otherwise.

**5.118.** Write a program that counts the number of even digits in a number `n`.

**5.119.** Write a program that computes the sum of the squares of the numbers in the list `numbers`. For example a call with `numbers = [2, 3, 4]` should print the result of 4+9+16 which is `29`

**5.120.** Place a hashtag `#` before a line of code that previously worked, and record what happens when you rerun the program. Whatever follows `#` is treated as a _comment_ and ignored by Python.

**5.121.** Write a program that concatenates all words in the list `words = ['apple', 'pear', 'banana', 'strawberry']`, placing one after the other with dashes `-` in between.

**5.122.** Generalize the preceding program to allow changing the connector (e.g., dash, space, underscore) by assigning this to a variable `connector`.

**5.123.** Given a list, write a Python program to swap first and last element of the list. Does your program work if the list has only one element? What should it do if the input list has zero elements?

**5.124.** What happens if you enter `AAAARGH I hate Python!` in the interpreter? And what if you surround it by quotation marks?

**5.125.** What happens if you enter `import this` in the interpreter? (`import` will be explained later.)

**5.126.** Assume the days of the week are numbered 0,1,2,3,4,5,6 from Monday to Sunday. Write a program that asks a day number, and prints the day name (a string).

**5.127.** Oops! Your client prefers to number the days from 1 (Monday) to 7 (Sunday). Can you modify the above program to fit their use case? How many changes did you need to make?

**5.128.** In the above program, did you use `if` statements? Try to write this program without using `if` statements, by using a list of day names instead. Does this make the program easier to modify if the client changes their mind again?

> **Note:** Whenever you need a mapping from integer numbers to something else, such as strings, use a list, which is precisely that. For a mapping from things other than integer numbers, we will learn about another datastructure later, the _dictionary_.

**5.130.** You go on a wonderful holiday leaving on day number 3 (a Wednesday). You return home after 137 sleeps. Write a general version of the program which asks for the starting day number, and the length of your stay, and it will tell you the name of day of the week you will return on.

**5.131.** Lists and strings are similar in many ways. Describe and show with code three ways in which they are alike, and three which in which they are not alike (remember _mutability_ from earlier).

**5.132.** How do you select the first element of a list? How do you select the `n`th element of a list? What happens if `n` is larger than the list's length? How do you select the last element of a list? How do you select the pre-last element of a list?

**5.133.** Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.

### 6. Functions

**6.135.** Write a function `print_spam` that prints the string _spam_.

**6.136.** Write a function `print_multiple` that is given a list, and prints each list element on a new line.

**6.137.** Write a function `print_multiple_oneline` that is given a list, and prints all list elements on a single line, concatenated with dashes in between.

**6.138.** Modify the original `print_multiple` to take an additional boolean argument `oneline`, such that `print_multiple([1, 2, 3], True)` prints all numbers on one line, and `print_multiple([1, 2, 3], False)` prints each number on a new line.

**6.139.** Write a function that takes three numbers and returns their sum.

**6.140.** Write a function that takes three numbers and returns their average.

**6.141.** Write a function that takes a list of numbers and returns their sum.

**6.142.** Write a function that takes a list of numbers and returns their average.

**6.143.** What happens if your script calls a function before defining it?

**6.144.** Write a function `find` that takes a string and a character, and returns the index of the first occurrence of that character in the string. For instance, `find('david', 'v')` returns `2`. Could you argue that `find` is kind-of the inverse of the square brackets notation for retrieving a character by index?

**6.145.** Write a function `find_in_list` that does the same, but for a list instead of a string. How much code could you reuse?

**6.146.** Write a function named `right_justify` that takes a string named `s` as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 40 of the display.

**6.147.** The four compass points can be abbreviated by single-letter strings as `'N'`, `'E'`, `'S'`, and `'W'`. Write a function `turn_clockwise` that takes one of these four compass points as its parameter, and returns the next compass point in the clockwise direction. What should this function do if you give it some 'illegal' input, e.g., `'A'`?

**6.148.** Explain the difference between `type(turn_clockwise)` and `type(turn_clockwise('N'))`.

**6.149.** Also write `turn_counterclockwise`. Should `turn_counterclockwise(turn_clockwise('N')) == 'N'` evaluate to `True`? Does it?

**6.150.** If applicable, streamline the functions `turn_clockwise` and `turn_counterclockwise` with the help of a list datastructure.

**6.151.** Write a function `get_day_name` that converts an integer number 0 to 6 into the name of a day. Assume day 0 is Sunday. Return `None` if the arguments to the function are not valid.

**6.152.** Write the inverse function `get_day_num` which is given a day name, and returns its number. Once again, if this function is given an invalid argument, it should return `None`.

**6.153.** If applicable, streamline the functions `get_day_name` and `get_day_num` with the help of list and/or dictionary datastructures.

**6.154.** Write a function `add_to_day_name` that helps answer questions like 'Today is Wednesday. I leave on holiday in 19 days time. What day will that be?'. So the function must take a day name and a `num_days` argument -- the number of days to add -- and should return the resulting day name.

**6.155.** Can your `add_to_day_name` function already work with negative deltas? For example, -1 would be yesterday, or -7 would be a week ago. If your function already works, explain why. If it does not work, make it work. Consider how the modulo `%` operator works.

**6.156.** Write a function `month_to_ndays` which takes the name of a month, and returns the number of days in the month. Ignore leap years.

**6.157.** Write a function `time_to_secs` that takes three arguments -- hours, minutes, seconds -- and converts the time these jointly represent to a total number of seconds, which it returns as output.

**6.158.** Extend `time_to_secs` so that it can cope with real values as inputs. It should always return an integer number of seconds (truncated, or rounded down, towards zero).

**6.159.** Write three functions that are the _inverses_ of `time_to_secs`: 1. `hours_in` returns the whole integer number of hours represented by a total number of seconds; 2. `minutes_in` returns the whole integer number of left over minutes in a total number of seconds, once the hours have been taken out; 3. `seconds_in` returns the left over seconds represented by a total number of seconds. You may assume that the total number of seconds passed to these functions is an integer.

**6.160.** Use again the function `print_spam` from above, that simply prints the string _spam_. What is the difference between `print_spam` and `print_spam()`? What are their types (according to `type`)?

**6.161.** Write a function `do_twice` that takes a function `f` as a parameter, and calls that function twice. Then call `do_twice` with the function `print_spam` as its parameter. What happens if you give `print_spam()` (with parenthesis) as parameter? Why?

**6.162.** Modify `do_twice` so that it takes two arguments, a function object and a value, and calls the function twice, passing the value as an argument. What happens if you enter `do_twice(print_spam)`? Why? What happens if you enter `do_twice(print, 'spam')`?

**6.163.** Define a new function called `do_four` that takes a function object and a value and calls the function four times, passing the value as a parameter. Try to achieve this with only two statements in the body of this function, not four.

**6.164.** Earlier we saw what happens if you call a function before defining it (try again!). What happens if your function call is inside another function, e.g., your implementation of `do_four` should involve a call to `do_twice`. Does the order of the two function definitions -- `do_four` and `do_twice` -- matter? Why would this be?

> **Note:** Now you know how to define a function, but _when_ should you turn a piece of code into a function? This is an art, but there are some useful rules of thumb. For instance, any chunk of code should _do a single thing, at a single level of abstraction_ -- that makes it much easier to read, understand and modify code. Functions make this possible. Also, define a function whenever you find you are repeating chunks of code (the motto _DRY_ = Don't Repeat yourself). Why would repeating code be such a bad thing (multiple good answers possible)? Dividing code into functions is sometimes called _chunking_.

**6.166.** Write a `compare` function that returns `1` if `a > b`, `0` if `a == b`, and `-1` if `a < b`. Examples: `compare(5, 4) == 1`, `compare(7, 7) == 0`, `compare(2, 3) == -1`.

**6.167.** Write a function called `hypotenuse` that returns the length of the hypotenuse (Dutch: 'schuine zijde') of a right triangle, given the lengths of the two legs adjacent to the right angle as parameters. Examples: `hypotenuse(3, 4) == 5.0`, `hypotenuse(24, 7) == 25.0`.

**6.168.** Write a function called `is_even` that takes an integer `n` as an argument and returns `True` if the argument is an even number and `False` if it is odd. Define unit tests for this function.

**6.169.** Is there a difference between `is_even(4)` and `is_even(4) == True`? Which formulation would be considered more _Pythonic_?

**6.170.** Now write the function `is_odd` that returns `True` when its integer argument `n` is odd and `False` otherwise. Define unit tests for this function.

**6.171.** Write a function `is_factor` with integer parameters `f`, `n` that passes these tests: `is_factor(3, 12)`, `not is_factor(5, 12)`, `is_factor(7, 14)`, `not is_factor(7, 15)`, `is_factor(1, 15)`, `is_factor(15, 15)`, `not is_factor(25, 15)`.

**6.172.** Write `is_multiple` to satisfy these statements: `is_multiple(12, 3)`, `is_multiple(12, 4)`, `not is_multiple(12, 5)`, `is_multiple(12, 6)`, not `is_multiple(12, 7)`.

**6.173.** Write the function `farenheit_to_celcius` designed to return the integer value of the nearest degree Celsius for given temperature in Fahrenheit, and its inverse `celcius_to_farenheit`. Extract suitable test cases from a conversion table on the web.

**6.174.** Write a function `has_any_odd` that takes a _list_ of integers as argument, and returns `True` if it contains at least one odd number, and `False` if it contains no odd numbers. Does your function ever inspect more list elements than necessary to reach a conclusion? If so, try to streamline your function; note that return statements can be placed inside a loop, and a function can have multiple return statements. Streamlining does not just serve efficiency; it should also improve the readability of your code.

**6.175.** Write a function `has_only_odd` that takes a list of integers as argument, and returns `True` if all numbers in the list are odd, and `False` otherwise. Again try to streamline your result.

**6.176.** Write a function `has_three_odd` that takes a list of integers as argument, and returns `True` if, and only if, at least three numbers in the list are odd.

**6.177.** Write a function that, given a list and two integer positions in the list, swap the two elements in the list. Does your function modify the input list _in-place_, or create a new list?

**6.178.** Write an analogous function for swapping two characters a string.

**6.179.** Suppose any line of text can contain at most one url that starts with `http://` and ends at the next space in the line. Write a fragment of code to extract and print the full url if it is present. (Hint: read the documentation for `find`.)

**6.180.** Write a function that counts the number of vowels in a string, and prints _evenly voweled!_ if it has an even number, otherwise _oddly voweled!_.

**6.181.** Write a function that takes a string, namely an English sentence, and prints the number of words in the sentence. Hint: Generally speaking, in written English, how do you know a new word is beginning?

**6.182.** Write a program that takes a string and creates a new string where all vowels have been replaced by `y`. Could you change the program to modify the original string _in-place_, instead of returning a changed copy?

**6.183.** Write a program that repeatedly gets numbers from the user (using the `input` function), until the user enters _done_. Once _done_ is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, print an error message and skip to the next number.

**6.184.** Write a function that takes a string, namely an English sentence, and returns a list containing its separate words. Congratulations, you have programmed a _tokenizer_! Can you spot some room for improvement? You can make your tokenizer as advanced as you like.
