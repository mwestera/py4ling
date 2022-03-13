# Python for linguists


## 9. More practice with lists and loops (also `index`, `range`)

**9.1.** Define three functions, each of which takes a list of numbers (e.g., the outcomes of an experiment) and returns a number. The first returns the sum of all elements. The second uses the summation function to compute and returns the list's average. The third uses the averaging function to compute and return the list's standard deviation. For the latter, you can do `import math` to use the `math.sqrt` function.

**9.2.** Write a function that takes a list of words like `words = ['the', 'dog', 'is', 'in', 'the', 'garden']`, takes the length of each word, and prints the total sum of word lengths. Do you get the same number as `len('the dog is in the garden')`? Why (not)? What about `len(words)`?

**9.3.** Write a function `index_in_string` that takes a string and a character, and returns the index of the first occurrence of that character in the string. For instance, `index_in_string('david', 'v')` returns `2`. Explain why `index_in_string` can be seen as the inverse of the square brackets slicing notation for retrieving a character by index.

**9.4.** Write a function `index_in_list` that does the same, but for a list instead of a string. Could you reuse any of the previous code?

**9.5.** Lists and strings in fact already come with a method `index`, which is called like this: `'david'.index('v')` or `[6, 4, 8, 6].index(8)`. Does this method behave the same as your own implementation from the foregoing exercises? What happens if the string or list does not contain the element you request the index for? Which index is returned if it contains the requested element multiple times? After testing this empirically, call for `help` on the `index` method to confirm your findings.

- - - - - -
**Something to keep in mind:** Lists and strings have a method **index**, which you can use to find the (first) index of an element in the list, provided it exists.
- - - - -

**9.6.** Write a function `find_index_of_largest` that finds and returns the _index_ of the largest element in a list (in mathematical terms this would be an _argmax_ function). You can do this without any explicit looping, namely by using the built-in functions `max` and the list method `index`. (Optional: Consider why this is not the most _computationally efficient_ way, e.g., imagine you had a list of millions of numbers.) What if you give your function a list of strings? What if you give it not a list, but a single string?

**9.7.** Write a function that takes a string, namely an English sentence, and loops through the characters of the string, ultimately returning the total number of _words_ in the sentence. Hint: Generally speaking, in written English, how do you know a new word is beginning?

**9.8.** Write a function that takes a string and returns a new string where all vowels have been replaced by the character _y_. Could you change the function to modify the original string _in-place_, instead of returning a changed copy? What if you give it a list of characters instead of a string, e.g., `vowels_to_y(['b', 'a', 'n', 'a', 'n', 'a'])`?

