"""
19. Some additional useful built-ins
"""

# 19.1
print('19.1')
names = ['John', 'Sue', 'Bob', 'Chris']
# for i in range(len(names)):   # old version
#     print(names[i])
for name in names:
    print(name)

# 19.2
print('19.2')
set_of_names = set(names)
# set_of_names[2]
# indexing no longer supported; but iteration still works:
for name in names:
    print(name)

# 19.3
print('19.3')
# In part subjective, but: indices are a potential source of error (IndexError).
# Indexing has us worry about things like: Is the upper bound of a range-like
# object exclusive or inclusive (different libraries vary in this regard)?
# Should we loop until the length of the list, or the length minus 1? And if
# we loop over consecutive pairs of elements (e.g., bigrams in a tokenized
# text), should we loop until length minus 1, or even minus 2? -- Even though
# you can probably answer these questions (let that be an exercise here), the
# problem is that it increases cognitive load while reading or writing code.

# 19.4
print('19.4')
ids = ['123', '456', '789', '890']
for i in range(min(len(ids), len(names))):  # min, for safety :)
    print(ids[i], names[i])

# 19.5
print('19.5')
# Up to you: do you see the resemblance?
# Regardless, that's what it's called:

# help(zip)
for id, name in zip(ids, names):
    print(id, name)

# 19.6
print('19.6')
for a in zip(ids, names):
    print(a)    # tuple is not unpacked, unlike before.


# 19.7
print('19.7')
for id, name in zip(ids, names[:2]):
    print(id, name)

# 19.8
print('19.8')
print(type(zip(ids, names)))
print(zip(ids, names))

# 19.9
print('19.9')
print(list(zip(ids, names)))
# Remember how dict applied to a list of pairs uses the elements as keys and values?

print(dict(zip(ids, names)))

# 19.10
print('19.10')
# Yes!
for t in zip(ids, names, ids, names):
    print(t)

# 19.11
print('19.11')
places = ['Amsterdam', 'Rotterdam', 'Den Haag']
counts = [905234, 656050, 552995]

place_to_count = dict(zip(places, counts))
print(place_to_count)

# 19.12
print('19.12')
# Remember to formulate your own prediction first!
print(list(zip(names, names)))
print(list(zip(names, names[1:])))

# 19.13
print('19.13')
s = 'abcdef'

# Predict the outcomes before you run this:
print(list(zip(s, s[:-1])))
print(list(zip(s[1:], s)))
print(list(zip(s[:-1], s)))
print(list(zip(s, s[::-1])))
print(list(zip(s, s[1:], s[2:])))

# 19.14
print('19.14')
target = [('a', 'b'), ('c', 'd'), ('e', 'f')]
attempt = list(zip(s[::2], s[1::2]))
print(target == attempt)

# 19.15
print('19.15')
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]

result = []
for e1 in l1:
    for e2 in l2:
        result.append((l1, l2))

# print(result == list(zip(l1, l2)))    # Make a prediction first!

# 19.16
print('19.16')
for i, name in enumerate(names):
    print(i, name)

# 19.17
print('19.17')
for i in enumerate(names):
    print(i, name)    # i is now an index-name pair (name still has a value assigned from earlier)!

# for i, name in names:  # error!
#     print(i, name)

# 19.18
print('19.18')

# This highlights that the enumerated 'indices' are not 'part of'
# the original iterable (sets don't support indexing), unlike keys
# of a dictionary. Rather, enumerate *counts* the elements given to it,
# independently of any indices in the original datastructure.

for i, char in enumerate({'a', 'b', 'c', 'd', 'e'}):
    print(i, char)

# 19.19
print('19.19')

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for x, y in enumerate(my_dict):
    print(x, y) # pairs of a count + key
for x, y in enumerate(my_dict.items()):
    print(x, y) # pairs of a count + key-value pair

# 19.20
# Formulate your expectation!
# list(range(10))
# list(10)
# enumerate(10)
# enumerate(range(10))
# range(enumerate(10))
# enumerate(list(range(10))

# 19.21
print('19.21')
results = [
    list(enumerate('abcd')),
    list(zip(range(4), 'abcd')),
    list(enumerate(range(5))),
    list(zip(range(5), range(10))),
    list(zip(range(10), range(5))),
    list(enumerate(enumerate(enumerate(range(5))))),
    list(zip(range(5))),
    ]
