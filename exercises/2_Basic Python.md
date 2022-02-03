# Python for linguists


## 2. My first Python (`print`, variables, `=`, `==`, `+`, ...)

**2.1.** In the Python console, enter a print statement such as `print('Hello, world!')`.

**2.2.** When executing a print statement, what happens if you leave out one of the parentheses, or both?

**2.3.** If you are trying to print a string, what happens if you leave out one of the quotation marks? What if you leave out both?

**2.4.** Try both single and double quotation marks around the string: `print('cheese')` and `print("cheese")`. What happens if you mix different types of quotation marks?

**2.5.** What happens if you use two single quotation marks, instead of a single double quotation mark, e.g., `print(''cheese'')`?

- - - - - -
**Something to keep in mind:** Whenever you learn something new, stick with it for a while, to explore different variants and _find ways to break it_. By consciously introducing errors and learning to recognize what happens, you will become good at diagnosing the problem when you make unintentional mistakes later.
- - - - -

**2.6.** What happens if you enter `primt('cheese')`? What happens if you enter `print('cheeze')`? Can you explain why?

**2.7.** What happens if you split a print statement over multiple lines, like below. Experiment with different places of putting the newline; which places give an error?

```python
print(
'Hello, world!')
```


**2.8.** Try using the Python console as a calculator, using numbers and operators like + and -. Which operators does Python recognize? What does `**` do? What does `//` do? And `%`?

**2.9.** What happens if you put a minus sign before a number? What happens if you put a plus sign before a number? What about `2++2`?

**2.10.** In math notation, leading zeros are ok, as in `09`. What happens if you try this in Python?

**2.11.** What happens if you have two values with no operator between them?

**2.12.** How many seconds are there in 42 minutes 42 seconds?

**2.13.** How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.

**2.14.** If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per kilometer in minutes and seconds)? What is your average speed in kilometers per hour?

**2.15.** We've seen that `n = 42` is legal. What about `42 = n`? And how about `x = y = 1`? If it is legal, what is the result (try printing the variables)?

- - - - - -
**Something to keep in mind:** Some of these exercises are about language, or at least about strings like words and sentences; but most aren't. The initial purpose for these exercises is for you to **learn a new language**, Python, and acquire a programmer's way of thinking. Later we will learn how to apply these skills specifically to natural language.
- - - - -

**2.16.** In math notation you can multiply variables _x_ and _y_ like this: _xy_. What happens if you try that in Python? Why?

**2.17.** What is the area of a circle with radius 3? What is the volume of a sphere with radius 5?

**2.18.** First enter `n = 42`. Then try each of the following. Is it legal, and if so, what does it do? 
- `n = 100` 
- `n = n` 
- `n = n + 3` 
- `n -= 3` 
- `n = 'n'` 
- `'n' = n`

**2.19.** Create a Python script containing `print('Hello, world!')` and run it.

**2.20.** Write and execute three lines of code that: (i) create a variable with the value 37; (ii) create another variable with the value 4; (iii) print out the result of multiplying those together.

**2.21.** Assign a string to a variable, then print it, and print it again. Now assign a different string to the same variable and print it again twice. What advantage of variables does this exercise illustrate?

**2.22.** In some languages every statement ends with a semi-colon, `;`. What happens if you put a semi-colon at the end of a Python statement?

**2.23.** What if you put a period at the end of a statement?

**2.24.** Print a string that contains single or double quotation marks, such as _She said: "Hello!"_ and _She said: 'Hello!'_. Can you get it to work? And how can you print a string that mixes single and double quotation marks?

**2.25.** Compare what happens in the Python console, vs. running a Python script containing the same code; try at least: 
- `print('cheese')` vs. `'cheese'` 
- `print(n)` vs. `n` (assuming `n` still has a value from before)

**2.26.** Take a statement that runs (e.g., `print('Hello, world!')`), add one or more spaces in front of it and try to run it again. What happens? Unlike in many other programming languages, in Python indentation (whitespace at the start of lines) is meaningful. Later we will see cases where you _must_ indent.

**2.27.** Add parentheses to the expression `6 * 1 - 2` to change its value from `4` to `-6`.

