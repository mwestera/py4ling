"""
13. Dictionary advanced
"""

# 13.1
name_to_id = {'Alf': '136124', 'Beth': '008623', 'Chris': '014212', 'Dave': '9123785', 'Esra': '978123'}

for x in name_to_id:
    print(x)
# What gets printed are only the keys!

# 13.2
print('13.2')
for key in name_to_id.keys():
    print(key)

for value in name_to_id.values():
    print(value)

for item in name_to_id.items():
    print(item)

# 13.3
def print_dict(dictionary):
    """
    Print the key-value pairs of a dictionary, each on a new line.
    """
    for key, value in dictionary.items():
        print(f'{key}: {value}')

print_dict(name_to_id)

# 13.4
print('13.4')
def update_dict(dict1, dict2):
    """
    Add all items from dict2 to dict1, modifying it in place.
    """
    for key, value in dict2.items():
        dict1[key] = value
    # Note that it doesn't return anything.

name_to_id2 = {'Bla': '12334', 'Blo': '809723'}

update_dict(name_to_id, name_to_id2)
print(name_to_id)

# 13.5
print('13.5')
name_to_id = {'Alf': '136124', 'Beth': '008623', 'Chris': '014212', 'Dave': '9123785', 'Esra': '978123'}        # first reset
name_to_id.update(name_to_id2)
print(name_to_id)   # yep, same result

# 13.6
# Variable assignment to a dictionary key updates a single item; the update function updates potentially multiple items.
# All the variants in the exercise give rise to (different types of) errors.

# 13.7
keys = name_to_id.keys()
print(keys)
print(type(keys))
values = name_to_id.values()
print(values)
print(type(values))
items = name_to_id.items()
print(items)
print(type(items))

# print(keys[1:3])    # not subscriptable
# print(values[1:3])    # not subscriptable
# print(items[1:3])    # not subscriptable

print(list(keys)[1:3])  # this works fine
print(list(values)[1:3])  # this works fine
print(list(items)[1:3])  # this works fine

# 13.8
print(list(name_to_id))
# this gives a list of keys, equivalent to list(name_to_id).keys())
# it matches the fact that looping over a dictionary (without the keys/values/items methods)
# likewise loops only over the keys.

# 13.9
dict1 = {1: 2, 5: 2, 3: 1}
dict1[5] = 3
dict1[1] = 10
print_dict(dict1)   # keys are ordered by first entry?

# 13.10
first_key = list(dict1.keys())[0]
print('value for first key:', dict1[first_key])

last_key = list(dict1.keys())[-1]
print('value for last key:', dict1[last_key])

# 13.11
max_key = max(dict1.keys())
print('value for max key:', dict1[max_key])

# 13.12
# Perhaps we have seen functions that return multiple values with return x, y.
# We've seen x, y = y, x to swap values.

# 13.13
print('13.13')

my_tuple = (1, 3, 5)
print(my_tuple)

# What types of values can they contain?
my_tuple2 = ('strings', ['l', 'i', 's', 't', 's'], ('nested', 'tuples'), 123, 6.5)  # basically anything
print(my_tuple2)

# Can you access their elements by index? What about slicing a range of indices?
print(my_tuple[1])     # sure!
print(my_tuple[:2])    # sure!

# Are tuples mutable?
# my_tuple[1] = 3 # Nope, or at least it does not support item assignment, just like strings.

# What happens if you omit the parentheses from your tuple declaration?
my_tuple3 = 1, 3, 5     # still a tuple

# Can you create an empty tuple?
my_empty_tuple = () # yep

# Can you convert a tuple to a list? To a string? Vice versa (like tuple('abc') perhaps?)?
print(list(my_tuple))   # yep
converted_tuple = str(my_tuple)
print(converted_tuple, type(converted_tuple))   # yep but it looks the same when printed ;)
my_tuple4 = tuple('abc')    # no problem!
print(my_tuple4)

# Does a tuple have a length?
print(len(my_tuple2))   # yup

# Can you concatenate two tuples into a new one using +?
my_concat_tuple = my_tuple + my_tuple2  # yep
print(my_concat_tuple)

# Can an element of a tuple be itself a tuple?
# Sure, see my_tuple2 above

# Can tuples be compared with operators like < and >?
print((3, 5) < (5, 8))
print((9, 5) < (5, 8))
print((9, 5) < (5, 3))
print((9, 5) < (9, 3))
print((9, 3) < (9, 5))  # Ah, so it compares by first element, then in case of ties by second element...

# 13.14
# Yes, try this yourself.

# 13.15
a = 1,
# print(a + 5)    # error because a is a tuple!

