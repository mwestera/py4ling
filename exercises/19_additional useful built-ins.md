# Python for linguists


## 19. Additional useful built-ins (`zip`, `enumerate`, `any`, `all`, `sum`)

<br>**_Avoiding indices; combining lists with `zip`_**

**19.1.** In general, Python programmers are a bit weary of using unnecessary indices to access list elements. Streamline the following code by getting rid of `range`, `len` and the index `i`:

```python
names = ['John', 'Sue', 'Bob', 'Chris']
for i in range(len(names)):
    print(names[i])
```


**19.2.** Besides the streamlined version of the above code being simpler, another reason for avoiding indices where possible is the following. If what a piece of code should do is iteration, then that code should work for any object that is iterable, not only those that happen to support indexing. Give a code example to illustrate the superiority of your streamlined version in this regard.

**19.3.** Can you think of another (possibly subjective) reason to avoid indices where possible?

**19.4.** Suppose we have two lists. Write a function to combine every element from one list, with each corresponding element from another, and print the resulting pairs one after the other. Without peeking at the next exercise (resist!), you will probably have to use an index and `range`.

**19.5.** Do you see the resemblance between your preceding function, and a zipper (of the type used in clothes)? That is why an analogous built-in function is called `zip`. Call `help` on this function and find a way to use it to solve the preceding exercise, instead of your custom-made function.

**19.6.** What is the difference between `for a in zip(...):` and `for a, b in zip(...):`?

**19.7.** What do you think will happen if `zip` is provided with two lists of unequal length? Test your expectation.

**19.8.** What type of object does a `zip` call on its own (i.e., outside of a for-loop context) return?

- - - - - -
**Something to keep in mind:** Use `zip` to combine elements, each from a different iterable (e.g., list), into tuples. As with several functions we encountered earlier (e.g., a dictionary's `.keys`, `.values` and `.items`; spaCy's `.sents`), the `zip` function does not return its tuples in a list, but rather returns a type of object that will only generate such tuples 'on the fly' as you iterate over it.
- - - - -

**19.9.** As usual with iterator-type objects, you can also directly collect the generated tuples into a list, with `list(zip(...))`. Try this. What do you expect will happen if you wrap a `zip`-call inside a `dict(...)`? Test your expectation.

**19.10.** Can `zip` also be applied to three or more lists? (Non-serious: can you think of an application for this type of zipper in a piece of clothing?)

**19.11.** Suppose we have a list of place names and a list of their respective inhabitant counts. Write code to create a dictionary from place names to inhabitant counts.

**19.12.** Predict what happens if `zip` is given the same list twice, e.g., `zip(names, names)`? What if it is given the same list twice, but once without the first element: `zip(names, names[1:])`?

**19.13.** Predict the outcomes of the following, given some string `s = 'abcdef'`, and then test your predictions:
 - `list(zip(s, s[:-1]))` 
 - `list(zip(s[1:], s))` 
 - `list(zip(s[:-1], s))` 
 - `list(zip(s, s[::-1]))` 
 - `list(zip(s, s[1:], s[2:]))`

**19.14.** With a single `zip`-command like the foregoing examples, and given the same string `s = 'abcdef'`, construct the following list: `[('a', 'b'), ('c', 'd'), ('e', 'f')]`.

**19.15.** Suppose we have two equal-length lists, `l1` and `l2`. Does `result = list(zip(l1, l2))` achieve the same as the following code? As usual, make a prediction before trying it out.

```python
result = []
for e1 in l1:
    for e2 in l2:
        result.append((l1, l2))
```


<br>**_Counting elements with `enumerate`_**

**19.16.** While Python progammers are weary of indexing (remember the reasons why?), sometimes it's simply necessary. Fortunately, there is often a way to get indices without the pesky `range(len(...))`. The built-in function `enumerate` iterates over elements while counting them, returning the count-element pairs. Assuming you still have a list `names` defined, try the following:

```python
for i, name in enumerate(names):
    print(i, name)
```


**19.17.** What happens if, in the above code, you forget the `i` and do `for name in enumerate(names): ...` instead (if relevant: adapt the `print` statement to avoid it causing a NameError)? And what happens if, conversely, you do include the `i` but forget the `enumerate`, that is, `for i, name in names: ...`?

**19.18.** The count-element pairs you get from `enumerate` may superficially resemble the key-value pairs you get from `dict.items()`, but there are differences too. Explain how the following illustrates one such difference:

```python
for i, char in enumerate({'a', 'b', 'c', 'd', 'e'}):
    print(i, char)
```


- - - - - -
**Something to keep in mind:** Use the built-in function `enumerate` to iterate over elements while counting them, returning count-element pairs. When applied directly to a list, the counts returned by `enumerate` correspond to the list's indices, and this way of accessing indices (_if_ you need indices at all) is often preferable to `range(len(...))`.
- - - - -

