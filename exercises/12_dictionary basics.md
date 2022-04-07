# Python for linguists


## 12. Dictionary basics

**12.1.** Run the code below to construct `name_to_id`, a mapping or _dictionary_ from fictional student names (the keys) to student IDs (the values). Then inspect the object you created by printing `name_to_id`, as well as `type(name_to_id)`.

```python
name_to_id = {'Alf': '136124', 'Beth': '008623', 'Chris': '014212', 'Dave': '9123785', 'Esra': '978123'}
```


**12.2.** You can look up a particular value in the dictionary by providing it with a key in square brackets (like list index notation). Look up the student IDs (values) of Alf and Chris (keys), and print them.

**12.3.** What happens if you try to look up the student ID (value) of a student whose name is not a key in the dictionary? What happens if you forget the quotation marks around the key string you're looking up?

**12.4.** Does a dictionary have a length, just like lists and strings? Can you create an empty dictionary?

**12.5.** Can you use the keyword `in`, just as with lists, to check if an element is contained in a dictionary? If so, does `in` look at the keys or the values, or both?

**12.6.** Does a dictionary support integer indexing just like lists and strings, e.g., can you select the third item (index 2) in the above dictionary by doing `name_to_id[2]`?

**12.7.** What if we have a dictionary with integers as keys instead of strings, like `{1: 'hi', 2: 'hello', 3: 'bye', 4: 'tata'}`? Can we now access an element by its index (or is this a misleading way to put it)?

- - - - - -
**Something to keep in mind:** A **dictionary** is Python's main datastructure for storing a mapping, from _keys_ to _values_. Both keys and values in a dictionary can be various types of objects, e.g., integers, floats, strings, functions, and more complex objects. However, not every type of object can be used as a dictionary key; keys must have a special property of being **hashable**, which is, roughly, that the object provides a `hash` method that generates a string code that (virtually) uniquely represents the object. It is by these hash strings that the items in a dictionary are stored and retrieved.
- - - - -

**12.8.** What happens if you define a dictionary by specifying key-value pairs (like `{'Alf': '36124', 'Beth': '008623'}`) but using equals signs `=` instead of the colons `:` to connect keys and values? Do you see why this is quite an easy-to-make syntax mistake?

**12.9.** Try to construct an integer-to-integer dictionary, say, from numbers representing an age (in years) to the number of (hypothetical) students that have that age. Construct a string-to-integer dictionary that could be a (small) example of a mapping from words to their counts in some (hypothetical) corpus. Construct a string-to-list dictionary that maps the name of a hypothetical course (say, `'semantics'`, `'syntax'`, `'python'`) to a list of students taking that course. Lastly, what happens if you try to construct a list-to-integer dictionary that, say, maps a list of numbers to its average? Why?

**12.10.** Can a single dictionary mix multiple types (e.g., integers, floats, strings) as values, and/or multiple types as keys?

**12.11.** Do you expect dictionaries to support slicing like lists and strings do, to select a range of elements, e.g., `name_to_id['Alf':'Dave']`? Test your expectation. What about dictionaries that have integers as keys, do they support slicing to get a range of elements? Why might this be?

**12.12.** Do you expect the keys in a dictionary to be case-sensitive? Test this.

**12.13.** Similar to assigning a value to a particular index in the list (e.g., `names[3] = 'Bert'`), you can assign a value to a particular key in the dictionary (e.g., `name_to_id['Suzy'] = '124987'`). What happens if the key to which you assign a value already exists in the dictionary? What happens if it does not yet exist in the dictionary? Relatedly, what happens if there are duplicate keys already at the moment you create a dictionary, e.g., `my_dict = {'a': 1, 'b': 2, 'a': 3}`?

**12.14.** What do you think `del name_to_id['Esra']` does? Try it! In fact, does this syntax also work on lists? Construct a list (like `names` from previous sections) and try to delete the item at one of its integer indices. Do you expect it to work on a string as well, i.e., to delete a character from the index in a string? Why (not)?

**12.15.** Oops, the `name_to_id` dictionary contains the wrong ID for Chris! It should be `'5987162'`. Also, Suzy has quit the course, so let's remove her entry from the dictionary altogether.

**12.16.** Interestingly, dictionaries are also used under the hood for storing the ordinary variables you create -- remember the `globals()` and `locals()` dictionaries from the previous section? What does the following code show?

```python
x = 5
print(x)

globals()['y'] = 10
print(y)
```


**12.17.** In the above example, PyCharm will likely warn you, with a red squiggle on the last line, that the variable `y` has not been defined. But Python itself doesn't care; the code runs fine! This means that PyCharm's warnings are based on a more shallow parsing of the code (called **linting**), not on actually interpreting it fully like Python does. Why might that be?

<br>**_Mini-adventure: Language generation with feature structures_**

**12.18.** Briefly review your random sentence generation code from Section 7. In the current section we will explore a different approach, relying heavily on dictionaries.

**12.19.** Dictionaries are useful for representing so-called **feature structures**, i.e., bundles of features with values. This lets us represent a vocabulary as a list of dictionaries, as illustrated below. Extend this vocabulary by adding different words:

```python
vocabulary = [
    {'word': 'walk', 'category': 'verb', 'frame': 'intransitive'},
    {'word': 'see', 'category': 'verb', 'frame': 'transitive'},
    {'word': 'student', 'category': 'noun'},
    {'word': 'the', 'category': 'det'},
]
```


**12.20.** As a warming up, use list comprehension to construct a new list from this vocabulary containing only all verb entries, and another one containing only nouns.

**12.21.** As another warming up, use `import random` and then `random.choice(...)` to select a random determiner from the vocabulary, a random noun, and a random intransitive verb, and concatenate their word forms with spaces into a simple sentence.

**12.22.** Now create a more general function that randomly generates a sentence based on the above vocabulary. It should output a single string composed of word forms (so not showing all the other features). Try to do so by defining and calling auxiliary functions corresponding roughly to natural language constituents, e.g., a `vp` function that generates a random verb phrase, a `dp` function that generates a random determiner phrase (like 'the student'), and so on. Your `vp` function should be sensitive to the `frame` feature in the vocabulary entries of verbs, and include an object `dp` where necessary. You can also make your `dp` function refer to an `np` function that generates noun phrases with an optional adjective (like 'smart student').

**12.23.** For testing, implement a simple loop that prints out, say, 20 random sentences generated by your grammar.

**12.24.** Add thematic role information as a feature to your verb entries (e.g., `'subject': 'agent'`), and relevant semantic information to your noun entries (e.g., `'animate': True`). If you let the `vp` function return not just a string but also the subject's required thematic role, you can feed this role as an argument to the `dp` function to generate a subject with appropriate semantic features (e.g., if an 'agent' is required, it should check the 'animate' feature of the noun).

**12.25.** There is in principle no limit to the amount of (word-level) information you can store in feature structures! As a final exercise, let us add phonetic information to each vocabulary entry, e.g., for walk add a feature `'phon': '/wɔːk/'`. For our small example vocabulary you can manually copy phonetic transcriptions for instance from Wiktionary (https://en.wiktionary.org/); for a larger vocabulary you would of course write a Python script do to this extraction automatically. Next, add a boolean parameter `phon` to your sentence generator, with default value `False`, that lets you choose whether to return a sentence in orthographic or phonetic format.

**12.26.** Write down some possible directions in which one could take this mini-adventure, whether as a research project, a practical application or a fun hobby.

