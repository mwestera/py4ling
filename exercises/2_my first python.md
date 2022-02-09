# Python for linguists


## 2. My first Python (`print`, variables, `=`, `==`, `+`, ...)

**2.1.** In the Python console, write a print statement such as `print('Hello, world!')` and press the Enter key to execute it.

**2.2.** Write something again, but instead of executing it, cancel it using `ctrl+c` or `cmd+c`. This will be useful to remember.

**2.3.** When executing a print statement, what happens if you leave out both of the parentheses? What happens if you leave out only the parenthesis open? Or only the closing parenthesis?

- - - - - -
**Something to keep in mind:** Like many IDEs, PyCharm will often auto-complete your parentheses or quotation marks. Hence, if you want to leave out a parenthesis or quotation mark _on purpose_, as required for these exercises, then you need to pay attention that PyCharm didn't mess with what you intended to type.
- - - - -

**2.4.** If you are trying to print a string, what happens if you leave out one of the quotation marks? (Try both the starting and the ending quotation mark.) What if you leave out both quotation marks? What might the error messages mean?

**2.5.** Try both single and double quotation marks around the string: `print('cheese')` and `print("cheese")`. What happens if you mix different types of quotation marks? Why?

**2.6.** What happens if you use two single quotation marks at the start and end, e.g., `print(''cheese'')`? What if you use three `'''`? (Triple-quotation-marked strings are a bit special; we will learn about them later.)

**2.7.** What happens if you enter `primt('cheese')`? What happens if you enter `print('cheeze')`? Can you explain why?

- - - - - -
**Something to keep in mind:** Whenever you learn something new, stick with it for a while, to explore different variants and _find ways to break it_. By consciously introducing errors and learning to recognize what happens, you will become good at diagnosing the problem when you make unintentional mistakes later.
- - - - -

**2.8.** What happens if you split a print statement over multiple lines, like below. Experiment with different places of putting the newline; which places give an error?

```python
print(
'Hello, world!')
```


**2.9.** Try using the Python console as a calculator, using numbers and operators like + and -. Which operators does Python recognize? What does `**` do?

**2.10.** What happens if you put a minus sign before a number? What happens if you put a plus sign before a number? What do `2+-2` and `2++2` do? (Spoiler: For readability, you would normally write these as `2 + -2`, or simply `2 - 2`, and `2 + 2`, respectively.)

**2.11.** In math notation, leading zeros are ok, as in `09`. What happens if you try this in Python?

**2.12.** What happens if you have two values with no operator between them?

**2.13.** Add parentheses to the expression `6 * 1 - 2` to change its value from `4` to `-6`.

**2.14.** How many seconds are there in 42 minutes 42 seconds?

**2.15.** How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.

**2.16.** What does `blabla = 5` do? Subsequently, what does `print(blabla)` do?

- - - - - -
**Something to keep in mind:** The equals sign `=` is used for **assigning** a value (on the right of the `=`) to a variable (on the left). When you subsequently need the same value, you can refer to it using the variable.
- - - - -

**2.17.** Can a variable name contain a number? Can it start with a number? Can it contain a space? A quotation mark? An underscore? Explore what other special characters can be used in your variable names. Try some legal and some illegal variable names.

**2.18.** Assignment like `n = 42` is legal. What about `42 = n`? And how about `x = y = 1`? If it is legal, what is the result (try printing the variables)?

**2.19.** In math notation you can multiply variables _x_ and _y_ like this: _xy_. What happens if you try that in Python? Why?

**2.20.** Can you reuse variables, i.e., assign a new value to an existing variable?

**2.21.** Write and execute three lines of code that: (i) create a variable with the value 37; (ii) create another variable with the value 4; (iii) print out the result of multiplying those variables together.

**2.22.** First enter `n = 42`. Then for each of the following, try to predict what it does, and then try it and make sure you understand what is happening: 
- `n = 100` 
- `n = n` 
- `n = n + 3` 
- `n -= 3` 
- `n = 'n'` 
- `'n' = n` 
- `n = 'n + 3'`

