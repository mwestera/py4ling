# Python for linguists


## 15. Basic text processing (`split`/`join`, `strip`, `read`/`write`)

**15.1.** Before learning how to read and write text files, it will be convenient to first learn a couple more basic string methods, that can be helpful for cleaning the data read from a file. As a warming up, look at `dir(str)`, or equivalently `dir('some_random_string')`, for a list of methods available on the string class itself. Explore at least the string methods `strip`, `swapcase`, `isalnum` and `center`; use `help` if needed (e.g., `help(str.strip)`) and illustrate how they work with your own examples.

**15.2.** What is the difference between the string methods `split` and `rsplit`? Illustrate with your own example.

**15.3.** Assume that we have assigned `test_string = 'abcblablablaabc'`. For each of the following invocations of `strip`, form an expectation about what it does (based on the `help` you obtained) and then test it (e.g., by printing the result), refining your understanding of `strip`:
 - `test_string.strip('abc')` 
 - `test_string.strip('cba')` 
 - `test_string.strip('a').strip('b').strip('c')` 
 - `test_string.strip('c').strip('b').strip('a')` 
 - `test_string.strip('bla')`

**15.4.** Call `help` on the `str.join` method, look at the example it provides, and try to join your own list of strings with a dash `-` in between.

**15.5.** Define a string `s` for which the following is _not_ true: `' '.join(s.split())`.

**15.6.** What happens if you try to join a list that contains objects other than strings, e.g., integers?

**15.7.** There may be something counterintuitive about `join` and `split`: `split` is called as a method of the string-to-be-split (with 'joiner' as an argument of the function call), while `join` is _not_ called on the strings to be joined, but rather, on the string used for joining them. For instance, when splitting/joining on `'-'`, the dash is the argument of `split`, but not of `join` (for which it is, instead, the object on which the method lives). The following variant would be more 'symmetrical' in this regard, as the connecting character `'-'` would be the argument in both cases. However, test this to see what type of error you get (and then fix it):

```python
names = ['john', 'sue', 'bob']
names_joined = names.join('-')	# Doesn't work!
names_unjoined_again = names_joined.split('-')
print(names == names_unjoined_again)
```


**15.8.** Two things can help you remember the aforementioned apparent asymmetry. First, try to think of a natural way in which to read `join` and `spit` commands, respectively, that will help you memorize the aforementioned apparent asymmetry. Second, try to think of a reason _why_ Python may have been designed this way, i.e., why `join` is _not_ called as a method _of the list to be joined_, but as a method of the string to join by.

**15.9.** Oh no! I copied a list of student names from a low-quality PDF and now all names are surrounded by weird symbols! See below -- imagine the list is much longer (so manual cleaning is not an option) but the type of 'noise' remains the same. Define a function that uses `split` and `strip` to return a list of separated, cleaned-up names:

```python
names = '''#*John#*
#*Mary# *,
*#*Suzy#*,
#*Bob#\t*;
#* Chris#\t*'''
```


**15.10.** Oops, copying from a different PDF resulted in even more mess, where all names are in uppercase and some characters were misread as similarly-shaped numbers. Can you tweak your previous cleanup function to handle this? Hint: there is a string method called `replace`.

```python
worse_names = '''#*T0DD#*
#*0NA# *,
*#*SUE#*,
#*ANN-M4RY#\t*;
#* R0S5#\t*'''
```


**15.11.** How does the string method `replace` work, exactly? What if the thing-to-be-replaced isn't there? What if it occurs multiple times? How can you use `replace` in order to _delete_ all occurrences of a certain substring? What do you expect the result of `'abc'.replace('', ' ')` to be (form an expectation first, then test it)?

**15.12.** Define a simple word-tokenizer function that uses `split` on spaces and `strip` to get rid of punctuation, and apply it to a sufficiently challenging string of your choice. Compare it to your earlier attempt at word-tokenization (e.g., the one you put in `text_utils.py` as part of Section 11), noting some potential differences and (possibly shared) shortcomings.

<br>**_Reading and writing files_**

**15.13.** Without searching the web, try to gather and formulate your intuitions: What is a file? What is the difference between, and relation between, long-term storage (e.g., your hard-disk, or the cloud) and working memory (RAM)? What is a folder (or directory)? What is a path (such as, depending on your operating system, `C:\Documents\semantics_report.pdf` or `~/Downloads/Alice_in_wonderland.txt`)? What might be the difference between an _absolute_ and a _relative_ path?

- - - - - -
**Something to keep in mind:** WARNING: Before executing any code that involves opening a file, _always_ assume the worst: that the referenced file, if it exists, will be destroyed/overwritten. Make sure you do not loose valuable data in case this happens. Some things we will learn -- using a context manager, opening a file as 'read-only' where possible, using relative paths -- and in general clean code help decrease the chance of unintended changes to your files.
- - - - -

**15.14.** Create a Python script with the following code. Execute it, then find the created file `test123.txt` on your computer and open it (it will be in the same folder as your Python script). 

```python
with open('test123.txt', 'w') as file:
    file.write('Hello!')
```


