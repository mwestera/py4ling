# Python for linguists


## 13. Dictionaries advanced

**13.1.** Can you loop over a dictionary with `for` by using the same syntax as looping over a list? Try to loop over the dictionary `name_to_id` from above, printing each element. Which elements get printed, the keys, the values, or both?

**13.2.** There are three other ways of looping over a dictionary: you can loop over elements in `name_to_id.keys()` (e.g., `for key in name_to_id.keys()`), over elements in `name_to_id.values()` and over elements in `name_to_id.items()`. Try the three versions, in each case simply printing the elements in the loop, and see what gets printed.

**13.3.** If you loop with `for item in name_to_id.items():`, note that what gets printed (each `item`) are _pairs_ of a key and a value (try printing `type(item)`). A pair (or more generally _tuple_) can be _unpacked_ by assigning it to two variables separated by a comma, like this: `for key, value in name_to_id.items():`. (Recall that we saw tuple unpacking before, in the Pythonic way of switching two variables, `x, y = y, x`.) Use this to define a function `print_dict` that takes a dictionary, and loops over its items to print keys and their associated values separated by a colon: `key: value`.

**13.4.** Define a function `update_dict` that takes two dictionaries, and adds all items of the second to the first (modifying the first dictionary in-place). To test this function, construct another dictionary `name_to_id2` with a bunch of fictional names and IDs different from those in the original `name_to_id`.

