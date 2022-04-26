# Python for linguists


## 16. Sorting and counting (`set`, `sort`, `Counter`, also probabilities)

<br>**_Vocabulary as a set_**

**16.1.** Use the function `read_from_gutenberg` from the previous section (in `text_utils.py`) to load a text file from the Gutenberg project, and tokenize the text (whether by using `split`, or a method already in `text_utils.py` from earlier) to obtain the list `tokens`.

**16.2.** When processing texts it is often useful to get the _unique_ elements (e.g., words, bigrams, part-of-speech combinations, consonant clusters) and _sort_ them (e.g., alphabetically, by occurrence count, by similarity to some search query). Python's _set_ data structure contains every element only once, hence creating a set from a list (or other collection) gives us the unique elements. Construct a vocabulary for the text from above by doing `set(tokens)`. If you already notice some ways in which your vocabulary is less than perfect (e.g., it contains lowercase and uppercase versions of the same word), explore ways to improve it (either by improving the tokenizer, or by doing some subsequent clean-up, before or even after turning the tokens into a set).

**16.3.** Apply `dir` to the set to get a quick overview of the available methods for this class. In fact, use list comprehension to print only the method names that do not start with an underscore.

**16.4.** In maths/set theory, sets are written with curly braces like `{1, 2, 3}`. Does that work in Python, too? What about creating an empty set like this `{}`? (Make a prediction, but also try it and, just to make sure, check the type of the resulting object.) Can you find some (other) way to create an empty set?

**16.5.** Also in maths/set theory, the order of elements in a set does not matter. Find a way to verify that this is how sets also behave in Python, and use the same kind of test on lists, to show that order does matter for lists.

**16.6.** Can you create a set containing strings? A set containing tuples? A set containing lists? Why (not)?

- - - - - -
**Something to keep in mind:** The **set** data structure contains each element only once. Moreover, sets are significantly faster than lists when it comes to determining if an object is present in the set. (Though lists are much faster if you know the index of the object you are looking for.) The price to pay for this lookup speed is that sets can only contain objects that are **hashable**, just like a dictionary's keys.
- - - - -

**16.7.** Do sets have a 'length' (`len`)? Can you check with `in` whether a set contains a certain element? Can you iterate over a set? Can you construct one set from another using comprehension syntax? Do you expect that you can use slicing on a set, as you would with a list? Why (not)? Test your expectation.

**16.8.** After creating a set, one can add elements to it with the method `add`, e.g., `my_set.add(5)`. What happens if you try to add an element that is already in the set? Do sets also have an `append` method like lists? Why might this be?

**16.9.** Although you can iterate over the elements in a set, the _order_ of iteration must not be relied upon (unlike lists and, in recent Python versions, dictionaries), as it depends on hash-codes which (in most Python implementations, for anything but the most basic types of objects) will vary between runs of the same program. Verify this by iterating over a set like `{'a', 'b', 'c', 'd', 'e', 'f'}` in your script, printing each element. Running the script several times should result in different element orders (though _within_ a run, e.g., if you iterate over the same set multiple times within a script, the order is maintained).

**16.10.** Recall that `+` is a shortcut for addition-like methods provided by classes like integer, string and list. Does `+` also work on sets? There are several operators in Python that work on sets. By trying with different sets, figure out what `set1 - set2`, `set1 | set2` and `set1 & set2` represent, and match these operators with some of the set methods you found above by doing `dir`.

**16.11.** Part of cleaning up a vocabulary is to standardize capitalization. Simply lower-casing all tokens before constructing the vocabulary (or lower-casing the vocabulary entries afterwards) is not quite satisfactory, since some words _must_ be capitalized. Define a function to standardize capitalization in a smarter way, i.e, that respects the fact that some words should not be lower-cased. Define this as a function that operates on a tokenized text (i.e., prior to constructing the vocabulary with `set`); can you think of a reason why that is the better place to do it?