**15.15.** Experiment with the above code. What if, inside the `with`-block, you add a second write statement? What will be in the file if you repeat the entire `with`-block twice? Does a `with`-block create a local scope? Does this align with what happens if you try to write a bit more to the file _after_ (i.e., outside, non-indented) the `with`-block?

**15.16.** What if you omit the second argument of `open`, the string `'w'`? What if you replace it by an `'a'` and run the code several times? In each case inspect the resulting file.

**15.17.** Call `help(open)` and find the table explaining the different modes. Based on the previous exercise, what is meant by 'truncating' in the explanation given for `w`?

**15.18.** Given a list of strings, use a loop inside the `with`-clause to write all strings to the file, each on a new line.

**15.19.** Assuming you now have a multi-line file `test123.txt`, execute the following code to read it. Does `file.read()` read one character or one line at a time, or the full file contents at once?

```python
with open('test123.txt', 'r') as file:
    text = file.read()
print(text)
```


**15.20.** What happens if you try to read the same file with `read` twice in a row, _within_ a single `with`-block (and print the results of both reads)? What if you read the same file twice but in _separate_ `with`-blocks? Hypothesize about what may cause this difference.

**15.21.** The file method `read` optionally takes an integer argument. What does it do? Try it. Then form an expectation: what will happen if you call `read` repeatedly on the same file with this integer argument specified? First formulate your expectation, then test it.

**15.22.** When you open a file, a pointer is kept that tracks the 'current position' in the file, i.e., the index of the byte of the file that is to be read next. In read-only mode `r`, this pointer starts at 0 (start of the file) and is incremented while the file is being read. Can you reconcile this with your findings in the previous two exercises? What will be the value of this pointer after reading an entire file? Calling `.tell()` on the file gives you the value of the pointer -- you can use this to test your prediction.

**15.23.** What do you think the starting value of the pointer of a file will be when you use append mode `a`? And what if you use write mode `w`? Again, test your predictions with the `tell` method.

- - - - - -
**Something to keep in mind:** If with Python code you want to read from or write to a file, you first need to **open** the file. The standard idiom uses the built-in function `open`, which takes a path and a _mode_ (read-only `r`, write-only `w`, read-and-write `r+`, append `a`) and returns a file object with methods such as `read` and `write` and a pointer to the 'current' position in the file. After opening a file through Python, one should **close** it (because unintentionally leaving files open can have some downsides). In the previous examples, closing the file was automatically handled by wrapping the `open` statement in a **context manager**, `with ... as ...`: whenever the `with`-block ends (i.e., when you un-indent) or an error is encountered, the file is automatically closed.
- - - - -

**15.24.** Without a context manager, the code for reading a file would have looked as follows (note the manual `close`). Verify that it does the same:

```python
file = open('test123.txt', 'r')
text = file.read()
file.close()
print(text)
```


**15.25.** Code you executed further above created the file `test123.txt`. Find this file in the Project tab on the left, and open it in the PyCharm editor (e.g., by double-clicking it). Can you manually change the contents of the file in the editor? Do they show up if you subsequently read the file in Python (of course you will not see this if your script overwrites the file prior to reading it)? And if you write something to the file through Python, does your view of the file in the editor update automatically?

