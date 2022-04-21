import operator

"""
16. Basic text processing
"""
import text_utils

# 16.1
# Change this path if necessary, depending on where you put your files.
gutenberg_path = '../adventures/data/gutenberg/alice_pg35688.txt'

text, meta_info = text_utils.read_from_gutenberg(gutenberg_path)
tokens = text_utils.tokenize(text)

# 16.2
vocabulary = set(tokens)
print(vocabulary)
# It's still quite messy. Consider stripping punctuation and newlines from the tokens here or (probably better) by
# improving the tokenizer's handling of these aspects). Standardizing capitalization would also be nice (see further below).
print(len(tokens))
print(len(vocabulary))

# 16.3
print([name for name in dir(set) if not name.startswith('_')])

# 16.4
is_this_a_set = {1, 2, 3}
print(is_this_a_set, type(is_this_a_set))   # yes!

what_about_this = {}
print(what_about_this, type(what_about_this))   # nope!

empty_set = set()
print(empty_set, type(empty_set))   # yep

# 16.5
print('16.5')
print({1, 2, 3} == {3, 2, 1})
print([1, 2, 3] == [3, 2, 1])


# 16.6
set_of_strings = {'a', 'b', 'c'}
set_of_tuples = {(1, 2), (3, 4)}
# set_of_lists = {[1, 2], [3, 4]}     # TypeError, as lists aren't hashable.

# 16.7
print('16.7')
print(len(set_of_strings))
print('a' in set_of_strings)
for t in set_of_tuples:
    print(t)
new_set = {x for x in set_of_strings if x.startswith('b')}
print(new_set)
# set_of_strings[0:2]    # nope, set object is not subscriptable, i.e., doesn't allow slicing/indexing.
    # this is as you might expect, because sets don't have an order.

# 16.8
set_of_strings.add('test')
print(set_of_strings)
set_of_strings.add('test')
print(set_of_strings)   # nothing changed

# set_of_strings.append('test')   # nope, no append method; this makes sense, because appending is something you do
    # 'at the end', i.e., after the 'final element', but sets don't have an order.

# 16.9
print('16.9')
print('Check the order:', end=' ')
for c in {'a', 'b', 'c', 'd', 'e', 'f'}:
    print(c, end=' ')
print()
# The order should differ if you re-run the same script multple times (if not, perhaps you have a 'strange' Python implementation?).

# 16.10
print('16.10')
# print({1, 2, 3} + {2, 3, 4})  # error: 'unsupported operand types'.
print({1, 2, 3} & {2, 3, 4})    # intersection
print({1, 2, 3} | {2, 3, 4})    # union
print({1, 2, 3} - {2, 3, 4})    # remove (in set-theory also: 'relative complement')

# 16.11
print('16.11')

def standardize_capitalization(tokens):
    """
    Lower-cases any token that already occurs lower-cased somewhere. Keeps capitals intact otherwise.
    """
    standardized_tokens = []
    rough_vocab = set(tokens)   # this only serves faster lookup in what follows
    for tok in tokens:
        if tok.lower() in rough_vocab:
            tok = tok.lower()
        standardized_tokens.append(tok)
    return standardized_tokens

standardized_tokens = standardize_capitalization(tokens)
vocabulary = set(standardized_tokens)
print(vocabulary)

# Applying this standardization is best done to the tokens _before_ computing a vocabulary, because we will likely
# need the standardized tokens also for, e.g., computing token counts, which we will do below.

# 16.12
# the 'os' module provides more robust ways to manipulate file paths, but for now this stringy mess suffices.
out_path = 'output/' + gutenberg_path.rsplit('/', maxsplit=1)[-1].replace('.', '_vocab.')
with open(out_path, 'w') as file:
    for w in vocabulary:
        file.write(w + '\n')

# The written file contains some empty lines. Why? Note that the vocabulary is still quite 'polluted', e.g., some tokens
# have newlines \n attached to them. One could solve this by improving the tokenizer's handling of newlines.