**2.28.** In the Python console enter `my_variable + 4`. What happens? Next, assign a value to `my_variable` so that `my_variable + 4` evaluates to `10`.

**2.29.** Suppose the cover price of a book is €24.95, but bookstores get a 40% discount. Shipping costs €3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?

**2.30.** If I leave my house at 6:52 am and run 1 km at an easy pace (6:15 per km), then 3 km at tempo (4:42 per km) and 1 km at easy pace again, what time do I get home for breakfast?

**2.31.** `%` is the modulo operator, look it up if you need to. Evaluate each of the following numerical expressions in your head, then use the Python console to check your results. What happens in each case? Why? 
- `5 % 2` 
- `9 % 5` 
- `15 % 12` 
- `12 % 15` 
- `6 % 6` 
- `0 % 7` 
- `7 % 0`

**2.32.** What do the built-in functions `max` and `min` do? For example, try `max(3, 4, 5)`, `max(10)`, and `min(5, -11, -2, 99)`.

**2.33.** In maths it is common to compare numbers or variables with _greater than_, _smaller than_, _not equal to_, and so on. Experiment with the operators `>`, `<`, `!=`, `>=`, `<=` to figure out what they do.

**2.34.** Put `not` in front of some of the expressions you tested, e.g., `not (3 >= 4)`. What does it do? What about `not True` and `not False`? Inspired by the operator `!=`, could you also use exclamation mark `!` instead of `not`?

**2.35.** Explore how boolean operators `and` and `or` work. Does `or` correspond to inclusive or exclusive _or_?

**2.36.** What is the difference between `not True or False` and `not (True or False)`, and why?

**2.37.** First enter `n = 42`, and then `n == 42`. What is the result? What about `n == 43`? What happens if you try to assign a new variable with `==`, e.g., `z == 123` (assuming you haven't used `z` before)?

**2.38.** Try to predict which one of these is legal, what the result is, and why: 
- `fruit = 'apple'` 
- `fruit = apple` 
- `'fruit' = 'apple'` 
- `fruit == apple` 
- `'fruit' == 'apple'` 
- `'fruit' == apple`.

**2.39.** What does this code do: `a = 3 == 3`? What is the result and why? What’s the difference between that code snippet and this one: `a == 3 = 3`? Why does the latter produce an error?

- - - - - -
**Something to keep in mind:** Single `=` is used for assigning a value to a variable, while double `==` tests for equality. It matters how you read them, whether mentally or out loud. If you read both simply as _is_, you are prone to confuse yourself.
- - - - -

**2.40.** What do these expressions evaluate to? 
- `3 == 3` 
- `3 != 3` 
- `3 >= 4` 
- `not (3 < 4)`

**2.41.** Give the logical opposites of these conditions: 
- `a > b` 
- `a >= b` 
- `a >= 18 and day == 3` 
- `a >= 18 and day != 3`.

**2.42.** Which of the following fail? Explain why. 
- `3 % 4 == 0` 
- `3 % 4 == 3` 
- `3 / 4 == 0` 
- `3 // 4 == 0` 
- `3+4 * 2 == 14` 
- `4-2+2 == 0` 
- `len("hello, world!") == 13`.

**2.43.** You look at the clock and it is exactly 2pm. You set an alarm to go off in 51 hours. At what time does the alarm go off? (Whenever a value increases and then goes back to zero, again and again, like hours on the clock, modulo can be useful.)

**2.44.** Make sure that the variable `my_variable` from before still has `6` as its value. What happens if you now do `my_other_variable = my_variable`? And if you subsequently reassign `my_variable = 20`, can you predict what happens to the value of `my_other_variable`? Test your prediction.

- - - - - -
**Something to keep in mind:** Variabels are 're-assigned' independently of one another. Even if two variables are initially made to refer to the same thing, reassigning something to one variable doesn't automatically reassign the other.
- - - - -

**2.45.** In the interpreter enter `name = input('What is your name?')`. What does it do? Enter something in the interpreter and press enter. Next, look what's in the variable `name`.

**2.46.** In a Python script, write a program that asks for the user's name and prints the name three times (each can be on a separate line).