**16.12.** Write code to output the vocabulary you obtained from the Gutenberg text to a new file (in a suitable place and with a suitable file name), with one word per line. Does the resulting file contain empty lines? Why? What might be a good way to fix this?

**16.13.** Suppose our purpose is to compare the **lexical diversity** of books (as on Gutenberg) vs. some other textual medium (e.g. tweets, or news media). Think of (or try to recall from an adventure) a way to compute the lexical diversity of the text, and implement this. Formulate a hypothesis about the comparative lexical diversity of different media (no need to actually test your hypothesis, though of course feel free to).

**16.14.** A conceptual question about lexical diversity: do you think verbal inflection ought to be standardized before computing lexical diversity, e.g., treating _walk_, _walked_ and _walks_ as the same entry? If not, can you think of some other purpose (research or applied) for which verbal inflection should probably be standardized? Can you think (in outline) of an algorithm to achieve this? (In Section 18 we will encounter two common approaches: _stemming_ and _lemmatization_.)

**16.15.** Can you predict what happens if you construct a set not from the tokenized text (`tokens`), but from the original, un-tokenized text directly? Roughly how many elements do you expect the resulting set to have? Only test this after formulating an explicit prediction.

<br>**_Sorting and counting_**

**16.16.** By printing the result, as well as `help` where needed, what are some differences between these two ways of sorting a list?

```python
my_list1 = [1, 3, 5, 6, 4, 2]
my_list1.sort()

my_list2 = [1, 3, 5, 6, 4, 2]
my_list2 = sorted(my_list2)
```


**16.17.** What goes wrong in the following two snippets?

```python
my_list3 = [1, 3, 5, 6, 4, 2]
sorted(my_list3)
print(my_list3)

my_list4 = [1, 3, 5, 6, 4, 2]
my_list4 = my_list4.sort()
print(my_list4)
```


**16.18.** Do you expect that you can call `sort` on a set, dictionary, string or tuple? Why (not)? Test your expectation and try to explain your finding.

**16.19.** Do the same for `sorted`: do you think its argument can be a set, dictionary, string or tuple?

**16.20.** The foregoing two exercises do not reflect just an arbitrary design decision of Python. Try to explain why, given other things you know about Python, the difference in availability/behavior of `sort` vs. `sorted` makes sense.

**16.21.** Does sorting a list keep its duplicate elements (if any)?

**16.22.** The `key` parameter of both sorting functions tells Python what aspect of the elements to sort on. If no `key` is provided, sorting will be based on whatever the comparison operators `<` and `>` are also based on (e.g., string comparison is kind of alphabetical (though how does it handle capitals, numbers, punctuation, etc.?); integer comparison is numerical, tuple comparison is defined in terms of comparison of the tuple elements from left to right). Verify this by sorting a list of strings, a list of integers, and a list of tuples. What happens if you try to sort a list containing objects of different types, e.g., both strings and integers?

**16.23.** If you do provide a `key`, then it needs to be a _function_ from the to-be-sorted elements to something sortable (i.e., a type of object for which `<` and `>` are defined). Would the built-in `len` such a function, i.e., could you use `len` directly as a key? Try to sort a list of strings with `key=len` (why not `key=len()`?).

**16.24.** Define a function that counts the number of vowels in a string, and use this as a key to sort a list of strings.

**16.25.** Why wouldn't `sorted(['DEF', 'abc', 'ABC', 'def'], key=lower)` work? What about `sorted(['DEF', 'abc', 'ABC', 'def'], key=str.lower)`?

**16.26.** Explain the difference in outcome, of `sorted(['DEF', 'abc', 'ABC', 'def'], key=str.lower)` vs. `sorted(['def', 'abc', 'ABC', 'DEF'], key=str.lower)`.