# 16.13
print('num unique tokens:', len(vocabulary))
print('lexical diversity:', len(vocabulary)/len(tokens))

# 16.14
# One possible consideration: It might make sense to standardize verbal inflection, because it inflates the vocabulary
# and makes verbs count much more than nouns toward the vocabulary size. Perhaps different media have different
# proportions of verbs and nouns, that could therefore mess with our calculated lexical diversities.

# An algorithm for removing inflection would have to have some knowledge of morphology, and perhaps of which things
# are verbs (via parsing and/or part-of-speech tagging). Because 'walks' should be standardized to 'walk', but the noun
# 'bed' should not be standardized to 'b'. Also some knowledge of consonant doubling (e.g., 'robbed' should not be
# standardized as 'robb', but as 'rob'). And irregular verbs...

# 16.15
print(set(text))
print(len(set(text)))   # You might have estimated something like 26 + 26 + 10 and then some more (punctuation).

# 16.16
print('16.16')
my_list1 = [1, 3, 5, 6, 4, 2]
my_list1.sort()

my_list2 = [1, 3, 5, 6, 4, 2]
my_list2 = sorted(my_list2)

print(my_list1)
print(my_list2)
help(sorted)
help(list.sort)

# Reflect on the differences yourself.

# 16.17
print('16.17')
my_list3 = [1, 3, 5, 6, 4, 2]
sorted(my_list3)    # doesn't modify in place, so my_list3 unchanged
print(my_list3)

my_list4 = [1, 3, 5, 6, 4, 2]
my_list4 = my_list4.sort()  # modifies in place, so my_list4 reassigned None
print(my_list4)

# 16.18
# Nope, no sort method exists for these objects.
# {2, 3, 1}.sort()  # sets have no reliable order
# {'c': 1, 'a': 3, 'b': 2}.sort()   # dictionaries do have reliable order, but only in recent Python versions...
# 'kjhasdnbv'.sort()    # strings are not mutable, so no in-place sorting possible like on lists.
# (2, 3, 1).sort()      # same as for strings.

# 16.18
# Sorted can take any iterable. It always returns a list (given that its order is crucial).
print(sorted({2, 3, 1}))
print(sorted({'a': 1, 'b': 2, 'c': 3}))  # results in a list of only the keys; did you expect that?
print(sorted('asdkjqweh'))
print(sorted((2, 3, 1)))

# 16.20
# Since sort modifies the collection in-place, this only works for mutable collections whose order matters.
# For sorted this restriction doesn't apply, as any elements can be sorted into a new list, regardless of what
#    used to contain them.

# 16.21
print(sorted([1, 1, 2, 3, 3, 2, 1, 2, 1, 1]))   # Yes!

# 16.22
print(sorted(['apple', 'monkey', 'banana', 'aardvark']))
print(sorted([1, 2, 5, 2, 3, 1]))
print(sorted([(1, 2), (2, 3), (3, 2), (2, 1)]), flush=True)
# print(sorted([1, 2, 5, 'apple', 'banana']))   # error! str and int cannot be compared.

# 16.23
# Yes, len is a perfectly fine function; it returns an integer for each string, and integers can be sorted.
print(sorted(['apple', 'bee', 'cecil', 'hyperactive'], key=len))
# Remember that the key should be a reference to a function, not a function call (unless that called function returns a function, eh...).

# 16.24
print('16.24')
def nvowels(s):
    return len([c for c in s if c in 'aeiouAEIOU'])

print(sorted(['apple', 'bee', 'cecil', 'hyperactive'], key=nvowels))

# 16.25
print('16.25')
# sorted(['DEF', 'abc', 'ABC', 'def'], key=lower)   # Python doesn't know what lower is
print(sorted(['DEF', 'abc', 'ABC', 'def'], key=str.lower))  # yes, it's a string method

# 16.26
print('16.26')
print(sorted(['def', 'abc', 'ABC', 'DEF'], key=str.lower))
# lowercasing makes 'def' and 'DEF' equivalent, and apparently that means their initial order is maintained.

