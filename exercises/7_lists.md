# Python for linguists


## 7. Lists (`list`, `append`, `[]`)

**7.1.** Assign a variable `names = ['Alf', 'Beth', 'Chris', 'Dave', 'Esra']`. What does `type(names)` say?

**7.2.** Use square brackets `[` and `]` to create a list of numbers, a list of strings, and a list of both numbers and strings. Do these lists all have the same `type`? What about an empty list?

**7.3.** What happens if you try to create a list but forget a comma? What if you forget a square bracket? Is it legal to put each list item on a separate line (i.e., newlines after each comma)?

**7.4.** Can you also create a nested _list of lists_? And a list of lists of lists?

**7.5.** Using the previous list `names`, try to predict what the following do (just as with strings, this is called _slicing_), and test your predictions: 
 - `names[1]` 
 - `names[2]` 
 - `names[8]` 
 - `names[-1]` 
 - `names[-2]` 
 - `names[1:3]` 
 - `names[2:2]` 
 - `names[-2:]` 
 - `names[2:]` 
 - `names[:2]` 
 - `names[0]` 
 - `names[2-4]` 
 - `names[3-2]` 
 - `names[1+1]`

**7.6.** Earlier we used `len` for strings. Does it also work on lists? What about an empty list?

**7.7.** What do you expect will happen if you do `names[len(names)]`? Test your expectation, and try to understand why you were wrong/right.

**7.8.** Recall from slicing with strings that you could specify not only a start and end, but also a step. Does this work with lists? For instance, use slicing to construct a sub-list containing only the elements at even indices (0, 2, 4, ...), or only at odd indices, or to construct the inverse of a list (by slicing it from back to front).

**7.9.** What happens if you pass an entire list as an argument to `print`, i.e., `print(names)`?

**7.10.** Assuming you still have the variable `names`, what does the `in` keyword do? Try at least `'Alf' in names` and `'Alwyn' in names`. How do you test whether _Alwyn_ is _not_ in `names`. Is the `in` keyword (or rather, the notion of 'string identity' on which it relies) case-sensitive?

**7.11.** Remember that various numerical operations could be performed on strings, e.g., `'apple' * 5`, and `'apple' + 'pear'`. Do such oprations also work on lists?

**7.12.** You can change a list element at a given position (index) by assigning a new value using `=`, e.g., `names[3] = 'Nick'`. Afterwards, print the list `names` to see the effect.

**7.13.** In the list `names`, use assign to replace the last element by 'Suzy' and the first element by 'Bob'. Can you also use assignment to _extend_ the list, by assigning a new element to the final index plus 1?

**7.14.** Adding elements at the end of a list can be done, instead, with `append`. This is a method of the list class, hence you call it 'on' a list with a period `.`, like `names.append('Ann')`. Try appending several names to `names`, and finally print the length of the resulting list.

**7.15.** Assign an empty list to a variable, and then `append` a bunch of things to it. Print the result.

**7.16.** Write down your expectation, and then test it: What happens if you append an object to a list that already contains it? And what happens if you define a list in which the same object occurs multiple times from the start?

**7.17.** So far, you first assigned a list to the variable `names`, then changed the list, and then you inspected the original variable `names` to see the result. However, at no point did you _reassign_ an updated list to `names`. Rather, the same list remained assigned to `names`; it is the list itself that was modified. This is possible because lists are _mutable_, unlike integers or strings. In comparison, there is no way to _change_ the integer or string value of a variable, _except_ by reassigning something new to it. To better understand this, reflect on the following code:

```python
int1 = 5
int2 = int1
int1 += 6
print('int1:', int1, '   int2:', int2)

str1 = 'bla'
str2 = str1
str1 *= 2
print('str1:', str1, '   str2:', str2)


list1 = ['a', 'nice', 'list']
list2 = list1
list1.append('really')

print('list1:', list1, '   list2:', list2)
```


**7.18.** One way of modifying a list in-place is by assigning a new value to an existing position in the list, as we saw above (e.g., `names[3] = 'Nick'`). Do you remember whether you can similarly change a string by assigning a character to a position, e.g., `str1[1] = 'z'`? Try it, and compare this to how a list behaves.

- - - - - -
**Something to keep in mind:** Lists are **mutable**: they can be changed in-place (e.g., using `append` or by assigning something to an index in the list). This means that the 'contents' of a variable to which a list is assigned can change, without ever needing to reassign an updated list to that variable. By contrast, strings and ints (and floats, and bools, and tuples) are _immutable_: e.g., the only way to change the value of a variable that refers to a string, is by reassigning a new string to that variable. Understanding mutability will help prevent some hard-to-track mistakes later on!
- - - - -

**7.19.** Based on the foregoing, do you expect strings to have an `append` method just like lists? Why (not)? Try it.

**7.20.** But if strings are really immutable, what is going on below? The value of `x` seems to change! Explain what's going on; is a string mutable after all?

