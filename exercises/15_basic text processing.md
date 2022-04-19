# Python for linguists


## 15. Basic text processing (`split`/`strip`, reading/writing files)

<br>**_Some convenient string-cleaning operations_**

**15.1.** Python provides many useful string operations, including some which you manually implemented in prior exercises. Look at `dir(str)`, or equivalently `dir('some_random_string')`, for a list of methods available on the string class itself. Explore at least the string methods `strip`, `swapcase`, `isalnum` and `center`; use `help` if needed (e.g., `help(str.strip)`) and illustrate how they work with your own examples.

**15.2.** What is the difference between the string methods `split` and `rsplit`? Illustrate with your own example.

**15.3.** Assume that we have assigned `test_string = 'abcblablablaabc'`. For each of the following invocations of `strip`, form an expectation about what it does (based on the `help` you obtained) and then test it (e.g., by printing the result), refining your understanding of `strip`:
 - `test_string.strip('abc')` 
 - `test_string.strip('cba')` 
 - `test_string.strip('a').strip('b').strip('c')` 
 - `test_string.strip('c').strip('b').strip('a')` 
 - `test_string.strip('bla')`

**15.4.** Call `help` on the `str.join` method, look at the example it provides, and try to apply it to join your own list of strings with a dash `-` in between. Pay attention: on which object is the `join` method called, on the joiner or on the joinees?

**15.5.** Define a string `s` for which the following is _not_ true: `' '.join(s.split())`.

**15.6.** There may be something counterintuitive about `join` and `split`: why is `split` called as a method of the string-to-be-split (with the string that joined them, `'-'`, as an argument), while `join` is _not_ called on the strings to be joined, but rather, on the string used for joining them. For instance, in the above code, `'-'` is the argument of `split`, but not of `join` (for which it is the object providing the method). The following variant would be more 'symmetrical' in this regard, as the connecting character `'-'` would be the argument in both cases. However, test this to see what type of error you get (and then fix it):

```python
names = ['john', 'sue', 'bob']
names_joined = names.join('-')	# Doesn't work!
names_unjoined_again = names_joined.split('-')
print(names == names_unjoined_again)
```


- - - - - -
**Something to keep in mind:** Two very useful built-in string operations are `split` and `join`. Memorize that `split` is called as a method _on the string to be splitted_ (so _not_ on the string to split by); while `join` is called as a method _on the string to join by_ (so _not_ on the list of strings to be joined). The reason is simple (though ultimately a mere design decision that could have been made otherwise): for `join` to be a string method, it must be called on a string object -- and the object witwh things-to-be-joined is not a string, but a list (or dictionary, set, and any other kind of collection or iterable...). To help you remember, always read `x.join(y)` as "with _x_ join _y_", and read `x.split(y)` as "split _x_ on _y_".
- - - - -

**15.7.** Oh no! I copied a list of student names from a low-quality PDF and now all names are surrounded by weird symbols! See below -- imagine the list is much longer (so manual cleaning is not an option) but the type of 'noise' remains the same. Define a function that uses `split` and `strip` to return a list of separated, cleaned-up names:

```python
names = '''#*John#*
#*Mary# *,
*#*Suzy#*,
#*Bob#\t*;
#* Chris#\t*'''
```


**15.8.** Oops, copying from a different PDF resulted in even more mess, where all names are in uppercase and some characters were misread as similarly-shaped numbers. Can you clean it up similarly? Hint: there is a string method called `replace`.

```python
names = '''#*T0DD#*
#*0NA# *,
*#*SUE#*,
#*ANN-M4RY#\t*;
#* R0S5#\t*'''
```


**15.9.** How does the string method `replace` work? What if the thing-to-be-replaced isn't there? How can you use `replace` in order to _delete_ all occurrences of a certain substring? What do you expect the result of `'abc'.replace('', ' ')` to be (form an expectation first, then test it)?

**15.10.** How does the string method `find` work? Call `help` on it if needed, and try it on some examples. What happens if the thing-to-be-found isn't there? (The latter behavior of `find` is known to be error-prone; can you think of why that is?) How does `find` differ from the method `index` that we saw before? Is `find`, just like `index`, available for strings and lists alike?

**15.11.** Define a simple word-tokenizer that uses `split` on spaces and `strip` to get rid of punctuation, and compare it to your earlier attempt at word-tokenization (e.g., the one you put in `text_utils.py` as part of Section 11), noting some (possibly shared) shortcomings.

<br>**_Reading and writing files_**

**15.12.** Without searching the web, try to gather and formulate your intuitions: What is file? What is the difference between, and relation between, long-term storage (e.g., your harddisk, or the cloud) and working memory (RAM)? What is a folder (or directory)? What is a path (such as, depending on your operating system, `C:\Documents\semantics_report.pdf` or `~\Downloads\Alice_in_wonderland.txt`)? What might be the difference between an _absolute_ and a _relative_ path?