**16.27.** If the function you need as a sorting key will be used only for that purpose, defining a whole function in the usual way is a bit cumbersome. For this reason sorting keys are often defined as so-called **anonymous functions** in a single line using Python's `lambda` syntax. For instance, `lambda x: x[2]` takes a value `x` and returns its first character (index 2), `lambda x: x % 3` takes a value and returns its modulo 3, and `lambda x: len(x)` takes a value and returns its length (equivalent to simply `len` itself, of course). Predict the result of the following sorting commands, and then verify your prediction:
 - `sorted([-5, -9, 2, 5, 8, 9, -3], key=lambda x: -x)` 
 - `sorted([-5, -9, 2, 5, 8, 9, -3], key=abs)` 
 - `sorted(['Alf', 'alf', 'beth', 'Sue', 'Beth', 'sue'])` 
 - `sorted(['Alf', 'alf', 'beth', 'Sue', 'Beth', 'sue'], key=lambda x: x.upper())` 
 - `sorted(['Alf', 'Beth', 'Sue'], key=lambda x: x[::-1])` 
 - `sorted([(1, 5), (-2, 6), (2, 4), (2, 5)], key=lambda x: x[1])`  
 - `sorted([(1, 5), (-2, 6), (2, 4), (2, 5)], key=lambda x: (x[1], x[0]))` 
 - `sorted(['Hello', 'this', 'is', 'a', 'tokenized', 'text'], key=lambda x: len([a for a in x if a not in 'aeiou']))` 
 - `sorted(['Hello', 'this', 'is', 'a', 'tokenized', 'text'], key=lambda x: len([a for a in x if a not in 'aeiou'])/len(x))` 
 - `sorted([6, 4, 2, 1, 3, 5], key=lambda x: 873)` 
 - `sorted([13, 16, 2, 5, 3, 8, 52, 47, 49], key=lambda x: x % 12)` 

 Of course the more complex your sorting key function, the less readable it becomes if you define it all in a single line, and a separately defined function (with `def`) becomes more attractive.

**16.28.** Why do you need parentheses if you use the sort key `lambda x: x.upper()`, but not if you use the sort key `str.upper`?

**16.29.** Why doesn't `sorted(['Alf', 'Beth', 'Sue'], key=lambda x: x[::-1])` result in `['euS', 'flA', 'hteB']`?

**16.30.** Predict and explain in plain English what the following code achieves, then test it. Why does the key have square brackets now, not round parentheses?

```python
scores = {'John': 123, 'Mary': 512, 'Sue': 82, 'Alf': 921}
my_list = sorted(scores, key=lambda x: scores[x])
```


**16.31.** Earlier you found that sorting a list containing both strings and integers results in an error, as the two cannot be directly compared. Can you resolve this by providing your own custom key that turns integers into something that can be compared to strings?