**19.19.** Try to predict the outcome of the following (forgive the uninformative variable names), and then test your predictions:

```python
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for x, y in enumerate(my_dict):
    print(x, y)
for x, y in enumerate(my_dict.items()):
    print(x, y)
```


**19.20.** Do you expect any of the following yield an error? Why? Test your expectations. 
 - `list(range(10))` 
 - `list(10)` 
 - `enumerate(10)` 
 - `enumerate(range(10))` 
 - `range(enumerate(10))` 
 - `enumerate(list(range(10))`

**19.21.** Predict, and then test and make sure you understand, the outcomes of the following statements:
 - `list(enumerate('abcd'))` 
 - `list(zip(range(4), 'abcd'))` 
 - `list(enumerate(range(5)))` 
 - `list(zip(range(5), range(10)))`  
 - `list(zip(range(10), range(5)))` 
 - `list(enumerate(enumerate(enumerate(range(5)))))`  
 - `list(zip(range(5)))`

<br>**_Quantifiers (`any`, `all`, `sum`; also `len` revisited)_**

**19.22.** The built-in functions `all` and `any` take an iterable (such as a list) and return a boolean value, representing if all/any of the iterable's elements evaluate to `True`. What do you think the following expressions evaluate to? Test your predictions.
 - `all([True, True, True])` 
 - `any([True, True, True])` 
 - `all([True, False, True])` 
 - `any([True, False, True])` 
 - `all([False, False, False])` 
 - `any([False, False, False])` 
 - `any([])` 
 - `all([])`

**19.23.** Assuming `booleans = [True, False, True]`, predict what the following equivalences evaluate to, then test your predictions:  
 - `not any(booleans) == all(not b for b in booleans)` 
 - `any(booleans) == (not all(not b for b in booleans))`

**19.24.** Assuming we have a list of strings assigned to `words`, what does `any(len(word) >= 3 for word in words)` check for? Write a similar one-liner that checks whether _all_ words are less than 10 characters long, and another that checks where _any_ words starts with a vowel.

**19.25.** Write three more one-liners, that check (respectively) whether none, some, and all of the words contain the letter 't'.

**19.26.** Another built-in function is `sum`, which does what you would expect: it takes an iterable and returns the sum of all elements. Use this to compute the sum of a list of numbers, in a single line. Does `sum` also work on a list of strings (after all, `'abc' + 'def'` is fine, too)? Does it work on a list of booleans?

**19.27.** Explore and explain how one could use `sum` to, basically, _count_ the number of `True` booleans in a list. Use this to write an expression that counts the number of words that have a length of at least 3, and another expression that tests whether there are at least 3 words that end with a vowel.

**19.28.** An alternative way to count how many elements meet a certain condition uses `len`: first use list comprehension with `if` to keep only the elements that meet the condition (we learned about such 'filtering' before), and then apply `len` to the result. Use this to provide alternative solutions to the previous exercise. Which solution do you find more readable?

**19.29.** Describe, at an intuitive level, the two approaches we just explored for counting how many elements meet a certain condition (i.e., using `sum` vs. using `len`). How does each work?

**19.30.** A technical detail: You may have found out 'the hard way', that whereas `sum`, `any` and `all` can take any iterable, including a 'generator' object that produces elements on the fly (as produced by comprehension syntax _without_ the brackets around it), `len` requires an object that has a length, such as a list or set (so the brackets are needed). Create an example to show this if you haven't already, and try to find this difference in the documentation.

**19.31.** Assuming we have a list of strings assigned to `words`, try to describe in plain English what the following lines compute. First make a prediction, then test and verify your understanding. (You can of course change `words` to include a variety of relevant strings!) Are there expressions among the following that are equivalent? 
 - `any(w[0].lower() in 'aeiou' for w in words)` 
 - `all(w[0].lower() in 'aeiou' for w in words)` 
 - `not any(w[0].lower() in 'aeiou' for w in words)` 
 - `all(w[0].lower() not in 'aeiou' for w in words)` 
 - `sum(w[0].lower() in 'aeiou' for w in words) >= 2` 
 - `len([w for w in words if w[0].lower() in 'aeiou']) >= 2` 
 - `not any(w[0].lower() not in 'aeiou' for w in words)` 

 Of course, the more involved the comprehension syntax and the boolean check, the less readable these one-liners become -- but in general, knowing these techniques can greatly improve the readability of your code.

**19.32.** With the help of the built-ins and techniques from this section, reimplement some functions from section 14 (there, recall, used to practice `break` and `continue`), in particular `has_any_odd`, `has_only_odd`, `has_three_odd` and `has_at_most_n_vowels`. (Sorry for the 'dry' exercises in this section!)

