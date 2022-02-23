# Python for linguists


## 5. If-clauses (`if`, `elif`, `else`)

**5.1.** Create a Python script with the following, predict what it does and test your prediction:

```python
if 4 + 2 == 6:
    print('yes!')
```


**5.2.** After learning something new, stay with it for a while, exploring it and finding ways to break it. Modify various things, for example, what if you replace `==` by `=`? (Undo that.) What if you remove the colon `:`? (Undo that.) What if you change the condition (`4 + 2 == 6`) into something that is always false?

- - - - - -
**Something to keep in mind:** The `if`-clause consists of a **header** `if 4 + 2 == 6:` and a **suite** `print('yes!')`, also called the **body** of the if-clause. We will see various other types of clauses later, always consisting of a header and a suite, e.g., for-loops and function definitions. The header of a clause always ends with a colon `:`. The suite/body typically starts on a new line, and must be indented.
- - - - -

**5.3.** What happens if you remove the indentation, i.e., if header and suite start at the same level?

**5.4.** What if you place the print statement on the same line as the if-statement, i.e., after the colon?

**5.5.** What is being printed by the following program:

```python
if 1 + 1 == 5:
    print('uuuuhm...')

print('print this!')
```


**5.6.** What happens if you indent the second print statement to the same level as the first print statement? (Undo that.) What if you replace the condition by something true? What happens if you remove the newline between the two statements? What if you indent the second print statement again, but now add several newlines between the two print statements?

- - - - - -
**Something to keep in mind:** _Indentation is meaningful_ in Python, whereas in most other programming languages it is only an optional style convention.
- - - - -

**5.7.** In your Python editor (or the interpreter), can you indent with the 'tab' key? Do these appear as proper tabs (large spaces) or are they replaced by sequences of multiple normal, narrow spaces? If the latter, you're safe; if the former, you need to pay extra attention: you can indent either with tabs or with spaces, but don't mix them!

**5.8.** Write a program that, given a variable `n` with a number, tests if its value is odd, and if not, adds 1 to it and prints _I've made it even!_. Subsequently, regardless of whether it was originally even or odd, the program should always print the resulting value of `n`.

**5.9.** Write a program that, given a variable `name` containing a string, tests if the first letter is `a`, and, if so, prints _The first letter is 'a'!_. Only if the first letter is 'a', it should additionally test if the second letter is 'b', and if so, print _The word starts with 'ab'!_. Your second `if` can be nested under the first `if` -- make sure the indentation reflects this. Apply your program to a number of strings to test, such as _able_, _apple_ and _banana_.

**5.10.** Write a program that asks for the user's name, tests if it starts with a vowel, and if so, prints _You are a vowel person!_.

**5.11.** Are the headers `if True:` and `if False:` accepted by Python (together with a suitable suite)? What do these conditions achieve?

**5.12.** You can follow an if-clause with an else-clause, which consists of its head `else:` and one or more statements as a suite. Use `else:` to expand the previous program to print _You are a consonant person!_ in the right circumstances.

**5.13.** Is your program robust to users (not) capitalizing their name?

**5.14.** Now write a program that basically does the same, but is coded in the reverse order: it first tests if the name starts with a _consonant_, and if so prints _You are a consonant person!_; otherwise print _You are a vowel person!_. Did you type a long string of all the consonants to implement this? If so, could this be avoided?

**5.15.** Write a program that tests whether the value of a variable `n` is odd (i.e., not divisible by 2), if so print _Odd!_, and if not print _Even!_.

**5.16.** Oops, our client requests a change: they want to the program to print, on the same line as _Odd!/Even!_, whether the number `n` is greater than 10, equal to 10, or smaller than 10.

**5.17.** Our client requests another feature: if the number is both odd and greater than ten, that's a very special case where it should print only _ALARM!!!_ and nothing else.

**5.18.** Python's `elif` is shorthand for `else, if`. Can you predict what the following program does?

```python
if n > 0:
    print('Positive!')
elif n == 0:
    print('Zero!')
else:
    print('Negative!')
```


**5.19.** Together, the if-clause, elif-clause and else-clause form a **compound clause**. Can you have an `elif` and/or an `else` clause without an initial `if` clause? Can you have more than one `elif`?

**5.20.** What happens if you specify a condition also in the `else` header, e.g., `else n < 0:`?

**5.21.** In an if-elif-else compound clause, what happens if one of the three clauses has an empty suite (e.g., delete or comment out (`#`) one of the print statements in the code above).

**5.22.** If possible, use `elif` to improve the readability of the 'odd/even/greater than 10' program from a few exercises ago, for instance by avoiding (deeply) nested if-clauses.

- - - - - -
**Something to keep in mind:** Nested if-clauses are frowned upon as an 'anti-pattern' in programming, to be avoided because they make code difficult to read and maintain -- and this applies not only to `if`-clauses (see also `for`-clauses below).
- - - - -

**5.23.** We both flip a coin (outside Python), and manually store the outcomes in two boolean variables `player1` and `player2`. If both came up heads, print _We both won!_, if both came up tails, print _Play again._, if only the first comes up heads, print _Player one won._, if the second, print _Player two won._.

**5.24.** Does your code for the previous exercise contain nested if-clauses? Implement a version without nested if-clauses. Besides `elif`, you can also reduce nested ifs by combining your conditions using boolean operators like `and` and `or`.

**5.25.** How often does your coin-flip program check the variables `player1` and `player2`? If either variable is checked more than twice, you are checking more than you need to; try to simplify your code.

**5.26.** Write a program that takes two strings from the user (one after the other). If either one is less than three characters long, it prints _You are disqualified_. Otherwise, if the two strings are not equal but one string is contained in the other, it prints _Yay well done!_, otherwise _Nope_.

**5.27.** Write a program that takes a word as input from the user, and checks the first two characters: if one is a vowel and the other a consonant (in either order), create a new string where the two characters are swapped; otherwise leave the string unchanged. Print the resulting string. Can you think of an English word that turns into another proper English word?

**5.28.** Write a program that takes a word as input from the user, tests a number of things in a row, and prints a single line of appropriate feedback: 
- whether it starts with two vowels, with a single vowel, or with a consonant 
- whether it has an even or odd number of characters 
- if odd, what the middle character is, and if even, what the middle two characters are 
- whether it is a palindrome (hint: use string slicing).

