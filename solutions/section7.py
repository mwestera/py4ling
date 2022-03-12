"""
7. Lists (list, append, [])
NOTE: I've separated all solutions per section into different files, after all.
Seems more convenient that way, easier to search...
"""


names = ['Alf', 'Beth', 'Chris', 'Dave', 'Esra']

# 7.11
print('Alf' in names)
print('Alwyn' in names)
print('Alwyn' not in names)

# 7.13
names[-1] = 'Suzy'
names[0] = 'Bob'

# names[len(names)] = 'Test'  # nope!

# 7.14
names.append('Matt')
names.append('Mary')
print(len(names))

# 7.15
my_list = []
my_list.append('a')
my_list.append(10)
print(my_list)

# 7.16
my_list.append('a')
print(my_list)
print([1, 2, 3, 3, 3, 4, 5, 3, 3, 4, 5, 6, 7, 8])
# Nothing spectacular happens; lists can contain duplicates

# 7.17
# The int and string variables are changed by reassigning something to it; but the variable list1 is never re-assigned; something is appended to the list, changing the list itself.
# Because variables are re-assigned independently (see section 2), only in the latter case does list2 update along with list1, because they reference the same object that is being changed.

# 7.18
my_string = 'abcde'
# my_string[3] = 'x'  # Nope! Strings are immutable.

# 7.19
# my_string.append('y') # Nope, and for the same reason.

# 7.20
# In the code from the exercise, x is being reassigned a new string (created by .upper()), so it does NOT show that strings are mutable (because they aren't).

# 7.21
my_list2 = my_list[:]
my_list2[2] = 'xxxxx'
print(my_list, my_list2)    # this shows that [:] creates a NEW list containing the same old elements.

# 7.22
row = [''] * 3
board = [row] * 3

def print_board(board):
    """
    Prints a 3x3 board in a more readable way, by printing each row of the board
    on a separate line. Also some horizontal lines.
    """
    print('  -----------')
    print(board[0])
    print(board[1])
    print(board[2])
    print('  -----------')

print_board(board)
board[1][1] = 'x'
print_board(board)  # the outer list refers to the same 'row' list three times, and modifying it
                    # will change all three occurrences.

# better_board = [[''] * 3, [''] * 3, [''] * 3]   # repetition to be avoided
better_board = [[''] * 3 for _ in range(3)] # list comprehension syntax for: create a (new) row three times
better_board[1][1] = 'x'
print_board(better_board)   # Now I can no longer cheat

# 7.23, 7.24
def swap_first_and_last(l, inplace):
    """
    Swaps first and last element of a list (or string), depending on the 'inplace' parameter either in-place (not returning anything)
    or creating (and returning) a new object.
    """
    if inplace:
        # the following works, but isn't super readable
        # first = l[0]
        # last = l[-1]
        # l[-1] = first
        # l[0] = last
        # more Pythonic, involving creating (on the right) and unpacking (into the left) of a 'tuple' (later section):
        l[0], l[-1] = l[-1], l[0]
        # no return statement necessary, as l is modified in place; no new object is created.
    else:
        # the following works, but isn't super safe, e.g., error if there's only one element.
        # return [l[-1]] + l[1:-1] + [l[0]]
        copy = l[:]
        copy[0], copy[-1] = copy[-1], copy[0]
        return copy

# Note that we can avoid some repetition (= good!) as follows:
def swap_first_and_last2(l, inplace):
    if not inplace:
        l = l[:]
    l[0], l[-1] = l[-1], l[0]
    if not inplace:
        return l


my_list = [1, 2, 3, 4, 5]
print(my_list)

swap_first_and_last(my_list, False)
print(my_list)  # not changed; because it wasn't changed in-place

my_list = [1, 2, 3, 4, 5]
my_list = swap_first_and_last(my_list, False)
print(my_list)  # yep, now it's changed

my_list = [1, 2, 3, 4, 5]
swap_first_and_last(my_list, True)
print(my_list)  # this works too; changed in place (i.e., it's still the same list object, but reordered)

my_list = [1, 2, 3, 4, 5]
my_new_list = swap_first_and_last(my_list, True)
print(my_new_list)  # Nope, nothing was returned.

# 7.25, 7.26, 7.27
day_names = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
def day_number_to_name(daynumber):
    """
    Translates a number from 1 to 7 into a day name.
    """
    daynumber -= 1  # fix for our annoying client
    return day_names[daynumber % 7]