- - - - - -
**Something to keep in mind:** WARNING: Before executing any code that involves opening a file, _always_ assume the worst: that the referenced file, if it exists, will be destroyed/overwritten. Make sure you do not loose valuable data in case this happens. Some things we will learn -- using a context manager, opening a file as 'read-only' where possible, using relative paths -- and in general clean code help decrease the chance of unintended changes to your files.
- - - - -

**15.13.** Create a Python script with the following code. Execute it, then find the created file `test123.txt` on your computer and open it (it will be in the same folder as your Python script). 

```python
with open('test123.txt', 'w') as file:
    file.write('Hello!')
```


**15.14.** Experiment with the above code. What if, inside the `with`-block, you add a second write statement? What will be in the file if you repeat the entire `with`-block twice? Does a `with`-block create a local scope? Does this align with what happens if you try to write a bit more to the file _after_ (i.e., outside, non-indented) the `with`-block?

**15.15.** What if you omit the second argument of `open`, the string `'w'`? What if you replace it by an `'a'` and run the code several times? In each case inspect the resulting file. The second argument of the `open`-call specifies the **mode**. The most common modes are read-only (`r`, which is the default), write-only (`w`), read-and-write (`r+`) and append (`a`). Call `help(open)` and find the table explaining the different modes. Based on the previous exercise, what is meant by 'trancating' in the explanation given for `w`?

**15.16.** Assuming the file `test123.txt` now exists, execute the following code to read it. Does `file.read()` read one line at a time, or the full file contents (create a multi-line file if you want to test this)?

```python
with open('test123.txt', 'r') as file:
    text = file.read()
print(text)
```


**15.17.** What happens if you try to read the same file twice in a row, _within_ a single `with`-block (and print the results of both reads)? What if you read the same file twice but in _separate_ `with`-blocks? First hypothesize about what may cause this difference, and only subsequently try to reconcile it with the following: When you open a file, a persistent pointer is created that to the 'current position' in the file, i.e., the index of the byte of the file that is to be read next. In read-only mode `r`, this pointer starts at 0 (start of the file) and is incremented while the file is being read. What will be the value of this pointer after reading an entire file?

**15.18.** What do you think the starting value of the pointer of a file will be when you use append mode `a`? And what if you use write mode `w`? You can verify your predictions with code like the following (also try mode `w`), where the `tell` method reveals the value of the pointer.

```python
with open('test123.txt', 'a') as file:
    print('Pointer when appending:', file.tell())
```


- - - - - -
**Something to keep in mind:** If you want to read from or write to a file in Python, you first need to **open** the file. The standard idiom uses the built-in function `open`, which takes a path and a _mode_ (read-only `r`, write-only `w`, read-and-write `r+`, append `a`), embedded in between the keywords `with ... as` for constructing a _context manager_. The latter ensures that the file is properly closed when you're done (as unintentionally leaving files open can have some downsides depending on Python version and operating-system). To prevent mistakes with reading and writing, keep in mind that files maintain a pointer to a 'current position' in the file.
- - - - -

