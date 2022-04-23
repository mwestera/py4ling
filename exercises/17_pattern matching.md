# Python for linguists


## 17. Pattern matching (regular expressions)

**17.1.** Earlier we encountered string methods for searching (`index`, see also `find`), replacing (`replace`) and splitting (`split`). But often one wants to search for (or replace by, split on) not a _literal_ substring, but a _pattern_, i.e., characterizing a _class_ of substrings. _Regular expressions_ are a powerful and convenient method for this, available in Python from the standard `re` library. As a first illustration, execute the following code and try to formulate in ordinary English what the regular expression `[aeiou]+` might represent:

```python
import re

example_string = 'The famous Dr. Freud hastily acquired a magenta T-shirt and an old sweater for 24.95EUR. He then very very eagerly left the H&M at 1am... It was, as the doctor said, "a necessity".'
print(re.findall('[aeiou]+', example_string))
```


**17.2.** Enter `help(re)` or visit the (mostly equivalent) official documentation at https://docs.python.org/3/library/re.html for a global, initial impression; see especially the list of special characters in the section _Regular Expression Syntax_.

**17.3.** Use `re.findall` to test (and try to understand) which substrings of `example_string` the following regular expressions match:
 - `[a-z]+` 
 - `[a-zA-Z]+` 
 - `[a-zA-Z ]+` 
 - `[^a-z]` 
 - `[aeiou]` 
 - `[aeiou]*` 
 - `[^aeiou .]+` 

 Note that you can copy this list of regular expressions, paste the whole thing into your Python script in between triple quotation marks, and split the whole thing on newlines `\n`, to obtain a list of separate regular expressions.

**17.4.** It will be convenient for some of the following exercises to define a function `test_regexes` that takes a list of regular expressions and a string in which to search, and first prints the latter string, followed by each regular expression on a separate line alongside the list of matches that `re.findall` returns for it.

**17.5.** With the help of the documentation at https://docs.python.org/3/library/re.html#regular-expression-syntax, try to _predict_ which substrings the following regular expressions will match. Test your predictions with the help of the function from the previous exercise (and you can also use the suggested `example_string` from above).
 - `[0-9]` 
 - `[0-9]+` 
 - `\d+` 
 - `[a-z]+` 
 - `[A-Z]+` 
 - `[A-Za-z]+` 
 - `[a-zA-Z]+` 
 - `[A-Z]+[a-z]+` 
 - `[A-Z]+[a-z]*` 
 - `[^A-Za-z]+` 
 - `[A-Za-z0-9]+` 
 - `\w+` 
 - `\w+s` 
 - `\w+ly` 
 - `[^\w]+` 
 - `The|the` 
 - `[Tt]he`

- - - - - -
**Something to keep in mind:** **Regular expressions** are the go-to method for working with string _patterns_. Regular expressions form a special-purpose language, with its own little syntax, independently of (and older than) Python. In Python, the standard `re` module provides functions for searching, splitting on and replacing patterns defined by regular expressions.
- - - - -

**17.6.** Explore what happens if your regular expression is not well-formed (but the containing Python code is), e.g., what happens if you use a regular expression with mismatching brackets (`[A-Z`), an incomplete character range (`[A-]`), or two plusses (`[a-z]++`)? Can you define a character range outside square brackets (e.g., `A-Z` on its own)? If the latter is well-formed, can you figure out what it means? Can you construct a string in which it will find a match?

**17.7.** Form your predictions, then test them: In which of the following strings does the regular expression `ab+c*d` match some substring?
 - `abbccd` 
 - `abbbcd` 
 - `accd` 
 - `aabcd` 
 - `abc` 
 - `abbdd`

**17.8.** This is a bit of a puzzle: for the following regular expressions, can you find a string on which all three patterns will return the same match (the same substring)? And a string where they all yield different matches? Try to find the smallest possible strings that satisfy these requirements.
 - `[ab]c+` 
 - `a[bc]+` 
 - `[abc]+`

**17.9.** Try the same for the following regular expressions: 
 - `a+|b+` 
 - `a+b+` 
 - `[ab]+`