**2.23.** Assign a string like `'hello!'` to a variable, then print it. Now assign a different string to the same variable and print it again. What advantage of variables might this exercise illustrate?

**2.24.** In the Python console enter `abcdefg + 4`. What happens and why? Next, assign a value to `abcdefg` so that, subsequently, `abcdefg + 4` evaluates to `10`.

**2.25.** In some languages every statement ends with a semi-colon, `;`. What happens if you put a semi-colon at the end of a Python statement? Or a colon `:`?

**2.26.** If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average speed in kilometers per hour?

**2.27.** What is the area of a circle with radius 3? What is the volume of a sphere with radius 5?

**2.28.** Create a Python file (e.g., `exercises2.py`), open it in the editor (if not opened automatically), enter `print('Hello, world!')` in the file and run it.

**2.29.** Compare what happens in the Python console vs. running a Python script containing the same code; try at least: 
- `print('cheese')` vs. `'cheese'` 
- `print(n)` vs. `n` (assuming `n` still has a value from before)

**2.30.** Take a statement that runs (e.g., `print('Hello, world!')`), add one or more spaces in front of it and try to run it again. What happens? Do the console vs. running a script behave the same in this regard?

- - - - - -
**Something to keep in mind:** Unlike in many other programming languages, in Python **indentation is meaningful**. Later we will see cases where you _must_ indent.
- - - - -

**2.31.** Suppose the cover price of a book is €24.95, but bookstores get a 40% discount. Shipping costs €3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?

**2.32.** `%` is the modulo operator, look it up if you need to. Evaluate each of the following numerical expressions in your head, then use the Python console to check your results. What happens in each case? Why? 
- `5 % 2` 
- `9 % 5` 
- `15 % 12` 
- `12 % 15` 
- `238 % 24` 
- `6 % 6` 
- `0 % 7` 
- `7 % 0`

**2.33.** `//` is the integer division operator. What does it do?

**2.34.** Compute in your head (or on paper) the result of `3 * (10 // 3) + 10 % 3`, and verify your own answer by subsequently trying it in Python.

- - - - - -
**Something to keep in mind:** Some of these exercises are about language, or at least about strings like words and sentences; but in these early sections most of them aren't. The initial purpose for these exercises is for you to learn Python syntax and semantics and acquire a programmer's way of thinking. Later we will learn how to apply these skills specifically to natural language.
- - - - -

