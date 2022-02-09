# Python for linguists


## 6. Lists (`list`, `append`, `[]`)

**6.1.** Assign a variable `names = ['Alf', 'Beth', 'Chris', 'Dave', 'Esra']`. What does `type(names)` say?

**6.2.** Use square brackets `[` and `]` to create a list of numbers, a list of strings, and a list of both numbers and strings. Do these lists all have the same `type`? What about an empty list?

**6.3.** What happens if you try to create a list but forget a comma? What if you forget a square bracket?

**6.4.** Using the previous variable `names`, try to predict what the following do (just as with strings, this is called _slicing_), and test your predictions: 
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
 - `names[1+1]`?

**6.5.** Earlier we used `len` for strings. Does it also work on lists? What about an empty list?

**6.6.** Recall from slicing with strings that you could specify not only a start and end, but also a step. Does this work with lists?

**6.7.** Form your expectation, and then test it: What happens if you define a list where the same object occurs multiple times? What happens if you append an object to a list that already contains it?

**6.8.** What happens if you pass an entire list as an argument to `print`?

**6.9.** Assuming you still have the variable `names`, what does the `in` keyword do? Try at least `'Alf' in names` and `'Alwyn' in names`. How do you test whether _Alwyn_ is _not_ in `names`.

**6.10.** Remember that various numerical operations could be performed on strings, e.g., `'apple' * 5`, and `'apple' + 'pear'`. Which of these also work on lists?

**6.11.** What do you expect will happen if you do `names[len(names)]`? Test your expectation, and try to understand why you were wrong/right.

**6.12.** You can change a list element at a given position (index) by assigning a new value using `=`, e.g., `names[3] = 'Nick'`. Print the resulting list.

**6.13.** In the list `names`, use assign to replace the last element by 'Suzy' and the first element by 'Bob'. Can you also use assignment to _extend_ the list, by assigning a new element to the final index plus 1?

**6.14.** Adding elements at the end of a list can be done, instead, with `append`, which is a method of the list class, hence you call it like `names.append('Ann')`. Try appending several names to `names`, and finally print the length of the resulting list.

**6.15.** Assign an empty list to a variable, and then `append` a bunch of things to it. Print the result.

**6.16.** So far, you first assigned a list to the variable `names`, then changed the list, and then you inspected the original variable `names` to see the result. However, at no point did you _reassign_ an updated list to `names`. Rather, the same list remained assigned to `names`; it is the list itself that was modified. This is possible because lists are _mutable_, unlike integers or strings. In comparison, there is no way to _change_ the integer or string value of a variable, _except_ by reassigning something new to it. To better understand this, reflect on the following code:

```python
int1 = 5
int2 = int1
int1 += 6
print('int1:', int1, '   int2:', int2)

str1 = 'bla'
str2 = str2
str1 *= 2
print('str1:', str1, '   str2:', str2)


list1 = ['a', 'nice', 'list']
list2 = list1
list1.append('really')

print('list1:', list1, '   list2:', list2)
```


**6.17.** One way of modifying a list in-place is by assigning a new value to an existing position in the list, as we saw above (e.g., `names[3] = 'Nick'`). Do you remember whether you can similarly change a string by assigning a character to a position, e.g., `str1[1] = 'z'`? Try it, and compare this to how a list behaves.

- - - - - -
**Something to keep in mind:** Lists are **mutable**: they can be changed in-place (e.g., using `append` or by assigning something to an index in the list). This means that the 'contents' of a variable to which a list is assigned can change, without ever needing to reassign an updated list to that variable. By contrast, strings and ints (and floats, and bools, and tuples) are _immutable_: e.g., the only way to change the value of a variable that refers to a string, is by reassigning a new string to that variable. Understanding mutability will prevent some hard-to-track mistakes later on!
- - - - -

**6.18.** Based on the foregoing, do you expect strings to have an `append` method? Why (not)? Try it.

**6.19.** But if strings are really immutable, what about this: First run `x = 'abc'` and `print(x)`, and then `x = x.upper()` and `print(x)` again. `x` seems to have changed! Explain what's going on; is a string mutable after all? (Beware: it's easy here to settle on an intuitive, but wrong answer.)

**6.20.** Can you also create a _list of lists_? And a list of lists of lists? What happens if you mismatch the required open and closing brackets? What happens if you forget a comma?

**6.21.** Given a list, write a Python program to swap first and last element of the list. Does your program work if the list has only one element? What should it do if the input list has zero elements?

**6.22.** Assume the days of the week are numbered 0,1,2,3,4,5,6 from Monday to Sunday. Write a program that asks a day number, and prints the day name (a string).

**6.23.** Oops! Your client prefers to number the days from 1 (Monday) to 7 (Sunday). Can you modify the above program to fit their use case? How many changes did you need to make?

**6.24.** In the above program, did you use `if` statements? Try to write this program without using `if` statements, by using a list of day names instead. Does this make the program easier to modify if the client changes their mind again?

- - - - - -
**Something to keep in mind:** Whenever you need a mapping from (consecutive) integer numbers to something else, such as strings, use a list, which is precisely such a mapping. For a mapping from things other than integer numbers, we will learn about another data structure later, the _dictionary_.
- - - - -

**6.25.** You go on a wonderful holiday leaving on day number 3 (a Wednesday). You return home after 137 sleeps. Write a general version of the program which asks for the starting day number, and the length of your stay, and it will tell you the name of day of the week you will return on.

**6.26.** Lists and strings are similar in many ways. Try to show with code three ways in which they are alike, and three in which they are not alike (think _mutability_).

**6.27.** Do you expect the following to be true or false: `len([1, 2, 3]) == len('[1, 2, 3]')`. Test your expectation.

**6.28.** Similar to converting from e.g. `int` to `str`, you can convert various types of objects to a list, using `list`. Try converting a string to a list, and understand what you see. Can you also a list to a string? Do you expect the following to be true? Is it? `str(list('apple')) == 'apple'`

**6.29.** Recap: how do you select the first element of a list? How do you select the `n`th element of a list? What happens if `n` is larger than the list's length? How do you select the last element of a list? How do you select the pre-last element of a list?

