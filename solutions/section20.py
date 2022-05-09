"""
20. Self-documenting code
"""

# 20.1
# Have a look.

# 20.2
print('20.2')
# Yes :) but the code runs fine.
def not_enough_newlines():
    print('Squiggle says: not enough space before the function definition.')


if(True):
    print('Squiggle says: remove redundant parentheses.')

print ('No whitespace before the function call\'s parentheses.')

# 20.3
# Form your own thoughts. A key component of an answer would be to relate
# code clarity and safety to the importance of REPRODUCIBILITY in science.
# Another key component is that code is read far more often than it is
# written, so clarity is simply a time-saver.
# Also, don't fall victim to thinking 'I'll still understand this
# in the morning', let alone 'a few weeks from now'.

# 20.4
print('20.4')
print('--------------------')
import this
print('--------------------')

# 20.5
# Up to you! Try to get at least to 10 keywords and 10 builtins (_excluding_ methods
# on classes like string, dict, list, lest it become too easy).

# 20.6
# In terms of purpose, triple-quotation-marked strings are specifically used for docstrings,
# explaining the purpose of functions. Hashtag comments can be used more loosely throughout the code.
# In terms of how they work: a key difference is that #-comments are genuinely comments only;
# they are ignored by Python. Triple-quotation-marked strings are not; they define ordinary
# string objects; it's just that they are assigned to a variable. Docstrings are still
# picked up by function definitions, e.g., they end up in the .__doc__ attribute.

# 20.7
print('20.7')
some_list1 = [
    'abc',
#    'def',
    'ghi',
    'jkl'
    ]

some_list2 = [
    'abc',
'''
    'def',
'''
    'ghi',
    'jkl'
    ]

print(some_list1)
print(some_list2) # In light of 20.6, explain where the mess comes from!

# 20.8
my_dict = {}   # create an empty dictionary
my_number = 5432   # assign integer to variable
# Both comments redundant, except for users completely unfamiliar with Python.

# 20.9
print('20.9')

# Misleading because it's a string, not int:
# n = input('Enter a number:')     # get an integer from the user
n = 10  # the above line commented out; annoying during testing
print(f'You entered {n}!')

# Misleading because it's not the list, but the contained strings that are inverted.
my_list = ['abc', 'def', 'ghi']
my_list2 = [s[::-1] for s in my_list]   # invert the list

my_dict = {'a': 15, 'b': 20, 'c': 25}

# Misleading because it prints character-number pairs, not only characters:
# print each character
for x in my_dict.items():
    print(x)

# 20.10
print('20.10')
import re
text = 'Imagine this is some kind of text. Could be a lot longer.'
# Tokenize by finding all alphanumeric characters in between word boundaries:
tokens = re.findall(r'\b\w+\b', text)
# Print the vocabulary size:
vocabulary = set(tokens)
print(len(vocabulary))
# Print the average token length of the text:  <-- No longer correct
average_length = sum([len(tok) for tok in vocabulary]) / len(vocabulary)
print(average_length)

# 20.11
inhabitant_counts = {}
# or, e.g., place_to_num_inhabitants

# 20.12
print('20.12')

name_to_id = {'John': '098124', 'Sue': '657317', 'Bob': '135809'}
id_to_name = {id: name for name, id in name_to_id.items()}
target_id = '657317'

if target_id in id_to_name:
    print(id_to_name[target_id])	# print the student's name

# The latter is not ideal, as it involves two dictionary lookups.
# The explicit 'dict.get' method solves this:
target_name = id_to_name.get(target_id, None)
if target_name:
    print(target_name)

# And later Python versions have a 'Walrus' operator to simplify this:
if target_name := id_to_name.get(target_id, None):
    print(target_name)
# But opinions differ about the readability/desirability of this shorthand...

# 20.13
print('20.13')
import math

circle_radii = [7, 4, 5, 8, 6, 9, 5]
for r in circle_radii:  # not changing r to 'radius', since r is so standard in maths.
    area = math.pi * r**2
    print(area)

# 20.14
print('20.14')
def circle_area(r):
    return math.pi * r**2

for r in circle_radii:  # not changing r to 'radius', since r is so standard in maths.
    print(circle_area(r))

# 20.15
# Brevity serves no real purpose, as modern editors have auto-complete anyway.
# Brevity hampers readability. (Though of course extremely long variable names
# are no good either.)
# Even if brevity had benefited coding speed (it doesn't really), code is read
# much more than it is written.
# Other considerations are possible too.

# 20.16
# It's best if you formulate your own answer here.
# Regarding the last sub-question: uninformative variable names can be acceptable if either 1. they
# are defined and then used in a single line, or 2. they are standard idioms (e.g., r for radius).