**2.35.** If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per kilometer in minutes and seconds)? It can be useful to first compute the time per kilometer in seconds and store this in a variable, before processing it further to separate minutes from seconds. (What are some disadvantages if you _don't_ store this intermediate result?)

**2.36.** If I leave my house at 6:52 am and run 1 km at an easy pace (6:15 per km), then 3 km at tempo (4:42 per km) and 1 km at easy pace again, what time do I get home for breakfast?

**2.37.** What do the built-in functions `max` and `min` do? For example, try `max(3, 4, 5)`, `min(5, -11, -2, 99)`, and `max(10)`; can you guess what the error means?

**2.38.** What happens if you accidentally put a space between the function name and the parentheses (against Python style): `max (3, 4, 5)`? What if you forget the parentheses altogether?

**2.39.** In maths it is common to compare numbers or variables with _greater than_, _smaller than_, _not equal to_, and so on. Experiment with the operators `>`, `<`, `!=`, `>=`, `<=` to figure out what they do.

**2.40.** Put the `not` operator in front of some of the expressions you tested, e.g., `not (3 >= 4)`. What does it do? What about `not True` and `not False`? Inspired by the meaning of the operator `!=`, could you also use exclamation mark `!` instead of `not`?

**2.41.** When using the `not` operator, can you leave out the parentheses, like `not 3 >= 4`? Compare this how the `max` function behaved above.

- - - - - -
**Something to keep in mind:** Python has various built-in **functions** and **operators**. Calling a function (such as `max` and `print`) requires parentheses directly following the function name, with no space (`max(...)`). By contrast, operators (such as `not`) do not require parentheses, and are followed by a space (e.g., `not 3 >= 4`), though often parentheses increase readability (e.g., `not (3 >= 4)`), and they can also matter for operator precedence (see next exercises).
- - - - -

**2.42.** Explore how boolean operators `and` and `or` work. Does `or` correspond to inclusive or exclusive _or_?

**2.43.** Let `cloudy = True` and `windy = True`, and `sunny = not cloudy`, and test whether it is nice day to go to the beach for flying a kite.

**2.44.** Predict, test and explain the difference between `not sunny or cloudy` and `not (sunny or cloudy)`.

**2.45.** Verify your previous explanation by considering the table of **operator precedence** in Python: https://docs.python.org/3/reference/expressions.html#operator-precedence

**2.46.** Ooh, the weather changes! Reassign `cloudy = False`. Did the variable `sunny` automatically update as well?

- - - - - -
**Something to keep in mind:** Variables are 're-assigned' independently of one another. Even if two variables are initially made to refer to the same thing, reassigning something to one variable doesn't automatically reassign the other.
- - - - -

**2.47.** Assign `my_variable = 6`. What happens if you subsequently do `my_other_variable = my_variable`? What if you then reassign `my_variable = 20`, can you predict what happens to the value of `my_other_variable`? Test your prediction.

**2.48.** Numerical expressions can be implicitly converted to boolean values (more about _type conversions_ later). Try to understand this: 
- `not 0` 
- `not 1` 
- `not 100` 
- `not -1`

**2.49.** Given the foregoing, can you predict the value of `not (0 + 1)` vs. `not 0 + 1`? Verify your prediction, and compare it with `not (False or True)` vs. `not False or True`. Make sure you understand this potentially puzzling behavior (see again the _operator precedence_ table).

**2.50.** First enter `n = 42`, and then `n == 42`. What is the result? What about `n == 43`? What happens if you try to assign a new variable with `==`, e.g., `z == 123` (assuming you haven't used `z` before)?

**2.51.** We have already seen you can create a string by using quotation marks. Try to predict which one of these is legal, what the result is, and why: 
- `fruit = 'apple'` 
- `fruit = apple` 
- `'fruit' = 'apple'` 
- `fruit == apple` 
- `'fruit' == 'apple'` 
- `'fruit' == apple`

**2.52.** What does this code do: `a = 3 == 3`? What is the result and why? What's the difference between that code snippet and this one: `a == 3 = 3`? Why does the latter produce an error?

- - - - - -
**Something to keep in mind:** While single `=` is used for **assigning** a value to a variable, double `==` tests for **equality**. It matters how you read them, whether mentally or out loud. If you read both simply as _'is'_, you are prone to confuse yourself.
- - - - -

**2.53.** What do these expressions evaluate to? 
- `3 == 3` 
- `3 != 3` 
- `3 >= 4` 
- `not (3 < 4)` 
- `3 % 4 == 0` 
- `3 % 4 == 3` 
- `3 / 4 == 0` 
- `3 // 4 == 0` 
- `3+4 * 2 == 14` 
- `4 - 2 + 2==0`

**2.54.** Give the logical opposites of these conditions: 
- `a > b` 
- `a >= b` 
- `a >= 18 and day == 3` 
- `a >= 18 and day != 3`.

**2.55.** Given two integer numbers, assigned to variables `x` and `y`, what is the value of `x == (y * (x // y) + x % y)`. Can you change the value by changing the numbers assigned to `x` and `y`? How / why not?

**2.56.** You look at the clock and it is exactly 2pm. You set an alarm to go off in 51 hours. At what time does the alarm go off? (Whenever a value increases and then goes back to zero, again and again, like hours on the clock, modulo can be useful.)

**2.57.** In the interpreter enter `name = input('What is your name?')`. What does it do? Enter something in the interpreter and press enter. Next, look what's in the variable `name`.

**2.58.** In a Python script, write a program that asks for the user's name and prints the name three times (each can be on a separate line).