# 16.27
print('16.27')

for result in [
        # sort the numbers using their negated values as keys, hence from big to small:
        sorted([-5, -9, 2, 5, 8, 9, -3], key=lambda x: -x),
        # sort by absolute value (i.e., ignoring the minus signs):
        sorted([-5, -9, 2, 5, 8, 9, -3], key=abs),
        # sort kinda alphabetically, though ABC... comes before abc...:
        sorted(['Alf', 'alf', 'beth', 'Sue', 'Beth', 'sue']),
        # now it's properly alphabetical; note that using str.upper as in exercise above is arguably more Pythonic:
        sorted(['Alf', 'alf', 'beth', 'Sue', 'Beth', 'sue'], key=lambda x: x.upper()),
        # sort by inverted versions of the strings:
        sorted(['Alf', 'Beth', 'Sue'], key=lambda x: x[::-1]),
        # sort by second (index 1) character:
        sorted([(1, 5), (-2, 6), (2, 4), (2, 5)], key=lambda x: x[1]),
        # sort by second member and then first member of the tuple:
        sorted([(1, 5), (-2, 6), (2, 4), (2, 5)], key=lambda x: (x[1], x[0])),
        # sort by number of consonants
        sorted(['Hello', 'this', 'is', 'a', 'tokenized', 'text'], key=lambda x: len([a for a in x if a not in 'aeiou'])),
        # sort by proportion of consonants
        sorted(['Hello', 'this', 'is', 'a', 'tokenized', 'text'], key=lambda x: len([a for a in x if a not in 'aeiou'])/len(x)),
        # sort every element by the same constant value 873, regardless of the original value:
        sorted([6, 4, 2, 1, 3, 5], key=lambda x: 873),  #  (of course this is a nonsensical example)
        # sort as if they are numbers of hours as indicated on a 12-hour clock.
        sorted([13, 16, 2, 5, 3, 8, 52, 47, 49], key=lambda x: x % 12)
    ]:
    print(result)

# To better understand the latter:
numbers = [13, 16, 2, 5, 3, 8, 52, 47, 49]
print('Sort keys for the latter (x, y) meaning x is sorted by key y:', list(zip(numbers, [x % 12 for x in numbers])))

# 16.28
# lambda x: x.upper() defines a function that turns x uppercase.
# str.upper is already a function that does exactly that.
# instead, lambda x: x.upper defines a function that returns a function (namely, it returns the function x.upper)
# and str.upper() is not a function, but a function call (and one which misses an argument; try it yourself).

# 16.29
# Although it uses the inverted strings as keys, it merely uses these temporarily, to sort the original (non-inverted) strings by.

# 16.30
scores = {'John': 123, 'Mary': 512, 'Sue': 82, 'Alf': 921}
my_list = sorted(scores, key=lambda x: scores[x])

print(my_list)  # It sorts the strings, using their scores in the dictionary (hence square brackets) as sorting keys.

# 16.31
print(sorted([1, 2, 5, 'apple', 'banana'], key=lambda x: str(x)))

# equivalent to (e.g.):
# print(sorted([1, 2, 5, 'apple', 'banana'], key=lambda x: f'{x}'))

# 16.32
# sorted(['abc', 'cab', 'acb', 'bac'], lambda x: x[1])    # error: sorted expected 1 argument, got 2
sorted(['abc', 'cab', 'acb', 'bac'], key=lambda x: x[1])    # this is fine
# The sort key MUST be provided as a keyword argument, not a positional argument.
# This is enforced by the Python developer who wrote this code, by inserting an asterisk to 'eat up' any positional
# arguments and thereby enforce the remaining parameters to be given by keyword only.
# The decision seems reasonable, since otherwise one might mistakenly read sort(a, b) as sorting a and b
# relative to each other (similar to max(a, b) returning the maximum of a and b), instead of using b as the key to
# sort a by.

# 16.33
print('16.33')

import collections
counter = collections.Counter(['a', 'a', 'b', 'c', 'a', 'a', 'b', 'c', 'c', 'c', 'd'])

