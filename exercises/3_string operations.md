# Python for linguists


## 3. String operations (`+`, `len`, `[]`, `f''`)

**3.1.** You know that Python can add and multiply numbers with `+` and `*`. Do these operations also work on strings? Try `'apple' + 'pear'`, `'apple' * 'pear'`, `'apple' * 5`, `'pear' + 5` and others. Which mathematical operations work on strings, and which ones don't? Which types of errors do you get?

**3.2.** How do you add two strings together with a dash "-" in between? And with a space in between? And with five spaces in between?

**3.3.** For the sentence _All work and no play makes Jack a dull boy_, first store each word in a separate variable, and, using these, print out the sentence on one line.

**3.4.** What happens if you try to create a string, but the string contains a new line, e.g.:

```python
sentence = 'apples do not fall
far from the tree'
```


**3.5.** Newlines in your string are no longer a problem if you use triple quotation marks (`'''` or `"""`) at the start and end. Fix the previous code so it runs correctly. If you print the string, does the newline survive?

**3.6.** You can also add newlines to your string by typing `
` as part of the string, e.g., `'apples do not fall
far from the tree'`. Here backslash `\` is used as an _escape operator_; it is used for various other special characters as well, e.g., `\t` for a tab. Very handy! But what should you do if you want to create a string that contains an actual backslash?

**3.7.** Print a string that contains single or double quotation marks, such as _She said: "Hello!"_ and _She said: 'Hello!'_. Can you get it to work (there are several ways)? Can you also print a string that contains both single and double quotation marks?

**3.8.** Do the comparison operators `>` and `<` work on strings, e.g., `'apple' < 'pear'`? What do they mean in this context? Can you explain `'300' > '4'`? What about `'300' > 4`?

**3.9.** For each of the following, explain whether it's true or false (or neither...) and why: 
- `'hat' == "hat"` 
- `hat == 'hat'` 
- `1/3 == .33` 
- `'three' > 'two'` 
- `2 + 2 = 4`

**3.10.** What happens if you feed the built-in functions `max` and `min` a string as argument (e.g., `max('apple')`, `min('bonanza')`)? And what about multiple strings, `max('apple', 'aardvark', 'banana', 'zebra')`? Can you explain the result of `max('250')`? And `min('-852')`? And `max('123abc')`?

- - - - - -
**Something to keep in mind:** To get the most out of these exercises, try not to use any built-in methods other than the ones mentioned in the exercises that came before. Later on, we will learn about convenient shortcuts for some of the things you are asked to do, as well as familiarize ourselves with powerful natural language programming libraries.
- - - - -

**3.11.** What does `len('apple')` do? Apply `len` to different strings.

**3.12.** Can you also get the length of a number, e.g., `len(3)`? What about a boolean? What about the length of the empty string?

**3.13.** What happens if you type `length` instead of `len`? What happens if you forget the quotation marks of the string, or a parenthesis?

**3.14.** In some programming languages, `len` is a method that 'belongs to' the string class, requiring you to type for example `'apple'.len()`. What happens if you do that in Python? What about the ugly `'apple'.__len__()`? Python's so-called _dunder_ (double underscore) methods will be explained later.

**3.15.** The `in` keyword does what you would expect: it checks if one thing is in another. Try `'p' in 'apple'`, and `'q' not in 'apple'`. Can you use `in` to check for larger substrings (e.g., `app`), or only single characters? According to `in`, does a string contain itself?

**3.16.** Suppose we have a single character assigned to the variable `char`. In ordinary English, describe what the following means: `char in 'aeoui'`. Does it work on capital letters?

**3.17.** Assign a variable `name = 'Michael'`. What do each of the following do: 
- `name[1]` 
- `name[2]` 
- `name[8]` 
- `name[-1]` 
- `name[-2]` 
- `name[1:3]` 
- `name[2:2]` 
- `name[-2:]` 
- `name[2:]` 
- `name[:2]` 
- `name[0]` 
- `name[2-4]` 
- `name[3-2]` 
- `name[1+1]`

**3.18.** You can also indicate the _step size_ when slicing, by adding another colon and a number. What does `name[::2]` do? What about `name[::-1]`? And `name[1:5:2]`?

- - - - - -
**Something to keep in mind:** The square brackets operator `[]` lets us select characters, contiguous substrings, and even non-contiguous substrings. This is called _slicing_ the string.
- - - - -

**3.19.** By using _only slicing_, extract only the odd-position characters from `michael` (assuming the `m` is at position 0, i.e., even). And can you also obtain the string `eh` from the string `michael` by using only slicing? What about the string `ehm`?

**3.20.** Perhaps you'd expect to be able to change the string in `name` by replacing a character like this: `name[2] = 'b'`, expecting the result `Mibhael`. But this doesn't work; what does the error message say? This is because strings are not _mutable_: once you create a string, you cannot change it, only create a new one that is different. We return to mutability later.

**3.21.** Can you predict what `'0123456'[3]` does? What about `'1234567'[3]`?

**3.22.** What does `name[len(name)]` do? What about `name[len(name)-1]`? Why?

**3.23.** Predict the outcomes of `len('apple' * 5)` and `len('apple') * 5`, then test your expectation.

**3.24.** Python's string class provides various methods, including `upper` and `lower`. What would you expect them to do? As methods of the string class, you call them like this: `'apple'.upper()`.

**3.25.** For some arbitrary string assigned to variable `s`, is the following true: `s == s.upper().lower()`.

**3.26.** In a Python script write a program that uses `input` to ask for the user's name, and subsequently print _Hi [name], how are you?_

**3.27.** In all of the Python scripts you create, add a _comment_ with the exercise number above the relevant chunk of code, e.g., `# Ex 1.23`, so that you can retrieve your own solutions later. Any text or code preceded by `#` is ignored by Python, as it represents a comment meant for humans.

**3.28.** Write an expression that, given a string `s`, gets rid of the last 4 characters.

**3.29.** Write an expression that, given a string `s`, evaluates to `True` if the first character of the string is a vowel, and `False` otherwise. Is your expression robust to capitalization differences? Can you improve this using `upper` or `lower`?

**3.30.** Write an expression that, given a string `s`, evaluates to `True` if the last character of the string is a consonant, and `False` otherwise. Did you use the boolean operator `not`?

**3.31.** Write a `print` statement that, given a string `s` and an integer `cut_at`, prints two substrings: the starting portion until the position indicated by `cut_at`, and the remainder.

**3.32.** Python's **format strings** can help you easily print stuff in a readable format. You can create a format string in many ways; an easy way is to prefix the string with an `f`, i.e., before the initial quotation mark. Inside a format string, curly braces can contain any Python expression, with some additional formatting options:

```python
print(f'Hi, my name is {name}, which starts with "{name[0]}" and is {len(name)} characters long!')
```


**3.33.** What happens if you forget the `f` prefix in the above example?

**3.34.** What happens if you want to print a format string, but it references a variable that does not exist?

**3.35.** Try printing the same stuff _without_ using a format string. You will need string concatenation instead, and explicitly convert the length to a string using `str(len(name))` (more about type conversion in the next section). Which version of the print statement do you find more readable?

**3.36.** Format strings have many more options; see what the following do:

```python
my_number = 6.1239871
print(f'{my_number} or {my_number:.6f} or {my_number:.4f} or {my_number:.2f}')')

my_string = 'just testing'
print(f'left {my_string:>20} right')
print(f'left {my_string:<20} right')
print(f'left {my_string:^20} right')
```