- - - - - -
**Something to keep in mind:** The file `test123.txt` was created in the same directory that contains the Python script, because `open` was given a **relative path**, i.e., it specified the desired file location _relative to_ the directory of the current (main) script. An **absolute path** specifies the location of a file all the way from the root of your file-system or home directory (e.g., `C:\` in Windows, `~` on Mac, Linux).
- - - - -

**15.26.** What might be (dis)advantages of using absolute vs. relative paths?

**15.27.** Re-run some of the above code with different paths (though keeping the earlier warning in mind, about losing data!), including an _absolute_ path to a place on your disk (e.g., depending on operating system, `C:\Documents\test456.txt` or `~/Documents/test456.txt`), and a _relative_ path to a sub-folder of the current working directory, e.g., `output/test789.txt` (first manually create such a folder if none exists yet).

**15.28.** In PyCharm, you can right-click (or ctrl-click) on a file in the Project tab on the left, choose 'Copy path/reference' and select 'Absolute path' or 'Path from repository root'. Try this (copy, and then paste the copied path somewhere else, e.g., into a string in your Python script). If your Python script is in the repository root (i.e., not in a sub-folder), then the latter corresponds also to the _relative_ path from your Python script.

**15.29.** How does writing to and reading from a file, relate to other input/output methods we have already learned about so far? Consider `input`, `print` and `import`. Compare them both in terms of their intended purpose and in terms of the details of their usage. For instance, do `write` and `print` behave differently with regard to newlines? Does `write`, like `print`, allow non-string arguments? Does it allow multiple arguments?

**15.30.** In the following code, choose appropriate modes in place of the `...`, such that -- assuming their respective files do not exist yet -- the two snippets have the same end result. What could be reasons for preferring one over the other?

```python
with open('testABC.txt', ...) as file:
    for i in range(10):
        file.write(f'{i}\n')

for i in range(10):
    with open('testDEF.txt', ...) as file:
        file.write(f'{i}\n')
```


**15.31.** File objects also have a method `readline`, which does what its name suggests. Use it to print just the first line of a multi-line file. Can you call this method repeatedly to print line after line? (To properly test it, make sure the file you use contains multiple lines of text, like `testABC.txt` written in the previous exercise.)

**15.32.** Instead of calling `read` on a file, or calling `readline` repeatedly, the more Pythonic way is to iterate directly over the file itself. Test the following on a multi-line file, and explain why the resulting printed lines all have empty lines in between. Then tweak the code to prevent this.

```python
with open('testABC.txt', 'r') as file:
    for line in file:
        print(line)
```


**15.33.** What happens if you duplicate the above loop, such that (within the `with`-statement) it attempts to loop over the file twice? What happens if you duplicate the entire `with`-statement (each containing the loop once)? Does this align with what you learned earlier about calling `read` multiple times?

**15.34.** What gets printed if you print the file itself (instead of the result of calling `read`)?

- - - - - -
**Something to keep in mind:** The previous exercise revealed that files have an `encoding` parameter, with value `UTF-8` (8-bit Unicode Transformation Format). Each file on your disk is a series of bytes, where each byte is 8 bits (bit = binary digit, i.e, 0 or 1). This is true for text files, but also for images, movies, word documents: they are all just series of bytes. What these bytes _represent_ depends on the **encoding** used for a given file. Nowadays you typically don't need to be concerned with encodings -- until it goes wrong (e.g., reading a file results in an error or a garbage string).
- - - - -

**15.35.** A simple encoding you may have heard of is ASCII. ASCII represents each character by a single byte. How many distinct characters does this let us represent? Is that enough?

**15.36.** To see a simple example of 'encodings gone wrong', write some emoji to a file (e.g., 😀😃😄). Emoji (like _many_ characters) are part of the widely adopted _Unicode_ standard, but not part of the much smaller ASCII set of characters. What happens if you open this emoji file with Python, and you give `open` the additional argument `encoding='ascii'`?

**15.37.** To practice, write a function that opens a file and iterates over it, and in the end writes some stats to a new file. Write at least the average number of characters per line, the average number of words per line, and the average number of characters per word (the next section will let us compute some more interesting stats; here you mainly practice reading and writing). Apply this function to a file of choice (e.g., a text file from the Gutenberg project). If your input file is (e.g.) `data/sherlock.txt`, the stats should be written to `output/sherlock_stats.txt` (manually create the `output` directory if it doesn't exist yet). The output path should be derived automatically from the input path, so you can easily apply the function to different input files.

**15.38.** Why might it be wise (in general) to separate the raw input data files from the directory to which you write output?

**15.39.** Unlike 'opening' a file in the way you are probably used to (e.g., opening a document in MS Word), opening a file in Python with `open` does not yet load the contents of the file into working memory. Instead, calling `.read()` on an open file is what actually loads the content. Sometimes, it is preferable to read a file one line at a time (which as we have seen can be done by iterating directly over the file object, or with `.readline()`). Can you think of a case where such line-by-line iteration might be preferable to reading the whole file at once?

**15.40.** Can you also use _list comprehension_ to iterate over a file? Try this, in order to create (each with a single line within a `with`-block): 
 - a list with the first characters of each line in a file. 
 - a list containing all the line lengths. 
 - a list containing the separate lines of the file where each line has been _stripped_ of its final newline character `\n`. 
 - a list of tokenized lines (hence a list of lists). 
 - a list of all lines that begin with a vowel.

<br>**_Mini-adventure: Reading `.txt` files from the Gutenberg Project_**

**15.41.** In this and the next few exercises you will be writing a function `read_from_gutenberg`. Not _super_ adventurous, but it will serve as good practice and be useful for subsequent sections! It should take a path to a `.txt` file you downloaded from the Gutenberg project (https://www.gutenberg.org/) and simply return the file's text content as a single string. In the next exercises you will make this function more sophisticated.

**15.42.** Text files from the Gutenberg project contain some meta-information (title, author, licence, etc.) that must be distinguished from the actual, original text: look in such a file for lines beginning with `*** START` and `*** END` (if your Gutenberg file does not contain these, maybe download a different one!). Enhance your `read_from_gutenberg` function so that only the original text (between the `*** START` and `*** END` lines) is returned.

**15.43.** Modify your `read_from_gutenberg` function so that instead of ignoring the meta-information, it parses the file-initial portion (with, e.g., title and author information) and returns it as a dictionary. More precisely, any line above `*** START` that contains a colon, should be added to the dictionary as a key-value pair. Your function will thus return both the extracted text and this dictionary.

**15.44.** One further enhancement: text files from the Gutenberg project are 'hard word-wrapped', meaning a newline character was inserted whenever a line exceeded (e.g.) 75 characters. Since these single newlines (`\n`) were not meaningful parts of the original text, we want to get rid of them (e.g., replace them by a space). However, we do not want to loose the information carried by _double_ newlines (`\n\n`), which _do_ represent a meaningful aspect of the original text, namely paragraph separations.

**15.45.** Move your `read_from_gutenberg` function to the file `text_utils.py`, as we will use it in the next section.