for result in results:
    print(result)

# 19.22
print('19.22')
# Formulate your own prediction first!
results = [
    all([True, True, True]),
    any([True, True, True]),
    all([True, False, True]),
    any([True, False, True]),
    all([False, False, False]),
    any([False, False, False]),
    any([]),
    all([]),
]
for result in results:
    print(result)

# 19.23
print('19.23')
booleans = [True, False, True]

print(not any(booleans) == all(not b for b in booleans))
print(any(booleans) == (not all(not b for b in booleans)))

# This may remind you of the equivalences in predicate logic (if you encountered
# this before): some == not all not,  not some == all not

# 19.24
print('19.24')

words = 'The quick brown fox jumped over the lazy dog'.split()

print(any(len(word) >= 3 for word in words))    # whether any word has length >= 3 (yes).
print(all(len(word) < 10 for word in words))
print(any(word[0].lower() in 'aeiou' for word in words))

# 19.25
print('19.25')

print(not any('t' in word for word in words))
print(any('t' in word for word in words))
print(all('t' in word for word in words))

# 19.26
print('19.26')

print(sum([1, 2, 3, 4, 5]))
# print(sum(['a', 'b', 'c'))  # nope.

print(sum([True, True, False])) # yep!

# 19.27
print('19.27')
print(sum(len(w) >= 3 for w in words))
print(sum(w[-1].lower() in 'aeiou' for w in words) >= 3)

# 19.28
print('19.28')

print(len([w for w in words if len(w) >= 3]))   # note the need for square brackets...
print(len([w for w in words if w[-1].lower() in 'aeiou']) >= 3)

# Very subjective, but the latter are probably a bit closer to how you
# would describe, in plain English, a manual approach to these kinds of problems.

# 19.29
# sum-based: create a list of booleans based on the original list, then count
#    the 'True' values.
# len-based: create a sublist of the original list based on a condition,
#    then count the number of remaining elements.

# 19.30
print('19.30')

print(sum(x for x in [1, 2, 3, 4]))
# print(len(x for x in [1, 2, 3, 4]))    # error!
print(len([x for x in [1, 2, 3, 4]]))   # fine!

# 19.31
print('19.31')

words = 'asdkjh qwlkj ekljsd alksj lkjf'.split()

print(any(w[0].lower() in 'aeiou' for w in words))  # does any word start with a vowel?
print(all(w[0].lower() in 'aeiou' for w in words))  # do all words start with a vowel?
print(not any(w[0].lower() in 'aeiou' for w in words)) # does no word start with a vowel?
print(all(w[0].lower() not in 'aeiou' for w in words)) # equivalent: do all words not start with a vowel
print(sum(w[0].lower() in 'aeiou' for w in words) >= 2) # do at least 2 words start with a vowel?
print(len([w for w in words if w[0].lower() in 'aeiou']) >= 2) # equivalent
print(not any(w[0].lower() not in 'aeiou' for w in words)) # does no word NOT start with a vowel, i.e., do all words? (equivalent to second)

# 19.32
print('19.32')

def has_any_odd(numbers):
    return any(n % 2 == 1 for n in numbers)

def has_only_odd(numbers):
    return all(n % 2 == 0 for n in numbers)

def has_three_odd(numbers):
    return len([n for n in numbers if n % 2 == 1]) == 3

print('Odd/even stuff:')
print(has_any_odd([1, 3, 5]))
print(has_any_odd([2, 4, 6]))
print(has_any_odd([2, 4, 5]))
print(has_only_odd([1, 2, 3]))
print(has_only_odd([1, 3, 5]))
print(has_three_odd([1, 2, 3, 4, 5]))
print(has_three_odd([1, 2, 3, 4]))
print(has_three_odd([1, 2, 3, 4, 5, 7]))

def has_at_most_n_vowels(s, n):
    return len([c for c in s.lower() if c in 'aeiou']) <= n

print('Vowel stuff:')
print(has_at_most_n_vowels('aqwekljhadskjlaw', 3))
print(has_at_most_n_vowels('aqwekljhadskjlaw', 10))