**17.10.** Suppose we want to find all indefinite articles (a, an). We can use the question mark `?`, which marks the thing that precedes it as optional (i.e., zero or one): `an?` therefore means `a` followed optionally by an `n`. Test this regular expression on `example_string` from above and explain its main shortcoming. Try to fix it by tweaking the regular expression (though it doesn't need to be perfect, see next exercise).

**17.11.** In the previous exercise, chances are (spoiler alert) that you tried adding spaces to signify **word boundaries** (like `' an? '`), in order to avoid matching on, e.g., the 'an' of 'and'. A shortcoming is that there exist word boundaries other than spaces (can you think of some?). Anticipating this, the `re` module provides a special character `\b` to represent a whole class of word boundaries. Verify this by looking up the meaning of `\b` in the online Python documentation for `re` (or via `help(re)`).

**17.12.** A slight obstacle for using `\b` in a regular expression, is that `\b` is _also_ a special character for Python itself, but with different meaning: it signifies a 'backspace' (≠ 'backslash'). Try `print('abc\bdef\b\bghij')` to see its effect. This means that, if you want create a string (to be used as a regular expression) containing an _actual, literal_ `\b`, you need to escape the backslash _with another backslash_, that is, write `\\b`: this tells Python that you mean literal `\b` instead of the special backspace character. Verify that this works by doing `print('abc\\bdef\\b\\bghij')`. This literal `\b` (defined in a Python string by `\\b`) can then be passed on to the regular expression parser, where it means a word boundary. Use this to improve your regular expression for matching _a(n)_. Does it make a difference on `example_string`?

**17.13.** To avoid having to worry about Python's special characters requiring double backslashes when defining regular expressions, it is customary to define regular expressions using **raw strings**, which are defined with an `r` prefix, like ``r'abc'``. Execute the following code to show that raw strings avoid the need for double backslashes. Also try printing each `regex`, and make sure you understand the result.

```python
regex1 = '\ban?\b'
regex2 = '\\ban?\\b'
regex3 = r'\ban?\b'

print(regex1 == regex3, regex2 == regex3)
```


**17.14.** Verify using your `text_regexes` function that `regex3` indeed works as intended for matching indefinite articles, and that `regex2` does too (it's just ugly), but `regex1` fails. To solidify your understanding, explain all of the foregoing, e.g., why either double backslashes or a raw string are necessary.

**17.15.** If you haven't done so already, improve the regular expression `regex3` to also match indefinites with an initial capital, i.e., _A(n)_, and apply it to a relevant test string (since no capitalized indefinites occur in `example_string`). If you are a bit stuck, review the various regular expressions in the exercises above.

**17.16.** Define a new regular expression that matches all definite articles (_the_) in `example_string`. Make sure your regular expression matches the capitalized `The` at the start, and correctly ignores the word `then`.

- - - - - -
**Something to keep in mind:** Defining a regular expression involves two steps: first the Python interpreter parses your string definition (turning a piece of your code into a string object), and then the regular expression parser of the `re` module interprets that string object as a regular expression definition. Using **raw strings** like `r'abc'` makes the first of these two steps as simple as possible (i.e., it tells Python to keep the backslashes in place), hence the definition of regular expressions more direct.
- - - - -

**17.17.** Predict the lengths (according to `len`) of the following strings and raw strings, keeping in mind that a special character like a newline counts as 1 character. (For additional insight also consider printing them.) 
 - `'ta\ta\ta'` 
 - `'ta\\ta\\ta'` 
 - `r'ta\ta\ta'` 
 - `r'ta\\ta\\ta'`

**17.18.** The strings (raw or plain) you use for defining regular expressions are ordinary Python strings, with the usual string methods. Concatenate the expression for matching indefinites with the expression for matching definites, with the regular expression operator `|` in between. Before testing it, explain in ordinary English what kinds of substrings the resulting composite expression will match.

**17.19.** Looking back at previous examples, explain whether `findall` returns _all_ substrings that match a given regular expression, or only a specific subset. Do you understand why this (default) matching procedure for regular expressions is called **greedy**? (Consider, for instance, the regular expressions `a+` and `aaa`, and how many matches each yields on the string `aaaaaaa`.)

**17.20.** If you are a linguistics student, did you ever come across the _Chomsky hierarchy_? Where do so-called _regular languages_ -- those characterizable by regular expressions -- fit in this hierarchy? Could you characterize the grammar of a natural human language in a regular expression?

**17.21.** As we have seen, some characters, escaped by a backslash, have special meaning in a regular expression. Do you remember the meanings of `\b`, `\w` and `\d`? In addition, with the help of the `re` documentation, illustrate the meanings of `\s` and `\A` by matching them on relevant example strings.

**17.22.** `\d \+ \d` will match any simple summation of single-digit numbers, like _3 + 6_. Verify that it works. Why do you think the backslash in front of the `+`-sign is needed? What if you omit it?

**17.23.** Expand (and test) the foregoing regular expression for summation, to work also with multi-digit integers like `123 + 51221`. Next, expand it further to also handle subtraction, division and multiplication, and make the spaces around the operator optional (e.g., permitting also `123-321`)`.

**17.24.** Take a moment to appreciate the power of regular expressions: what would the plain Python code look like, in outline, for solving the previous exercise? No actual programming required; just a sketch suffices.

**17.25.** It is often convenient to compose a bigger regular expression from smaller ones with format strings (and a string can be both a _raw_ string and a _format_ string at the same time: `fr'{some_variable}'`). Try this for your maths regular expression from two exercises ago, by defining one expression `number` that matches numbers, another `operator` that matches operators, and combining them with a format string. Verify that it still works as intended.

**17.26.** The period `.` is another special character: outside a square brackets context, the `.` matches _any_ character except newline. (What does it match _inside_ square brackets?) Accordingly, to match an _actual_ period, you need to escape it with backslash. Given this, predict what the following regular expressions mean, and verify your prediction by matching them on a relevant example string of your choice:
 - `.+` 
 - `\.+` 
 - `".+"` 
 - `...`

**17.27.** Since the backslash `\` is a special character for the regular expression parser, defining a regular expression that matches an actual, literal backslash requires escaping the backslash, i.e., `\\`. Verify your understanding, by explaining why even in a _raw_ string, you need a double backslash to match a literal backslash. And given that `\` is a special character also for the Python interpreter, how many backslashes would you need to enter in a _non-raw_ string, in order to define a regular expression that matches a single, literal backslash?

**17.28.** Let us combine the power of regular expressions with some of the things we learned before. In a text of your choice (e.g., a book from the Gutenberg project), find all vowel clusters (single vowels or sequences thereof) and sort them by frequency, printing a top-20 of most frequent vowel clusters.

**17.29.** Do the same, but now for word-initial _consonant_ clusters, and (separately) for word-final consonant clusters. (Advice: define consonant by simply listing them manually, since defining consonant as 'anything alphabetical except a vowel' within a regular expression is tricky, requiring some `re` constructs that we have not covered yet.)

**17.30.** Think of an imperfect-but-good-enough way of detecting English adverbs with a regular expression. What are the most common adverbs in a text of your choice?

**17.31.** The module `re` provides functions `re.sub` (short for 'substitute') and `re.split`, which are analogous to the string methods `replace` and `split`, but take a regular expression to replace or split on (instead of a literal string). Use these functions to, separately: 
 - replace all vowels in a string by `a`; 
 - replace all adverbs in a given string by `badly`; 
 - censor all numbers, replacing them by _`<censored>`_; 
 - split a string into separate words by splitting on anything that is not alphanumeric (and identify some shortcomings); 
 - split a string into sentences by splitting on certain punctuation (and identify some shortcomings).

**17.32.** The `re` documentation (https://docs.python.org/3/library/re.html) explains several useful extensions of the basic regular expression syntax. Let us consider just two quick examples. With the help of the documentation and the examples below, try to understand what the extensions `(?i)` and `(?<!...)` are for:
```python
print(re.findall(r'the', example_string))
print(re.findall(r'(?i)the', example_string))
print(re.split(r'\.', example_string))
print(re.split(r'(?<!Dr)\.', example_string))
```


<br>**_Mini-adventure: Extracting dialogues from books_**

**17.33.** Download a text on the Gutenberg project that, incorporated in the story, contains reported speech surrounded by quotation marks (e.g., _The Adventures of Sherlock Holmes_, https://www.gutenberg.org/ebooks/1661). Extract such quotations with the help of a regular expression. You need to look for any passage contained in quotation marks, where the passage does not itself contain a quotation mark (why is the latter restriction necessary?). Be aware of the many types of quotation marks that can in principle be used (https://unicode-table.com/en/sets/quotation-marks/), and make sure your regular expression works at least for your specific text.

**17.34.** Building on the foregoing, write a function that extracts all 'dialogues' from a text, where a dialogue is a series of sufficiently close, consecutive quotations. Use the `span` method of the retrieved `Match` objects to decide whether two quotations are close enough to belong to 'the same dialogue', or whether they are better understood as constituting separate dialogues.

**17.35.** Write your corpus of extracted dialogues to a file, using a sensible format (so that, say, a dialogue researcher could easily read in the data with Python again).

**17.36.** Please consider sharing your code for this mini-adventure in the 'code review' course forum!

**17.37.** With a big enough corpus of literature, do you think the resulting corpus could be used as a window on actual human dialogue? Why (not), or in which way(s)?

<br>**_Retrieve more than substrings: `Match` objects and capture groups_**

**17.38.** To find not only the matching substrings but also the _locations_ of these matching substrings in the original string, use the function `re.finditer` (instead of `re.findall` we used earlier). For a given regular expression and string it returns an iterator over `Match` objects. Use this to find all definite/indefinite articles in the `example_string` from before (you can reuse your own regular expression from an earlier exercise). (Note: since `finditer` returns an _iterator_, you have to loop over it, or wrap it in `list(...)`, to get the results.)

**17.39.** From a given `Match` object you can retrieve the matched span (`match.span()`) and the substring (`match.group()`). Write a loop to print, instead of the `Match` objects themselves, more readable lines like `3-6: the` (representing a match with span (3, 6) and substring `the`).

**17.40.** The following function takes an iterator over (or iterable of) matches, and returns the original text with brackets `[..]` around the matching substrings. For some input it _almost_ works (e.g., call it with, as its `matches` argument, the result of `re.finditer(r'abc', 'abc abc abc')`), but for other input it gives an error (e.g., `re.finditer(r'abc', 'abc abc def')`). Can you fix it?

```python
def contextualize_matches(matches):
    matches = list(matches)
    text = matches[0].string
    bracketed_text = []
    for i in range(len(text)):
        if matches[0].span()[0] == i:
            bracketed_text.append('[')
        bracketed_text.append(text[i])
        if matches[0].span()[1] == i:
            bracketed_text.append(']')
            matches.pop(0)
    return ''.join(bracketed_text)
```


**17.41.** Use the (now corrected) function `contextualize_matches` to review the outcome of some of the previous exercises, e.g., all definite and indefinite articles in `example_string`.

**17.42.** You may wonder why the method for obtaining the matched substring is called `group`. Explore why, with the help of the regular expression `(\w+)ly`, in which the parentheses define a _group_ (containing just `\w+`). Use `re.finditer` to find all its matches on the `example_string` from earlier, and for each match print both `match.group()` and `match.group(1)`.

- - - - - -
**Something to keep in mind:** Parentheses in a regular expression define **capture groups**, and a `Match` object will provide a matching substring for each separate group. Thus, `match.group(1)`, `match.group(2)` etc. are substrings matching what's in the first set of parentheses, the second set of parentheses, etc. Call `match.group()` to get the substring matching the entire regular expression.
- - - - -

**17.43.** Define a regular expression containing a capture group, that lets you retrieve all vowel sequences (single vowels or multiple consecutive vowels) that are preceded by a consonant. Use the capture group to specifically print only the vowel part of each match.

**17.44.** What happens if your regular expression contains no round parentheses (i.e., no capture groups defined), and on a given match you call `match.group(1)`? What about `match.group(0)`? Explain the relation to `match.group()` in terms of the notion of 'default value'.

**17.45.** Does the `span` method of a `Match` object likewise take an integer argument? Does it do what you would expect?

**17.46.** Recall from the start of this section that `re.findall` returns the matching substrings directly, so no `Match` objects with groups and spans. How does `re.findall` (and hence your helper function from earlier, `test_regexes`) handle capture groups? Investigate this by matching the regular expressions `ab`, `(a)b`, `(a)(b)` and `((a)b)` against a simple string such as `'abab'`.

**17.47.** Although round parentheses `(...)` have a special meaning in regular expressions, namely capture groups, they are also still used for governing **operator precedence**. Explain which patterns the following regular expressions match (some may match the same). (To avoid confusion, use `finditer` to test these expressions, not `findall`, because of how the latter implicitly handles capture groups.) 
 - `(ab)+` 
 - `a+b+` 
 - `ab+` 
 - `(ab+)` 
 - `a(b+)`

**17.48.** Recall your mathematical expression from a while back (for summation, subtraction, etc.). Generalize it to also accept floating point numbers (e.g., `0.151 + 6512.36432`). (Note that only a single period per number is permitted, e.g., not `0.52.312 * 65.1543`). Compose your regular expression from simpler building blocks using a format string.

**17.49.** If your regular expression defines a capture group, you can invoke it in the same regular expression with a backslash-number, e.g., `\1` refers to the substring matched by group 1. Do you expect `(\w)\1` to match anything on `example_string`? Test your understanding.

**17.50.** Could the regular expression `(h[aeio])\1+` be used to detect grammatically well-formed laughter?

**17.51.** Can you predict what `(\b\w+\b)\s\1` will match? Test it on `example_string` (again, `finditer` is advised, given the way `findall` implicitly handles capture groups). To check your understanding of the 'greedy' nature of regular expression matching (see earlier), can you predict the number of matches it will have on the string `'test test test'`?

**17.52.** Let's take another look at a text of your choice (e.g., from the Gutenberg Project). What are the most frequently reduplicated words?

**17.53.** Compare the following two regular expressions, intended for a simple sentence tokenizer using `re.split`, and verify your understanding of the difference by reading in the Python documentation how `re.split` is supposed to handle capture groups (e.g., `help(re.split)`). Can you conceive of a scenario (e.g., research or application) for which the second sentence tokenizer might be more convenient than the first? 
 - `[.!?]+` 
 - `([.!?]+)`

**17.54.** Write a program that extracts _questions_ from a text, automatically categorizes them based on the question-word (e.g., who, what, where), if any, and feeds these categorizations into a `Counter`. (Make sure to view the actual data and, if needed, clean up your text or the extracted questions prior to categorization.) Which types of questions are the most frequent in a text of your choice? How might this depend on genre (within literature, but also compared to, e.g., dialogue, twitter, fake news vs. real news...)?