**9.9.** It is often convenient to loop over consecutive numbers (0, 1, 2, 3, ...). One way to achieve this is to create a list of numbers and loop over those list elements just as we did before, e.g., `for n in [0, 1, 2, 3]:`. Use this technique to print each number from 0 to 9. To understand a downside of this technique, consider printing the numbers up to 999 in the same way (but don't).

**9.10.** A more convenient way to loop over consecutive numbers is to use `range`, e.g., `for i in range(10):` loops over all integers from 0 to 9. Try this, and see how easily it scales up to larger ranges.

- - - - - -
**Something to keep in mind:** To loop over a **range** of consecutive integers from 0 to some integer `n`, use `range(n)`. We will learn more about `range` later, as it is a lot more flexible/powerful than simply 'integers from 0 to _n_'.
- - - - -

**9.11.** For a list like `words` from above, what does looping over `range(len(words))` achieve? Use it to print each index (0, 1, 2, ...) next to the corresponding element in the list (`0 the`, `1 dog`, `2 is`, etc.). (Later we will learn a slightly more Pythonic way to achieve this, using `enumerate`.)

**9.12.** What happens if in the above `range` construction, you forget the `len`, so it reads `for i in range(words)`? This type of mistake is easily made, so it is helpful if you can recognize it. And what happens if you accidentally do `for i in range(len(words - 1))`? (Do you see the mistake?)

**9.13.** Use `range` to iterate over indices of the list `words`, in a way that lets you print _pairs_ of consecutive words, or **bigrams** (`the dog`, `dog is`, `is in`, etc.). What should be the upper bound of your range?

**9.14.** The code below implements a simple tokenizer, that takes a text and returns a list of words. (Later we will learn more convenient methods for this, but the code below illustrates a useful pattern.) Try to understand how the function works and apply it to a number of sentences. Can you improve the tokenizer to ensure that punctuation marks are treated as separate tokens? For example, `tokenize('Hello, world!')` should return `['Hello', ',', 'world', '!']`. Subsequently, can you think of some other shortcomings and possible fixes?

```python
def tokenize(sentence):
    tokens = ['']
    for char in sentence:
        if char == ' ':
            tokens.append('')
        else:
            tokens[-1] += char
    return tokens
```


**9.15.** Define a function that takes a string (an English sentence) and first uses your `tokenize` function to obtain a list of tokens, and then loops through the resulting tokens to collect all _bigrams_. Your function should return a list of all bigrams. You can represent each bigram as a list containing two words (or a tuple/pair, but we will learn about that later), e.g., `['the', 'apple']` for the bigram _the apple_. The returned list is, therefore, a list of lists, each inner list containing two strings.

**9.16.** Create another function to collect not bigrams but _trigrams_, i.e., sequences of three consecutive words.

**9.17.** Two more conceptual questions (no programming required): 
 1. Currently your `bigrams` and `trigrams` function each take an untokenized string as parameter and call the `tokenizer` function on it. This means that, if we need both bigrams and trigrams for our research, we would be tokenizing each text _twice_! How could we restructure the code to avoid this redundancy? 
 2. Can you think of a way to combine the `bigrams` and `trigrams` functions into a single `ngrams` function (maybe taking an additional integer argument `n`), to avoid code repetition?

**9.18.** In the following example, how come the list `cities` doesn't change?

```python
cities = ['amsterdam', 'rotterdam', 'leiden', 'gouda', 'eindhoven']
for city in cities:
    city.capitalize()

print(cities)
```


**9.19.** What about now? (First formulate your prediction, then test it.)

```python
cities = ['amsterdam', 'rotterdam', 'leiden', 'gouda', 'eindhoven']
for city in cities:
    city = city.capitalize()

print(cities)
```


**9.20.** If the previous code did not change the list `cities`, modify the code so that it does. Does your modification actually change the original list in-place, or create a new, modified copy (re-assigned to the old variable)?

**9.21.** Earlier we saw that if-clauses can be nested. What about for-clauses? Write a function (and think of an appropriate name) that loops over the `cities` list from earlier (`for city1 in cities:`), and nested within that loop, loops over the same list again (`for city2 in cities:`). In the body of the inner loop, print the two names stored in `city1` and `city2`, concatenated with a dash in between. Can you predict what will be printed? Try it, and make sure you understand what's happening.

**9.22.** (It will likely be helpful to print a separator in between exercises (e.g., `print('---------')`), or you'll loose track of where each printed text originates from!) In the previous exercise, why did the inner loop use a different variable from the outer loop, namely `city2` and `city1`, respectively? Do you understand the output of the following variant?

```python
for city in cities:
    for city in cities:
        print(city)
```


**9.23.** Use nested loops and if-statements to print all pairs of cities where the first city name starts with a vowel and the second with a consonant. Looking at the city names, can you predict how many lines will be printed?

**9.24.** Write a function `chain` that takes a list of lists, and chains all lists into a single list. For example, chaining `[[1, 2], [3, 4, 5], [6, 7]]` will result in `[1, 2, 3, 4, 5, 6, 7]`.

**9.25.** Remember your random sentence generator from before? Use the same lists of words as before (determiners, nouns, intransitive verbs, transitive verbs), but now, instead of returning one random sentence, write a function that *prints* _all possible sentences_, one after the other. This will require many nested loops.

**9.26.** If your sentence generator had actually implemented a full human grammar, would the previous function ever terminate? (Should it?)

**9.27.** The four compass points can be abbreviated by single-letter strings as `'N'`, `'E'`, `'S'`, and `'W'`. Write a function `turn_clockwise` that takes one of these four compass point strings as an argument, and returns the next compass point in the clockwise direction.

**9.28.** Explain the difference between `type(turn_clockwise)` and `type(turn_clockwise('N'))`.

**9.29.** Also define an analogous function `turn_counterclockwise`. Should `turn_counterclockwise(turn_clockwise('N')) == 'N'` evaluate to `True`? Does it?

**9.30.** If you haven't done so already, perhaps you can streamline the functions `turn_clockwise` and `turn_counterclockwise` by storing the four compass points in a list. To simplify the function definitions, both the list method `index` and the modulo operator `%` can be useful here.

**9.31.** Extend your clockwise and counterclockwise functions to deal with four diagonal directions (such as North-East `NE` and South-West `SW`). If this is difficult or requires a lot of manual typing, it means your functions could probably have been implemented in a smarter, more concise way...