**13.5.** In fact, the function you just defined should achieve the same as the built-in dictionary method `update`, i.e., `name_to_id.update(name_to_id2)`. Test this, after first resetting `name_to_id` to what it was before. (The existence of built-in `update` doesn't make the previous exercise pointless; it has given you experience with looping over dictionaries, and, having implemented an `update` function yourself, it will be easier to remember what the built-in `update` does.)

**13.6.** What are differences (in functionality) between the `update` method and assigning a value to a key using direct assignment (`=`)? What happens if you confuse the two, e.g., `name_to_id.update('Bobby') = 5`, or `name_to_id.update(Bobby=5)`, or `name_to_id.update('Bobby': 5)`?

**13.7.** Do the dictionary methods `keys`, `values` and `items` return an ordinary list (since we could loop over it), or a different type of object? Do these types of objects support indexing and slicing like a list? If not, it might occasionally be convenient to convert them to a list with `list(...)`. Try this, and see if the resulting list does support indexing and slicing (as one would expect).

**13.8.** What sort of object do you get if you convert the whole dictionary to a list (without going through the `keys`, `values` or `items` methods), like `list(name_to_id)`? Can you reconcile this with the things we looped over when doing `for x in name_to_id:`?

**13.9.** What determines the order in which the keys are iterated over? Form a hypothesis by defining several dictionaries (and also adding some new items to them later) and iterating over their keys, printing them (you can use your own `print_dict` from before).

- - - - - -
**Something to keep in mind:** Until Python 3.6, the **order** of items in a dictionary could depend on the particular implementation of Python, and was _not_ to be relied upon in Python code. Since Python 3.7, however, dictionary order has been promoted from an implementational side-effect to a core feature of dictionaries: when iterating over a dictionary, the elements are now guaranteed to be given in the order in which they were added to the dictionary (whether in the initial dictionary definition (from left to right) or through subsequent assignment).
- - - - -

**13.10.** Write code that relies on dictionary order (in Python 3.7 or higher) to get the value whose key was first added to the dictionary, and code to get the value whose key was last added to the dictionary.

**13.11.** Write code that gets whatever value belongs to the maximum key in a dictionary. You can either do this with the help of built-in `max`, or without it, for extra looping practice.

<br>**_A bit about tuples_**

**13.12.** Iterating over `name_to_id.items()` yields tuples. What are some other contexts in which you encountered tuples so far?

**13.13.** The standard way to define your own tuple is as a series of comma-separated expressions in parentheses e.g., `my_tuple = (1, 3, 5)`. Experiment with tuples: What types of values can they contain? Can you access their elements by index? What about slicing a range of indices? Are tuples mutable? What happens if you omit the parentheses from your tuple declaration? Can you create an empty tuple? Can you convert a tuple to a list? To a string? Vice versa (like `tuple('abc')` perhaps?)? Does a tuple have a length? Can you concatenate two tuples into a new one using `+`? Can an element of a tuple be itself a tuple? Can tuples be compared with operators like `<` and `>`?

**13.14.** Comma-separated values are commonly used also to let a function return multiple values at once (e.g., `return x, y`), and for _unpacking_ a tuple (as in `for key, value in name_to_id.items()`), and for the Pythonic way of swapping values (e.g., `x, y = y, x`). Do all of these uses also permit surrounding the comma-separated expression lists with parentheses?

- - - - - -
**Something to keep in mind:** Comma-separated expressions in Python form _expression lists_, and an expression list containing at least one comma (and commonly, but _not_ necessarily, surrounded by parentheses) yields a **tuple** (except when part of defining e.g. a list like `[1, 2, 3]`). Note that it is _not_ the parentheses that signal to Python that you are defining a tuple, but rather the comma (_except_ when defining an empty tuple, which is done with `()`).
- - - - -

**13.15.** Suppose we accidentally end our line with a comma, like `a = 1,`. Invent a possible context where this typo could lead to a subsequent error.

**13.16.** Although when creating tuples the parentheses are sometimes optional, sloppiness can lead to potentially unexpected results. Explain the difference between `(1, 2, 3) + (4, 5)` and `1, 2, 3 + 4, 5`.

**13.17.** Explain the truth value of `True, True, True == (True, True, True)`

**13.18.** Tuples are ideal for storing a (small) number of fixed values with a fixed order, such as a name with a student ID and email address, or the coordinates of a point in 3D-space `(x, y, z)`. If you need to store more data fields (e.g., email address, average grade, place of birth...) then a dictionary usually becomes more convenient than a tuple, and if you need to store an in principle unbounded number of (typically more homogeneous) elements, a list is preferable. Can you identify reasons for these preferences? Reflect on the varying use-cases of these three data structures.

**13.19a.** **[Recent addition.]** Recall the relation between dictionaries and **hashability**. There is a relation between hashability and mutability: objects that are intended to be mutated, like lists (and also dictionaries themselves), are typically not hashable (try this). This is because the hash code of a container object is computed based on the hash codes of the objects it contains, such that changing the objects it contains (as mutability allows) would cause the hash code of the container object to change, and the latter would cease to be a suitable, fixed 'anchor' for storing and retrieving objects in a dictionary. Test whether tuples are hashable (e.g., can they be used as keys in a dictionary?). Based on this, do you expect tuples to be mutable? Test this, too.

**13.19b.** Is the following statement true? 'The fact the items of a dictionary are tuples, shows that tuples are hashable.'

**13.20.** Tuples are immutable, lists are mutable, but tuples can contain lists... Can a tuple that contains a list as one of its elements, be used as a dictionary key?

**13.21.** Recall that **list comprehension** syntax can be used for concisely constructing a list (e.g., from an existing list, a range, or more generally a 'generator expression'), like `[i**2 for i in range(10)]`. To construct a tuple in this way, instead of a list, merely surrounding it with round parentheses instead of square brackets doesn't work: `(i**2 for i in range(10))`. Does this match what you learned about defining tuples in Python? Instead, you need to explicitly construct a tuple using `tuple(i**2 for i in range(10))` (note that the same also works with lists: `list(i**2 for i in range(10))`). Try this.

<br>**_List comprehension for dictionaries_**

**13.22.** List comprehension-type syntax, or more generally 'comprehension', also works with dictionaries. More correctly, `... for X in Y` is a so-called **generator expression**, and the items it 'generates' can be collected not only in a list (`[... for X in Y]`), but also in a dictionary (among other datastructures), as long as `...` has the right format, namely key-value pairs in case of a dictionary. Given this, what do you think the following does?

```python
new_dict = {key: value for key, value in name_to_id.items() if key[0].lower() in 'aeiou'}
```


**13.23.** Use comprehension to take an existing dictionary with strings as keys (e.g., `name_to_id`), and filter it, constructing a new dictionary that contains only those items whose key has an even length.

**13.24.** Explain in ordinary English what the following comprehensions do: 
 - `{name: len(name) for name in name_to_id}` 
 - `{i: i**2 for i in range(10)}` 
 - `{name: name[::-1] for name in name_to_id.keys()}` 
 - `{key: value for key, value in name_to_id.items() if int(value) % 2 == 0}`

**13.25.** Use comprehension to take an existing dictionary and invert it, swapping the keys with the values.

**13.26.** Suppose we have a predefined list of English numerals `numerals = ['zero', 'one', 'two', 'three', 'four', 'five']` (or more). Use comprehension and `range` to create a dictionary from English numerals to numbers (0, 1, 2, 3, ...), and another one for the reverse mapping.

**13.27.** In section 11 you created the file `text_utils.py`, containing functions `ngrams` and `tokenize`. This means that in your current working file (make sure it is placed in the same directory) you can do `import text_utils`. Do this and apply the `text_utils.tokenize` and `text_utils.ngrams` functions to a short text. For instance, copy a text from Wikipedia, a blog, or an e-book, and simply paste it into your program in between triple quotation marks `'''` (to allow newlines within the copied string), the entire string assigned to a variable `text`. (Mixing code and data in a single file is bad practice of course, but fine for now. We learn about reading text from a separate file later.)

**13.28.** (Without peeking in the Week 6 adventure code:) Write a function `count_tokens` that takes a list of strings and returns a dictionary that maps each string to how often it occurs in the list. You can use comprehension to initialize a counts dictionary (mapping each string to 0), and then loop through the tokens list while updating the counts.

**13.29.** Does your function `count_tokens` also work if you feed it a list of n-grams instead of a list of single tokens? If not, find a way to fix this (in your current working file or by changing the `text_utils.ngrams` function itself). You should then be able to print individual token counts, bigram counts and trigram counts.

**13.30.** Conversion to a dictionary can be done with `dict`. Which types of objects can be converted to a dictionary? Can you convert an ordinary list to a dictionary? A string? (In each case, try to form an expectation before testing it.) What about a list of pairs (2-tuples)? What about a list of lists, where each inner list has two elements? What if one of the inner lists has only one element, or three? What about a list of two-character strings?

**13.31.** Given that looping over a dictionary loops over the keys, what do you expect conversion to a list to do? Does converting a list to a dictionary and back to a list bring you back to where you started (e.g., `list(dict(some_list_of_pairs))`)?

<br>**_Mini-adventure: Translation_**

**13.32.** Create a dictionary `en_to_nl` that maps some English words to Dutch words. (You can also use another language pair of choice for these exercises.)

**13.33.** Write a function `invert_dict` that takes a dictionary and returns a new, inverse dictionary, mapping the original values back to the original keys. Use this to construct a dictionary `nl_to_en` from the original `en_to_nl` you defined in the previous exercsie. Can you now use the two dictionaries to translate back and forth, e.g., assuming your original dictionary contained the word _tree_, what is the outcome of `nl_to_en[en_to_nl[nl_to_en[en_to_nl['tree']]]]`.

**13.34.** To `en_to_nl`, add the English word _feather_ mapping to Dutch _veer_, as well as the English word _spring_, which also happens to translate into Dutch _veer_. Feed it into your function `invert_dict`. What is the problem, technically and conceptually? Illustrate this in code by inverting your dictionary `en_to_nl` once, and then inverting the result again, comparing the outcome to the original. (You can use your function `print_dict` from above to print the dictionaries in a more readable way.)

**13.35.** In general, a single word can have multiple adequate translations, for instance if the word is ambiguous or if the target language has multiple synonyms. To account for this, define a different type of dictionary, `en_to_nl_multi` that maps each English word to a _list_ of Dutch words, e.g., `{'bat': ['vleermuis', 'knuppel'], 'tree': ['boom'], ...}`. Your previous function `invert_dict` does not work on this type of mapping (explain what the problem is), so write a new function `invert_dict_multi` that does work. Note that just switching keys and values won't be adequate; the inverted dictionary `nl_to_en_multi` should again be a mapping from strings to lists, just like the original. Your new inversion function should handle the _bat_ (_vleermuis_/_knuppel_) example correctly, and also solve the _feather_/_spring_ (_veer_) problem from the previous exercise.

**13.36.** Write a function that takes a text and a dictionary as parameters, and returns a word-by-word translation of the text. You can of course use `text_utils.tokenize` to get the individual words for translation. If multiple translations for a given word are possible, choose a random one (using `import random` and then `random.choice(...)`). Add enough words to your dictionary to enable the translation of some simple sentences. For instance, feeding your translation function the sentence _The feather was very light_ (together with the `en_to_nl` dictionary) should result in _De veer was heel licht_.

**13.37.** What if your text contains a word that is not in the dictionary? Give your translation function a third parameter `mask_unknown` that is a boolean with a default value True. If it is set to True, unknown words should appear as `<UNKOWN>` in the resulting string. If it is set to False, unknown words should simply be left untranslated (e.g., resulting in a mostly-Dutch sentence with some untranslated English words). You can of course use `in` to check if a word is included in the dictionary or not, but doing so will often lead to two dictionary lookups where one should suffice (consider why). The `get` method of dictionary objects is better here; enter `help({}.get)` in the Python console to see how you can use it.

**13.38.** Naturally, a shortcoming of word-by-word translation is that any word order differences between languages are not accounted for. Illustrate this with a sentence of choice. Without programming, can you think of a reason why (or a way in which) n-grams could be used to improve the accuracy of automatic translation?