print(counter)
print(len(counter))
print(counter['a'])
print(list(counter.keys()))
counter['e'] = 10
counter.update(['a', 'a', 'b', 'd'])
for key, value in counter.items():
    print(key, value)
print(isinstance(counter, dict))
# The latter shows Counter is literally a sub-class of dict, so every Counter object is also a dict object.

# 16.34
print('16.34')
print(collections.Counter({1, 2, 3, 4, 5, 1, 2, 3, 1, 2}))
print(collections.Counter({'a': 3, 'b': 2}))    # not super interesting
print(collections.Counter('asdjkhqwekjasdasdkjhasd'))

# 16.35
# Counter is a class provided by the collections library. Counter() creates an object of that class.
# We called the created object 'counter', but we could have also called it 'blabla': that's just a variable name.

# 16.36
print('16.36')
print(counter.most_common(3))
print(counter.most_common())    # default behavior: show the full ordered list

# 16.37
print('16.37')
token_counts = collections.Counter(tokens)

print(token_counts.most_common(50))
for w in ['woman', 'girl', 'man', 'boy']:
    print(w, token_counts[w])

# 16.38
vocabulary_sorted = sorted(vocabulary, key=lambda x: (x[:1], token_counts[x]))

out_path = 'output/' + gutenberg_path.rsplit('/', maxsplit=1)[-1].replace('.', '_vocab_sorted.')
with open(out_path, 'w') as file:
    for w in vocabulary_sorted:
        file.write(w + '\n')

# 16.39
# This is up to you; consider for instance pronouns with apostrophes like I'm and you're, possessive suffix 's.

# 16.40
# A common idea (underlying also TF-IDF) is to 'normalize' the word counts for a given document, by dividing the number
# of times a word occurs in that document, by (some function of) the number of documents that contain that word
# (equivalent: multiply the Term Frequency (TF) by the Inverse Document Frequency (IDF)). The idea is that 'the' will
# be frequent in a given document, but also in all other documents, so it does not tell us anything about the topic of
# the current document. In contrast, a word like 'castle' may not appear in most documents, so if it does appear a lot
# in one document, then 'castle' is likely to be a topic of that document specifically.

# 16.41
bigrams = text_utils.ngrams(text, 2)  # I changed the function to return tuples, which will be easier to work with.
bigram_counts = collections.Counter(bigrams)

# 16.42
def collocationhood(token_counts, ngram_counts):
    token_probabilities = {token: count/len(tokens) for token, count in token_counts.items()}
    ngram_probabilities = {ngram: count/len(tokens) for ngram, count in ngram_counts.items()}
    collocationhoods = {}
    for ngram, prob in ngram_probabilities.items():
        independent_probability = 1
        for w in ngram: # ngrams being tuples pays off here!
            independent_probability *= token_probabilities[w]
        collocationhoods[ngram] = prob - independent_probability    # i.e., observed - expected
    collocationhoods_sorted = sorted(collocationhoods.items(), key=operator.itemgetter(1), reverse=True)
    return collocationhoods_sorted

bigram_collocationhoods = collocationhood(token_counts, bigram_counts)

print(bigram_collocationhoods[:30])

# 16.43
print('16.43')
trigrams = text_utils.ngrams(text, 3)
trigram_counts = collections.Counter(trigrams)

trigram_collocationhoods = collocationhood(token_counts, trigram_counts)

print(trigram_collocationhoods[:30])

# 16.44
print('16.44')
# I only changed the text_utils.ngrams function to also allow returning character-level ngrams.
# The rest just worked as it was!
character_counts = collections.Counter(text)
character_bigrams = text_utils.ngrams(text, 2, word_tokenize=False)
character_bigram_counts = collections.Counter(character_bigrams)

character_bigram_collocationhoods = collocationhood(character_counts, character_bigram_counts)

print(character_bigram_collocationhoods[:30])

# 16.45 and beyond:
# Be adventurous, up to you!