print(day_number_to_name(0), day_number_to_name(1), day_number_to_name(3), day_number_to_name(7))
# answer to 7.27: while the list approach is more readable, for this particular fix it doesn't matter much;
# the daynumber -= 1 tweak could be made either way.

# 7.28
def print_return_day_name(start_day_number, duration_n_nights):
    """
    If you leave on start_day_number, and stay for duration_n_nights, on what day (name) wil you return?
    """
    return_day_number = (start_day_number + duration_n_nights) % 7
    return_day_name = day_number_to_name(return_day_number)
    print('Return day:', return_day_name)

print_return_day_name(3, 137)

# 7.29
# similar, e.g., slicing, len, concatenation.
# different, e.g., mutability (e.g., assignment to index, append), elements of a string are #
# themselves strings while lists are more flexible.

# 7.30
# Note that one object is a list, and the other object is a string that looks like a list.

# 7.31
# Converting a string to a list, results in a list of all its single character strings.
# Converting a list back to a string does revert the aforementioned change; rather the result is a string
# matching what it looks like if you were to print a list. (And this makes sense; while one could in principle
# 'convert' a list of strings back to a string by concatenating all characters, this would only work in case
# list elements were themselves strings. Since converting a list to a string ought to work for any sort of list,
# not just lists of strings, that is not how it is defined.

# 7.32
# Python permits this; PyCharm will issue a warning (squiggle underneath the variable name).
# it is dangerous to change the meaning of things that everyone assumes they know the meaning of.

# 7.33
def swapped_list_by_indices(l, i, j):
    """
    Creates a modified copy (i.e., not in-place) of the list l with elements at indices i and j swapped.
    """
    # With some assumptions, e.g., i < j and both are positive, the following works correctly in many cases:
    # return l[:i] + [l[j]] + l[i+1:j] + [l[i]] + l[j+1:]
    # But the following is a lot safer and more readable:
    copy = l[:] # create a copy, let's not modify in-place
    copy[i], copy[j] = copy[j], copy[i]     # using a tuple, see also 7.23
    return copy

print(swapped_list_by_indices([1, 2, 3, 4], 1, 2))
print(swapped_list_by_indices([1, 2, 3, 4], 2, 1)) # takes i,j in any order
print(swapped_list_by_indices([1, 2, 3, 4], 1, -1))    # even works on negative indices
print(swapped_list_by_indices([1, 2, 3, 4], 1, 1))    # extreme case, also works
# print(swapped_list_by_indices([], 2, 2))    # I'd expect an error here, which indeed we get.

# 7.34
# For a string, assigning to indices doesn't work, so you would need the commented-out variant in 7.33 above.
# A preferable variant might be to convert to list and back to string, like a 'wrapper' around the above function:
def swapped_str_by_indices(s, i, j):
    """
    Swaps two characters (by indices) in a string s, returning the new string.
    """
    swapped_list = swapped_list_by_indices(list(s), i, j)
    swapped_str = ''.join(swapped_list) # we learn about the join function later
    return swapped_str

print(swapped_str_by_indices('test', 1, 2))

# 7.35
# construct these lists outside the function for efficiency, in case the function will be called
# a million times in a big corpus.
determiners = ['the', 'a', 'an', 'many', 'some']
lowercased_determiners = [det.lower() for det in determiners]   # just in case our dictionary is not uniform

def is_determiner(word):
    """
    Checks if the word is a determiner, by comparing against a predefined list. Not case-sensitive.
    """
    return word.lower() in lowercased_determiners

print(is_determiner('the'))
print(is_determiner('there'))
print(is_determiner('the man'))
print(is_determiner('The'))

# 7.36, 7.37
import random   # imports are normally put at the top of the file

nouns = ['tree', 'house', 'person', 'teacher']
intransitive_verbs = ['fall', 'sing']
transitive_verbs = ['hit', 'kiss']

def generate_sentence():
    """
    Generate and return a single random sentence.
    """
    noun = random.choice(nouns)
    determiner = random.choice(determiners)
    verb_frame = random.choice(['transitive', 'intransitive'])
    if verb_frame == 'transitive':
        verb = random.choice(transitive_verbs)
        determiner2 = random.choice(determiners)
        noun2 = random.choice(nouns)
        sentence = f'{determiner} {noun} {verb}s {determiner2} {noun2}'
    else:
        verb = random.choice(intransitive_verbs)
        sentence = f'{determiner} {noun} {verb}s'   # using a format string, note the little 'f'
    return sentence

print(generate_sentence())
print(generate_sentence())
print(generate_sentence())
print(generate_sentence())
print(generate_sentence())
print(generate_sentence())
