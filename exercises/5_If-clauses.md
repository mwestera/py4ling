# Python for linguists


## 5. If-clauses (`if`, `elif`, `else`)

**5.1.** Create a python script containing `if 4+2 == 6: print('yes!')`, and execute it. Now try to break it by modifying different things, for example, what if you replace `==` by `=`? (Undo that.) What if you remove the colon `:`?

**5.2.** Now change the condition (`4+2 == 6`) into something that is always false, and execute it again. Did it print anything?

- - - - - -
**Something to keep in mind:** Some terminology: the `if`-clause consists of a **header** `if 4+2 == 6:` and a **suite** `print('yes!')`, also called the **body** of the if-clause. We will see various other types of clauses later, always consisting of a header and a suite, e.g., for-loops and function definitions. The header of a clause always ends with a colon `:`.
- - - - -

**5.3.** After the header, the clause's suite/body is typically placed on a new line, where it _must_ be indented (i.e., spaces at the front). Change the previous program to make this the case, and run it again; e.g.:

```python
if 4+2 == 6:
    print('yes!')
```


**5.4.** What happens if you remove the indentation, i.e., if header and suite start at the same level?

**5.5.** What is being printed by the following program:

```python
if 1+1 == 5:
    print('uuuuhm...')

print('print this!')
```


**5.6.** What happens if you indent the second print-statement to the same level as the first print statement? And what if you now make the condition true (e.g., `1+1 == 2`)? What happens if you remove the newline between the two statements? Or if you add five newlines? Play around!

**5.7.** In an if-clause, does it still work if you place the condition in parentheses right behind the `if`? (This goes against Python style.)

**5.8.** In your Python editor (or the interpreter), can you indent with the 'tab' key? Do these appear as proper tabs (large spaces) or are they replaced by sequences of multiple normal, narrow spaces? If the latter, you're safe; if the former, you need to pay extra attention: you can indent either with tabs or with spaces, but don't mix them!

**5.9.** Write a program that takes a variable `n`, tests if its value is odd, and if not, adds 1 to it and prints _I've made it even!_. Subsequently, regardless of whether it was originally even or odd, the program should always print the resulting value of `n`.

**5.10.** With variable `name` containing a string, write a program that tests if the first letter is `a`, and, if so, prints _The first letter is 'a'!_. Only if the first letter is 'a', it should additionally test if the second letter is 'b', and if so, print _The word starts with 'ab'!_. Your second `if` can be nested under the first `if` -- make sure the indentation reflects this. Apply your program to a number of strings to test, such as _able_, _apple_ and _banana_.

- - - - - -
**Something to keep in mind:** **Indentation is meaningful** in Python, whereas in most other programming languages indentation is only a reading aid. Look up Python's indentation rules if you are unsure.
- - - - -

**5.11.** Write a program that asks for the user's name, tests if it starts with a vowel, and if so, prints _You are a vowel person!_.

**5.12.** You can follow an if-clause with an else-clause, which consists of its head `else:` and one or more statements as a suite. Use `else:` to expand the previous program to print _You are a consonant person!_ in the right circumstances.

**5.13.** Is your program robust to different capitalizations?

**5.14.** Now write a program that likewise asks for the user's name, but then tests if the name starts with a _consonant_, and if so print _You are a consonant person!_; otherwise print _You are a vowel person!_. Did you type a long list of consonants to implement this? If so, could this be avoided?

**5.15.** Place a hashtag `#` before a line of code that previously worked, and record what happens when you rerun the program. Whatever follows `#` is treated as a _comment_ and ignored by Python.

**5.16.** Write a program that tests whether the value of a variable `n` is odd, and if so print _Odd!_, and if not print _Even!_.

**5.17.** Oops, our client requests a change: they want to the program to print, in addition, whether the number `n` is greater than 10 or not.

**5.18.** What happens if `n` is not a number but, say, a string? Make your program more robust by using `isinstance` to test if `n` is a number; if not, print _Wrong input!_.

**5.19.** Our client requests another feature: if the number is both odd and greater than ten, that's a very special case where it should print only _ALARM!!!_ and nothing else.

**5.20.** Python's `elif` is shorthand for `else, if`, and it helps you avoid many nested if-clauses. Make sure you understand the following example:

```python
if n > 0:
    print('Positive!')
elif n == 0:
    print('Zero!')
else:
    print('Negative!')
```


**5.21.** Together, the if-clause, elif-clause and else-clause form a **compound clause**. Can you have an `elif` and/or an `else` without an initial `if`? Can you have more than one `elif`?

**5.22.** Use `elif` to improve the 'odd/even/greater than 10' from a few exercises ago program if possible, avoiding nested if-clauses and removing any repeated code to you used to specify the conditions.

- - - - - -
**Something to keep in mind:** Deeply nested clauses are frowned upon as an 'anti-pattern' in programming, to be avoided because they make code difficult to read and maintain -- and this applies not only to `if`-clauses (see also `for`-clauses below).
- - - - -

**5.23.** We both flip a coin, the outcome of which is stored in two boolean variables `player1` and `player2`. If both come up heads, print _We both won!_, if both come up tails, print _Play again._, if only the first comes up heads, print _Player one won._, if the second, print _Player two won._. Implement a version with nested if-clauses, and a version without nested if-clauses. Besides `elif`, you can also reduce nested ifs by combining your conditions using boolean operators like `and` and `or`.

**5.24.** Write a program that takes a word as input from the user, and checks the first two characters: if one is a vowel and the other a consonant, create a new string where the two characters are swapped; otherwise leave the string unchanged. Print the resulting string. Can you think of an English word that turns into another proper English word?

**5.25.** In an if-elif-else compound clause, what happens if one of the three clauses has an empty suite (e.g., delete or comment out (`#`) one of the print statements in the code above).

**5.26.** Are the headers `if True:` and `if False:` accepted by Python (together with a suitable suite)? What do these conditions achieve?

**5.27.** Write a program that takes two strings from the user, prints _You are disqualified_ if either one is less than three characters long, and prints _Yay well done!_ if the two strings are not equal but one string is contained in the other.