**16.32.** What goes wrong with the code `sorted(['abc', 'cab', 'acb', 'bac'], lambda x: x[1])`, and why? (See the asterisk in the function's signature as seen in `help(sorted)`.) Do you agree with this design decision?

- - - - - -
**Something to keep in mind:** Among Python's built-ins there are two main functions for **sorting**: The function `sorted` takes an 'iterable' (anything over which you can iterate) and turns it into a sorted list; the list method `sort` (available only for lists) modifies a list in-place. Both functions take an optional argument `key`, that lets you specify a function to tell Python how to compare the to-be-sorted elements. Such functions can be built-ins, or defined using either `def` or (convenient in a single line) `lambda`.
- - - - -

**16.33.** Often we want to count elements and then sort them by the resulting counts (e.g., to find the most common elements). The **Counter** class from the `collections` module is specifically designed for this. Execute the following code and show with additional code that the `Counter` object behaves in many ways like a dictionary (e.g., remember how you access, iterate over, and update a dictionary?).

```python
import collections
counter = collections.Counter(['a', 'a', 'b', 'c', 'a', 'a', 'b', 'c', 'c', 'c', 'd'])
```


**16.34.** Do you expect that a `Counter` object can also be constructed from a set, from a dictionary, or from a string? Test this.

**16.35.** In the above code, what is the difference (in value, in use) between `Counter` and (lowercase) `counter`?

**16.36.** `Counter` is a subclass of `dict`, meaning it supports all methods a dictionary has, and potentially some in addition. One such added method is `most_common`, e.g., `counter.most_common(3)` returns the top 3 most common elements. The integer is an optional argument; what is this function's default behavior (i.e., if you omit it the integer)?

**16.37.** Construct a `Counter` object from the tokenized Gutenberg text and print the 50 most common words. Also look up some specific word counts (the way you would look up values in a dictionary).

**16.38.** Recall that tuples are (by default) sorted by their first component, then their second, their third, and so on. Use this to sort vocabulary items first by initial character, then by count, by providing a sort `key` function that takes a word and returns the kind of tuple by which words should be compared. (If you haven't already, first removing the empty string from your vocabulary can simply the current task.) Write the newly sorted vocabulary to a file, one word per line.

**16.39.** Viewing the resulting file (i.e., the vocabulary sorted alphabetically and by count) can reveal some further shortcomings of the tokenization and other preprocessing steps currently used. Can you find some vocabulary entries that you think ought to be split up? And pairs of vocabulary entries that you think ought to be treated as one and the same? Try to make some modest improvements, and try to make them where they make sense: some are best handled by improving the tokenizer, others perhaps by applying prior standardization steps to the raw text, or posterior cleanup to the derived vocabulary.

**16.40.** A conceptual exercise (though feel free to experiment with code): Do you think token counts obtained from a document could be used to obtain a list of words that represent the main _topic(s)_ of that document? If not directly, can you think of a way to transform (e.g., scale, divide, normalize) the token counts in such a way that the tokens with the highest values will be (more) representative of the topic(s) of a document? (Spoiler: this exercise may lead you to (re)invent the _TF-IDF_ algorithm (Term Frequency, Inverse Document Frequency), which is one of the most popular techniques in topic modeling and information retrieval.)

<br>**_Mini-adventure 1: Detecting collocations_**

**16.41.** The next few exercises are about automatically detecting **collocations**, which are words that occur together more often than one would expect based on their individual frequencies. Examples are 'regular exercise', 'fast food', 'richly decorated'. First, use `Counter` to count not just single tokens, but also (in a separate counter) bi-grams of your Gutenberg text. You can reuse your own function `ngrams` from a previous section (which should still be in `text_utils`), but it is strongly advisable to slightly change it, so it represents _n_-grams as _tuples_ (not as lists or strings).

**16.42.** Think of a way to compute a degree of 'collocation-hood' for each bi-gram, based on the single token counts and bi-gram counts. Then define a function that takes the single word counts and bi-gram counts, and returns a list of all bigrams ranked from most to least 'collocational'. Inspect the top results for a text of your choice. _Hint:_ Perhaps you can transform the raw counts into something like probabilities, by dividing them by the total number of tokens/bigrams: the greater the difference between the 'observed' probability of a bigram (`prob(word1 word2)`) and the 'expected' probability if the two tokens had been independent (`prob(word1) * prob(word2)`) the more 'collocational' the bi-gram is.)

**16.43.** Generalize the previous code to find potential three-word collocations, and inspect the outcome.

**16.44.** Generalize the foregoing to be able to find not only word-level collocations, but also character-level collocations (e.g., perhaps 'th' is more common than one would expect based on 't' and 'h' alone). A first (and perhaps sufficient) step may be to add to `text_utils.ngrams` a parameter `word_tokenize` with default value `True`; if you then call the function with `word_tokenize=False`, it should not word-tokenize the text prior to computing _n_-grams, instead using the individual characters as 'tokens' on which to compute the _n_-grams. (That might already be sufficient...)

**16.45.** Please consider sharing your code for this adventure in the 'code review' forum for the course.

<br>**_Mini-adventure 2: Language generation with an _n_-gram-based language model_**

_Consider doing the remainder of the homework first, before having a go at this adventure!_

**16.46.** Think of a way in which we can automatically generate text by, repeatedly, randomly sampling the next word given previous words, on the basis of _n_-gram probabilities estimated from a text corpus. While a pretty basic approach to language generation, currently even the largest, state-of-the-art deep learning language models are still a direct generalization of this simple idea.

**16.47.** If you haven't already, write a function that turns a `Counter` object into a dictionary of (estimated) probabilities.

**16.48.** Write a function that takes a starting word `prompt`, a dictionary of single token probabilities and a dictionary of bigram probabilities. It should return a random next word that could reasonably follow the `prompt` in a sentence (e.g., if the `prompt` is a noun like _cat_, the next word could be a verb like _sleeps_), by probabilistically sampling a word, for instance as follows (ignore the following suggestion if you like a puzzle!): 
 - Find a list of all bi-grams whose first word matches with the `prompt` (e.g., _cat sleeps_, _cat chased_, etc.). 
 - If some `prompt`-matching bi-grams are found, use `random.choices` to choose a random bi-gram from this list; you should provide `random.choices` with the optional argument `weights`, which should be a list of the probabilities of the bi-grams to sample from. The function should then return the _second_ word of the selected bi-gram (e.g., _sleeps_). 
 - If no `prompt`-matching bi-grams are found, just ignore the bi-grams and instead sample a random word based on the _single_ token probabilities (this will be very random, but it's a last resort).

**16.49.** Generalize the foregoing to allow also _tri_-grams: it will take tri-gram probabilities as an additional argument, and it will first check for a matching tri-gram, if that fails it tries the bi-grams, and only if that fails will it sample a single token at random (i.e., the last resort). For this generalization, it will be best to make the `prompt` a list of tokens: when searching tri-grams you can then look at the final _two_ tokens of the `prompt`).

**16.50.** Write a wrapper function that takes a tokenized text, computes the single token and _n_-gram probabilities, asks for an `input` from the user (a writing prompt, i.e., the start of a sentence), turns this into the (potentially multi-word) `prompt` list, and then repeatedly uses the above word sampling function to generate words continuing the `prompt`. Each time after sampling a word, the chosen word should be appended to the `prompt` list before sampling the next word, thus slowly writing a continuous text. Make sure your generator stops either when a sentence separator is generated (e.g., a period `.`) -- assuming your tokenizer didn't remove them! -- or when a certain maximum number of tokens has been generated. (To avoid having to re-count all the tokens each time you want to generate another sentence, consider either (i) writing the counts to a file the first time, and subsequently reading from that file if it exists; or (ii) wrapping the whole program in another loop so you can generate multiple sentences until you type 'quit' as a prompt, or something.)

**16.51.** Use the previous function to inspect the quality of your language generator. For instance, compare the generated sentences if you use 3, 2 and 1-grams vs. only 2 and 1-grams, or even only 1-grams. Do you observe differences in the type of generated language? Which is more grammatical? More human-like? Do you think your generator will improve with _n_-grams of higher _n_, and/or with a larger corpus to extract the probabilities from? (You can of course generalize your code to try this.)

**16.52.** Try to generalize the foregoing code to also work at the character-level, i.e., letting it sample one character at a time. What is your impression of the generated language? Do you think it will improve with character _n_-grams for higher _n_? Can you think of pros/cons of character-level generation vs. word-level generation?

**16.53.** State-of-the-art deep learning language models are, in essence (but grossly simplifying) still _n_-gram language models (and both character- and word-level models are in active use in industry and research), but with much higher _n_ and stronger ability to generalize to unseen words and _n_-grams (due to 'hidden layers' in an artificial neural network). With this in mind, can you give one reason why these models need _enormous_ datasets to 'train' on? And can you explain why contrary to popular claims of AI achieving human-like 'language understanding', such models have been criticized as being mere 'stochastic parrots'? What, if anything, might make humans different from such models?

**16.54.** Optional exploration: Use different types of input text for your language generation (e.g., children's story, fiction, news) to see if the generated text is faithful to each genre.

**16.55.** Share your most 'beautiful' sentence(s) in the course forum (subjective of course: it might be the most random or the most coherent, the most poetic, the most offensive...).

