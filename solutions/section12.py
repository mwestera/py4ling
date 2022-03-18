"""
12. Dictionary basics
"""

# 12.1
name_to_id = {'Alf': '136124', 'Beth': '008623', 'Chris': '014212', 'Dave': '9123785', 'Esra': '978123'}
print(name_to_id)
print(type(name_to_id))

# 12.2
print(name_to_id['Alf'])
print(name_to_id['Chris'])

# 12.3
# name_to_id['Bobby']    # KeyError: 'Bobby'
# name_to_id[Alf]         # NameError: Name 'Alf' is not defined
#   Explanation: without the quotation marks it's looking for a variable with that name, instead
#   of treating it as a string. This is not specific to dictionaries of course.

# 12.4
print(len(name_to_id))
empty_dict = {}
print('Double check:', type(empty_dict))     # yes :)

# 12.5
print('12.5')
print('Value in dict?', '136124' in name_to_id)   # nope, not values.
print('Key in dict?', 'Alf' in name_to_id)   # yes, checks keys.

# 12.6
# name_to_id[2]    # KeyError: 2, so nope!

# 12.7
dict_with_integers = {1: 'hi', 2: 'hello', 3: 'bye', 4: 'tata'}
print(dict_with_integers[2])    # this works now, but better say 'key', not 'index', to avoid confusion.

# 12.8
# my_dict = {'Alf' = '36124', 'Beth' = '008623'}  # Invalid syntax.
# This typo is easy to make, because associating values with keys is quite similar to assigning values to variables.

# 12.9
age_to_count = {20: 4, 21: 6, 22: 8, 23: 5, 26: 3}
word_counts = {'the': 100, 'student': 13, 'studies': 3, 'laughs': 5} # completely imaginary counts; it's a weird corpus
course_to_students = {'syntax': ['Alf', 'Beth', 'Gemma'], 'semantics': ['Dale', 'Ebba']}
# list_to_average = {[1, 2, 3]: 2, [3, 4, 5]: 4}  # TypeError: list is an unhashable type; because it is mutable.
#   Dictionary keys need to be hashable.

# 12.10
test_dict = {1: 'a', 'b': 3.6, 'c': [1, 2, 3], 123: 125}    # yes, all fine!

# 12.11
# Nope, dictionaries don't support slicing.
# print(name_to_id['Alf':'Dave']) # TypeError: unhashable type: 'slice'
# print(dict_with_integers[2:4]) # TypeError: unhashable type: 'slice'

# What the above error shows, indirectly, is that Python isn't attempting to retrieve individual keys from the slice
# (because those would be hashable). Rather, it attempts look up the entire slice object as a key (which it cannot,
# because it is not 'hashable'). The short answer is: dictionaries don't support slicing.

# 12.12
# name_to_id['alf']   # KeyError, because dictionary is case-sensitive, as are most/all operations in Python.

# 12.13
name_to_id['Suzy'] = '124987'       # adds Suzy with her ID to the dictionary
name_to_id['Alf'] = '999999'        # replaces the ID of Alf that was already there
print(name_to_id)

some_dict = {1: 3, 3: 5, 1: 5}
print(some_dict)
# apparently later occurrences of a key in a dictionary definition override earlier occurrences.
# Note that PyCharm (in the editor) gives a warning about the duplicate keys, but Python runs fine.

# 12.14
print('12.14')
del name_to_id['Esra']  # deletes the key-value pair with key 'Esra'.
print(name_to_id)

names = ['Alf', 'Beth', 'Gemma']
del names[1]
print(names)    # yes, works on lists too!

name = 'Alf'
# del name[1]     # doesn't work on strings, because it is immutable.

# 12.15
name_to_id['Chris'] = '5987162'
del name_to_id['Suzy']
print(name_to_id)

# 12.16
x = 5
print(x)

globals()['y'] = 10
print(y)
# This shows that plain variable assignment is a shortcut for assigning a value to a key in the globals dictionary
# or (if you're inside a function) the locals dictionary.

# 12.17
# PyCharm relies on a more shallow parsing for the warnings it shows, auto-completion, and various other helpful
# programming tools. The reason for this shallow parsing is that it would be very inefficient if while you're coding,
# PyCharm is constantly, in the background, telling Python to interpret your code. (More so with larger programs,
# of course, that may do a lot more than merely assign and print some variables.)


############## Mini-adventure ######################

# 12.18
# Ok.

# 12.19
vocabulary = [
    {'word': 'walk', 'category': 'verb', 'frame': 'intransitive'},
    {'word': 'see', 'category': 'verb', 'frame': 'transitive'},
    {'word': 'student', 'category': 'noun'},
    {'word': 'the', 'category': 'det'},
    {'word': 'a(n)', 'category': 'det'},
]
# up to you to add more words!

# 12.20
import random   # you'd normally put this at the top of your file
det = random.choice([word for word in vocabulary if word['category'] == 'det'])
noun = random.choice([word for word in vocabulary if word['category'] == 'noun'])
verb = random.choice([word for word in vocabulary if word['category'] == 'verb' and word['frame'] == 'intransitive'])

print(f'{det["word"]} {noun["word"]} {verb["word"]}s')


# Solutions for remaining exercises of this adventure are omitted, lest it would not be as adventurous! Good luck!