# 13.16
print((1, 2, 3) + (4, 5))   # tuple concatenation
print(1, 2, 3 + 4, 5)   # first computes 3 + 4 as addition, before creating the tuple containing it

# 13.17
print(True, True, True == (True, True, True))   # it's only comparing the last True to the tuple as a whole.

# 13.18
# With more data fields, it's difficult to remember the ordering in the tuple, and better to label
# each field with a key, hence a dictionary.
# With an in principle unbounded (and potentially varying) list of more homogeneous elements (instead of
# elements with distinct roles, as in the example tuple use cases), one likely wants mutability.

# 13.19a
# Tuples are hashable:
my_dict = {(1, 2): 3, (6, 5): 11}   # tuples can be keys!
# Tuples are also immutable; possible tests are whether tuples support item assignment (see above), and perhaps the lack of an append method...

# 13.19b
# Not correct; although items are tuples, this does not show that tuples are hashable; it is not the items,
# but the dictionary KEYS that need to be immutable.

# 13.20
# my_dict2 = {(1, [2, 3]): 3}     # TypeError: unhashable type: list

# 13.21
print('13.21')
print(i**2 for i in range(10))    # Doesn't work.
print((i**2 for i in range(10)))    # Doesn't work either.
print(tuple(i**2 for i in range(10)))    # Finally! This is because parentheses don't define a tuple; it's commas that do.

# 13.22
# form your own expectation, reviewing the earlier list comprehension exercises if needed.
new_dict = {key: value for key, value in name_to_id.items() if key[0].lower() in 'aeiou'}
print(new_dict)

# 13.23
even_name_to_id = {key: value for key, value in name_to_id.items() if len(key) % 2 == 0}
print(even_name_to_id)

# 13.24
print('\n13.24')
print({name: len(name) for name in name_to_id}) # map all names to their length
print({i: i**2 for i in range(10)}) # map each number from 0 to 9 to its square
print({name: name[::-1] for name in name_to_id.keys()}) # map each name from the original keys to its inverse
print({key: value for key, value in name_to_id.items() if int(value) % 2 == 0}) # take all items for
                                                                        # which the student id is an even number.

# 13.25
id_to_name = {value: key for key, value in name_to_id.items()}
print(id_to_name)

# 13.26
print('\n13.26')
numerals = ['zero', 'one', 'two', 'three', 'four', 'five']
numerals_to_numbers = {numerals[i]: i for i in range(len(numerals))}
numbers_to_numerals = {i: numerals[i] for i in range(len(numerals))}
print(numerals_to_numbers)
print(numbers_to_numerals)

# 13.27
import text_utils       # normally would be at the top of your file

text = '''The following table summarizes the operator precedence in Python, from highest precedence (most binding) to lowest precedence (least binding). 
Operators in the same box have the same precedence. Unless the syntax is explicitly given, operators are binary. 
Operators in the same box group left to right (except for exponentiation, which groups from right to left).'''

tokens = text_utils.tokenize(text)
trigrams = text_utils.ngrams(text, 3)

print(tokens)
print(trigrams)

# 13.28
print('13.28', flush=True)
def count_tokens(tokens):
    """
    Returns a dictionary with the number of occurrences of each token type in a list of strings (e.g., tokenized text).
    """
    counts = {tok: 0 for tok in tokens}
    for tok in tokens:
        counts[tok] += 1
    return counts

print(count_tokens(tokens))

# 13.29
print('13.29')
# print(count_tokens(trigrams))   # unhashable type: list

# The following does work, since strings are hashable:
print(count_tokens(text_utils.ngrams(text, 3, as_strings=True)))

# This would also work, i.e., converting every list (ngram) to a tuple, since tuples are hashable:
print(count_tokens([tuple(t) for t in trigrams]))

# You can also change the text_utils.ngrams function to return a list of tuples by default.


# 13.30
print('13.30')
# Can you convert an ordinary list to a dictionary? A string?
# dict([1, 2, 3, 4])  # nope.
# dict('ab')  # nope.

# List of pairs:
print(dict([(1, 2), (3, 4)]))   # yes!

# What about a list of lists, where each inner list has two elements?
print(dict([[1, 2], [3, 4]]))   # yes!

# What if one of the inner lists has only one element, or three?
# print(dict([[1, 2], [3, 4, 5]]))   # nope!

#  What about a list of two-character strings?
print(dict(['ab', 'cd', 'ef']))   # yes!

# 13.31
# You might expect converting a dictionary to a list to collect only the keys, and you'd be right. Hence, converting
# a dict to a list and back again does not return you to where you began.


# 13.32 and beyond: Mini-adventure, up to you!