**15.19.** The above code created the file `test123.txt` in the same directory that contains the Python script, because it is a _relative_ path, i.e., it specifies the location _relative to_ the current working directory. An _absolute_ path specifies the location of a file all the way from the root of your file-system or home directory (e.g., `C:\` in Windows, `~` on Mac, Linux). Re-run the above code with different paths (though keeping the above warning in mind!), including an _absolute_ path to a place on your disk (e.g., depending on operating system, `C:\Documents\test123.txt` or `~/Documents/test123.txt`), and a _relative_ path to a sub-folder of the current working directory, e.g., `output/test123.txt` (first create such a folder if none exist yet).

**15.20.** In PyCharm, you can right-click (or ctrl-click) on a file in the Project tab on the left, choose 'Copy path/reference' and select 'Absolute path' or 'Path from repository root'. Try this (copy, and then paste the copied path somewhere else, e.g., into a string in your python script). If your Python script is in the repository root (i.e., not in a sub-folder), then the latter corresponds to the _relative_ path from your Python script.

**15.21.** How does writing to and reading from a file in the above manner relate to other input/output methods we have so far, both in purpose and in function? Consider `input`, `print` and `import`. For instance, with regard to function, do `write` and `print` behave differently with regard to newlines? Does `write`, like `print`, allow non-string arguments? Does it allow multiple arguments?

**15.22.** Do you expect the following two code snippets, when executed separately, have the same end result? What could be reasons for preferring one over the other? (And can you predict the file's contents if the second snippet, too, were to use write mode `w` instead of `a`?)

```python
with open('test123.txt', 'w') as file:
    for i in range(10):
        file.write(f'{i}\n')

for i in range(10):
    with open('test123.txt', 'a') as file:
        file.write(f'{i}\n')
```


**15.23.** Instead of calling `read` on a file, you can also iterate over a file with a loop. Test the following on a multi-line file, and explain why the resulting printed lines all have empty lines in between.

```python
with open('test123.txt', 'r') as file:
    for line in file:
        print(file)
```


**15.24.** What happens if you duplicate the above loop, such that (within the `with`-statement) it attempts to loop over the file twice? What happens if you duplicate the entire `with`-statement (each containing the loop once)? Does this align with what you learned earlier about calling `read` multiple times?

**15.25.** To practice, write a function that opens a file and iterates over it, and in the end prints the average line length in number of characters and number of words (using a simple tokenization function from earlier).

- - - - - -
**Something to keep in mind:** Unlike 'opening' a file in the way you are used to (e.g., opening a document in MS Word), opening a file in Python with `open` does not yet load the contents of the file into working memory. We have seen that calling `.read()` on an open file does the latter. Sometimes, if a file is particularly large (why then?), it is preferable to read it one line at a time, which you can do by iterating over the file itself.
- - - - -

**15.26.** Can you also use list comprehension to iterate over a file? Try this, to collect (for instance) the first character of each line in a file, to construct a list containing the separate lines of the file, or to construct a list containing the separate lines of the file where each line has been _stripped_ of its final newline character `\n`.

**15.27.** In this and the next few exercises you will be writing a function `read_from_gutenberg`, that will serve as good practice and be useful for subsequent sections. It should take a path to a `.txt` file you downloaded from the Gutenberg project (https://www.gutenberg.org/) and simply return the file's text content as a single string. In the next exercises you will make this function more sophisticated.

**15.28.** Text files from the Gutenberg project contain some meta-information (title, author, licence, etc.) that must be distinguished from the actual, original text: look in such a file for lines beginning with `*** START` and `*** END`. Enhance your `read_from_gutenberg` function so that only the original text (between the `*** START` and `*** END` lines) is returned.

**15.29.** Modify your `read_from_gutenberg` function so that instead of ignoring the meta-information, it parses the file-initial portion (with, e.g., title and author information) and returns it as a dictionary. More precisely, any line above `*** START` that contains a colon, should be added to the dictionary as a key-value pair. Your function will thus return both the extracted text and this dictionary.

**15.30.** One further enhancement: text files from the Gutenberg project are 'hard word-wrapped', meaning a newline character was inserted whenever a line exceeded (e.g.) 75 characters. Since these single newlines (`\n`) were not meaningful parts of the original text, we want to get rid of them (e.g., replace them by a space). However, we do not want to loose the information carried by _double_ newlines (`\n\n`), which _do_ represent a meaningful aspect of the original text, namely paragraph separations.

**15.31.** Move your `read_from_gutenberg` function to the file `text_utils.py`, as we will use it in the next section.

<br>**_Unique elements (`set`)_**

**15.32.** Use your function `read_from_gutenberg` from `text_utils.py` (Section 15) to load a text file from the Gutenberg project, and tokenize it to obtain the list `tokens`.

**15.33.** When processing texts it is often useful to get the _unique_ elements (e.g., words, bigrams, part-of-speech combinations, consonant clusters) from our data and _sort_ them (e.g., alphabetically, by occurrence count, by similarity to some search query). Python's _set_ data structure contains every element only once, hence creating a set from a list (or other collection) amounts to filtering out duplicates, leaving each unique element once. Construct a set from the `tokens` list from above by doing `set(tokens)`.

**15.34.** Print an overview of the methods provided by the resulting set object (with `dir`).

**15.35.** In maths/set theory, sets are written with curly braces like `{1, 2, 3}`. Does that work in Python, too? What about creating an empty set like this `{}`? (Make a prediction, but also try it and, just to make sure, check the type of the resulting object.) Can you find some (other) way to create an empty set?

**15.36.** Can you create a set containing strings? A set containing tuples? A set containing lists? Why (not)?

- - - - - -
**Something to keep in mind:** The **set** data structure contains each element only once. Moreover, sets are significantly faster than lists when it comes to determining if an object is present in the set. (Though lists are much faster if you know the index of the object you are looking for.) The price to pay for this lookup speed is that sets can only contain objects that are **hashable**, just like a dictionary's keys.
- - - - -

**15.37.** Do you remember some objects that are, and some objects that aren't hashable?

**15.38.** Do sets have a 'length' (`len`)? Can you check with `in` whether a set contains a certain element? Can you iterate over a set? Can you construct one set from another using comprehension syntax? Do you expect that you can use slicing on a set, as you would with a list? Why (not)? Test your expectation.

**15.39.** After creating a set, one can add elements to it with the method `add`, e.g., `my_set.add(5)`. What happens if you try to add an element that is already in the set? Do sets also have an `append` method like lists? Why might this be?

**15.40.** Can you predict what happens if you construct a set not from the tokens, but from the original, un-tokenized text directly? Verify your prediction.