# 20.17
print('20.17')

project_topics = ['sentiment analysis', 'zipf\'s law', 'collocations', 'distributional semantics']
students = ['Alf', 'Beth', 'Gemma', 'Dale', 'Ebba', 'Zod', 'Ethan', 'Philip']
team_size = len(project_topics) / len(students)
print(f'{team_size} students will work together on each project')

# 20.18 and 20.20
print('20.18 and 20.20')

MAX_N_CHARS = 500

with open('../adventures/data/gutenberg/alice_pg35688.txt', 'r') as file:
    text = file.read()

if MAX_N_CHARS:
    text = text[:MAX_N_CHARS]

# Don't forget to delete the redundant comment :)

# 20.19
# Similar to 'separation of concerns' in the discussion of functions.
# Modularity is good, keeps code testable, clear.
# You don't want to accidentally change the main program when all you wanted
# to do was change a configuration setting.
# You may want to save a particular configuration for later, or share it
# with a friend, and that should not require a copy of the (potentially large)
# whole program.

# 20.20
# A 'cheap' way to sort-of achieve it would be to at least put all configuration
# settings as variables at the top of your file, recognizably in all-caps.
# A much better way would be to store them in a separate file, like `config.py`,
# that you can then import to access the settings, or even a non-python file
# that you open(...) and parse to obtain the settings.

# 20.21
# Yes, magic numbers are not self-documenting (or not in a self-documenting context).
# Both pi and 2 are numbers that, given the context of computing the area
# of a circle, could not reasonably have been chosen differently, so they arguably
# aren't 'magic numbers' (though the ad-hoc rounding 3.1415 perhaps would be).
# Of course this could change (for the 2, at least) in the context of code dealing
# with, say, n-dimensional generalizations of circles (spheres, hyperspheres...).

# 20.22
# In your answer, consider things like mutability, order, support for indexing, duplicates, mapping.

# 20.23
print('20.23')

TARGET_NAME = 'Bob'  # placed at the top as 'cheap' way of separation of concerns

names = ['John', 'Sue', 'Bob', 'Chris']
ids = ['124987', '098513', '098122', '198732']

name_to_id = dict(zip(names, ids))
target_id = name_to_id[TARGET_NAME]
print(target_id)

# 20.24
print('20.24')

TARGET_NAME = 'Bob'

# student records consist of the fields name, age, id and major:
students = [
    ['John', 22, '1249871', 'linguistics'],
    ['Mary', 24, '4198712', 'psychology'],
    ['Bob', 32, '089123', 'mathematics'],
]

students_dict = [dict(zip(['name', 'age', 'id', 'major'], student))
                 for student in students]

print(students_dict)    # Look, it documents itself :)

for student in students_dict:
    if student['name'] == TARGET_NAME:
        print(student['id'])

# A relevant consideration here is that there may be multiple students with the same names.

# Alternatively a pandas dataframe, though it's a bit overkill:
# import pandas as pd
# students = pd.DataFrame(students, columns=['name', 'age', 'id', 'major']).set_index('name')
# print(students.loc['Bob', 'id'])

# 20.25
print('20.25')

NEW_NUMBER = 8      # magic number placed at the top

unique_numbers = {1, 6, 3, 2, 5, 7, 9}      # spaces added, for PEP8

unique_numbers.add(NEW_NUMBER)      # uniqueness taken care of by set :)

# 20.26
print('20.26')

EXAM_POINTS_TOTAL = 100
EXAM_POINTS_BONUS = 5
EXAM_PASSING_GRADE = 5.5
EXAM_MAX_GRADE = 10

# Two co-indexed lists is not ideal, but we're building so many new lists below that
# a dictionary mapping wouldn't be the most convenient here either. I think this might
# be a job for pandas instead. But let's proceed without.

students = ['John', 'Sue', 'Bob', 'Chris', 'Peter', 'Pjotr', 'Maria']
points_earned = [80, 60, 43, 75, 27, 92, 94]

# Consider encapsulating the following in one or more functions. Not least because
# you may want to compute other grades in one go.

points_for_max_grade = EXAM_POINTS_TOTAL - EXAM_POINTS_BONUS
grades = [points_earned / points_for_max_grade * EXAM_MAX_GRADE
          for points_earned in points_earned]
passfails = [grade > EXAM_PASSING_GRADE for grade in grades]
failed_by = [name
             for passed, name in zip(passfails, students)
             if not passed]

print('Exam grades:', list(zip(students, grades))) # some rounding would be nice...
print(f'Students who failed: {", ".join(failed_by)} (total: {len(failed_by)}')

# 20.27
# Up to you!