```python
x = 'abc'
print(x)
x = x.upper()
print(x)
```


**7.21.** Given some list `my_list`, do you remember what this slicing notation does: `my_list[:]`? Is the resulting object the same list as the one originally assigned to `my_list`, or does it merely have the same elements? Test this by trying to modify one without modifying the other.

**7.22.** Here is a fun puzzle related to mutability. For the game of tic-tac-toe, we can construct a 3x3 board as follows: `row = [''] * 3`, and then  `board = [row] * 3`. See what the `board` looks like, and optionally write a function to print it in a prettier way. Now let's play the game: I'm the first player, and I place a cross in _one_ of the cells, like this: `board[1][1] = 'x'`. Let's print the board again. Oops, it appears I already won! Easiest game of tic-tac-toe! (What on earth is going on??) How should the `board` have been constructed to prevent this cheat?

**7.23.** Define a function `swap_first_and_last` that takes a list and swaps the first and last elements, modifying the list in-place. Does your program work if the list has only one element? What should it do if the input list has zero elements?

**7.24.** Make your previous function more sophisticated by giving it an additional parameter `in_place`, a boolean that indicates whether the function should modify the list in-place (and return nothing) or make a changed copy instead (and return that). Change the rest of the function accordingly, to handle this parameter. If `in_place` is set to False **[Correction: previously this erroneously said 'True']**, your function should also be able to work on strings.

**7.25.** Assume the days of the week are numbered 0,1,2,3,4,5,6 from Monday to Sunday. Write a function `day_number_to_name` that asks a day number, and returns the day name (a string). Call the function with some values to test it.

**7.26.** Oops! Your client prefers to number the days from 1 (Monday) to 7 (Sunday). Can you modify the above program to fit their use case? How many changes did you need to make?

**7.27.** In the above function, did you use `if` statements? Try to write this program without using `if` statements, by using a list of day names instead. Does this make the program easier to modify if the client changes their mind again?

- - - - - -
**Something to keep in mind:** Whenever you need a mapping from (consecutive) integer numbers to something else, such as strings, use a list, which is precisely such a mapping. For a mapping from things other than integer numbers, we will learn about another data structure later, the _dictionary_.
- - - - -

**7.28.** You go on a wonderful holiday leaving on day number 3 (a Wednesday). You return home after 137 nights. Write a function that asks for the starting day number, and the length of your stay, and it will tell you the name of day of the week you will return on.

**7.29.** Lists and strings are similar in many ways. Try to show with code several ways in which they are alike, and ways in which they are not alike.

**7.30.** Do you expect the following to be true or false: `len([1, 2, 3]) == len('[1, 2, 3]')`. Test your expectation.

**7.31.** In the section on types we saw how to build a string from an int (`str(5)`), an int from a string (`int('24')`), etc., essentially converting between types. Similarly, you can build a list from various types of objects, using `list`. Try 'converting' a string to a list, and understand what you see. Can you also convert a list to a string? Do you expect the following to be true: `str(list('apple')) == 'apple'`? Is it? Why (not)?

**7.32.** What happens if you define your own variable with the name `list` (or `str`, or `int`, for that matter)? Why might doing so be a bad idea?

**7.33.** Write a function with three parameters that, given a list and two integer positions in the list, swaps the two elements in the list. Does your function modify the input list _in-place_, or create a new list?

**7.34.** Write an analogous function (or at least 'as analogous as possible') for swapping two characters in a string.

**7.35.** If applicable, improve your function `is_determiner` from the end of the previous section, which checks whether a given word is an English determiner, by first storing the determiners in a convenient list.

**7.36.** Define a function that generates random, simple sentences of the shape "{determiner} {noun} {verb}s" (e.g., "the student walks"). Use separate lists to store a bunch of lexical items of the required syntactic categories. At the top of your program add `import random`, which lets you use the function `random.choice` to randomly select an item from a list. (We will learn more about `import` as well as `random` later.) Select random items from the appropriate lists and compose a string from them, printing the final result.

**7.37.** Make your random sentence generator as advanced as you like (though try to use only Python constructs that have been introduced in the exercises so far). For instance, can you extend it to randomly choose between an intransitive and a transitive verb frame, and then choose the right type of verb and include a direct object if the verb is transitive?

**7.38.** **New addition** Don't forget the extra homework: to implement the function `is_about_vaccine` in our tweet sentiment adventure. (It may help to first do the initial loop-exercises of the next section, also homework.)

**7.39.** **New addition** Another idea in case you have some time left: try to determine the sentiment of tweets by checking what emoji each tweet contains (instead of using textblob). Since emoji are part of the unicode standard, you can copy-paste emoji from a website like https://unicode.org/emoji/charts-12.0/emoji-ordering.html and store them into a Python string. With the help of such a string, you can try to write a function that (e.g.) counts happy vs. sad/angry emoji and turns this into a sentiment value between -1 and 1.
