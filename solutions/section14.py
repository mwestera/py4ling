"""
14. Breaking out of loops
"""

# 14.1
# See, e.g., exercises 8.18, 8.19.

# 14.2
print('14.2')

def has_any_odd_INCORRECT(numbers):   # Note: The docstring is a lie.
    """
    Returns True if the list of numbers has any odd number; False otherwise.
    """
    for number in numbers:
        if number % 2 == 1:
            return True
        else:
            return False    # this returns too early

print(has_any_odd_INCORRECT([1, 2, 3, 4]))    # works
print(has_any_odd_INCORRECT([2, 4, 6, 8]))    # works
print(has_any_odd_INCORRECT([2, 3, 4, 5]))    # fails!

print('14.2 fixed')

def has_any_odd(numbers):
    """
    Returns True if the list of numbers has any odd number; False otherwise.
    """
    for number in numbers:
        if number % 2 == 1:
            return True
    return False

print(has_any_odd([1, 2, 3, 4]))    # works
print(has_any_odd([2, 4, 6, 8]))    # works
print(has_any_odd([2, 3, 4, 5]))    # now it works!


# 14.3
print('14.3')
def has_any_vowel(string):
    """
    Returns true if the list contains any vowel.
    """
    for char in string:
        if char.lower() in 'aeiou':
            return True
    return False

print(has_any_vowel('asdj'))
print(has_any_vowel('jkdfsaasd'))
print(has_any_vowel('jkdfssd'))


# 14.4
print('14.4')
def has_only_odd(numbers):
    """
    Returns True if the list of numbers has only odd numbers.
    """
    for num in numbers:
        if num % 2 == 0:
            return False
    return True

print(has_only_odd([1,3,5,7]))
print(has_only_odd([1,3,5,7,8]))

# 14.5
print('14.5')
def has_three_odd(numbers):
    """
    Returns true if there are three or more odd numbers in the list.
    """
    n_odd = 0
    for num in numbers:
        if num % 2 != 0:
            n_odd += 1
        # In this case I feel the early return statement doesn't make the code more readable.
        # But if the list has millions of numbers, it's worth the efficiency gain.
        if n_odd >= 3:
            return True
    return False

print(has_three_odd([1,3,5,7]))
print(has_three_odd([1,3,5,8]))
print(has_three_odd([1,3,4,8]))

# 14.6
print('14.6')
def has_at_most_n_vowels(strings, n):
    """
    Returns False if the list of strings contains more than n vowels.
    """
    n_vowels = 0
    for string in strings:
        for character in string:
            if character.lower() in 'aeiou':
                n_vowels += 1
            if n_vowels > n:
                return False
    return True

print(has_at_most_n_vowels(['abc', 'def', 'eoi'], 3))
print(has_at_most_n_vowels(['abc', 'def', 'eoi'], 10))

# 14.7
print('\n14.7')
names = ['Alf', 'Beth', 'Chris', 'Dave', 'Esra']

for name in names:
    print('Checking:', name)
    if name[0].lower() not in 'aeiou':
        print('Got one!')       # Beth is the first consonant person, and the only printed name
        break

# 14.8
print('\n14.8')
for name in names:
    print(name)
    break       # prints just the first name, breaks right away

# 14.9
print('14.9')
for name in names:
    break
    print(name)     # never reached!

# 14.10
print('\n14.10')
for name in names:
    if len(name) > 4:
        break
    print(name)

# 14.11, 14.12
print('\n14.11')
def print_until_vowel(strings, inclusive=True):
    for s in strings:
        if s[0].lower() in 'aeiou':
            if inclusive:
                print(s)
            break
        print(s)
    print('Done!')      # A return statement instead of break, would also result in skipping the last print statement.

print_until_vowel(['askj', 'lkjqwe'])
print()
print_until_vowel(['lkjqwe', 'askj'])
print_until_vowel(['lkjqwe', 'askj'], inclusive=False)

# 14.13
print('\n14.13')
for i in range(10):
    for j in range(10):
        if i + j > 10:
            print('breaking here!')
            break
        print(i, j)

# 14.14
# break     # SyntaxError: 'break' outside loop

# 14.15
print('14.15')
def print_whether_has_any_odd(numbers): # fixed it!
    """
    Prints whether or not the list contains an odd number, and 'Done!' afterwards.
    """
    has_odd = False
    for number in numbers:
        if number % 2 == 1:
            has_odd = True      # keeping this little 'flag' variable is one way of handling it.
            break
    if has_odd:
        print('It has an odd number!')
    else:
        print('Zero odd numbers here!')
    print('   ...really!')    # this final command is mainly why we use break to escape the loop, not return


print_whether_has_any_odd([1, 3, 5, 7])
print_whether_has_any_odd([2, 4, 6, 8])
print_whether_has_any_odd([2, 4, 6, 8, 9])  # this was wrong, now it's fixed


# 14.16
print('14.16')
def print_whether_has_any_odd_2(numbers):
    for number in numbers:
        if number % 2 == 1:
            print('It has an odd number!')
            break
    else:                                   # note the indentation: the else belongs with for, not if.
        print('Zero odd numbers here!')
    print('   ...really!')

print_whether_has_any_odd_2([1, 3, 5, 7])
print_whether_has_any_odd_2([2, 4, 6, 8])
print_whether_has_any_odd_2([2, 4, 6, 8, 9])

# 14.17
print('\n14.17')
for name in names:
    if name[0] == 'D':
        break
    print(name)
    if name[1] == 'e':
        break
# Whichever 'break' statement is encountered first, that will exit the loop, and the other will never be reached.
# A possible use-case would be where the loop needs to be exited in several conditions, and those conditions
# cannot easily be evaluated all at once (using boolean 'or'). E.g., if one if-condition is at the start of the loop
# and the other at the end, they cannot be easily merged into a single if-clause, hence each would need their own break
# statement.

# 14.18, 14.19
print('14.18')
def some_has_some_odd(lists):
    for numbers in lists:
        for num in numbers:
            if num % 2 != 0:
                return True
    return False


def some_has_only_odd(lists):
    for numbers in lists:
        has_even = False
        for num in numbers:
            if num % 2 == 0:
                has_even = True
                break
        if not has_even:
            return True
    return False


def each_has_some_odd(lists):
    for numbers in lists:
        has_odd = False
        for num in numbers:
            if num % 2 != 0:
                has_odd = True
                break
        if not has_odd:
            return False
    return True


def each_has_only_odd(lists):
    for numbers in lists:
        has_even = False
        for num in numbers:
            if num % 2 == 0:
                has_even = True
                break
        if has_even:
            return False
    return True


def test_the_four_functions():
    # convenient testing code:
    list1 = [[1, 2], [3, 4]]
    list2 = [[2, 2], [3, 4]]
    list3 = [[2, 2], [4, 4]]
    list4 = [[1, 3], [5, 9]]
    list5 = [[1, 3], [4, 4]]

    for test_list in [list1, list2, list3, list4, list5]:
        print(test_list)
        for function in [some_has_some_odd, some_has_only_odd, each_has_some_odd, each_has_only_odd]:
            print(f' - {function.__name__}: {function(test_list)}')


test_the_four_functions()

# 14.20
print('\n14.20')

def some_has_some_odd(lists):   # I'm just overriding the above functions with the same name
    for numbers in lists:
        if has_any_odd(numbers):
            return True
    return False


def some_has_only_odd(lists):
    for numbers in lists:
        if has_only_odd(numbers):
            return True
    return False


def each_has_some_odd(lists):
    for numbers in lists:
        if not has_any_odd(numbers):
            return False
    return True


def each_has_only_odd(lists):
    for numbers in lists:
        if not has_only_odd(numbers):
            return False
    return True


test_the_four_functions()



# 14.21
# Prints all odd numbers that are not multiples of 5

# 14.22
for i in range(10):
    if i % 2 != 0 and i % 5 != 0:
        print(i)

# 14.23
# Verify your understanding.


# 14.24
print('14.24')

counter = 0
while counter < 10:
    print(counter)
    counter += 1

# 14.25
print('14.25')

for counter in range(10):
    print(counter)

# 14.26
# Try!

# 14.27
print('14.27')

# counter = 0
# while True:           # AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH!
#     print(counter)
#     counter += 1

# 14.28
def interactive_number_adder():
    total_sum = 0
    total_count = 0
    while True:
        s = input('Number pzl, or "done":')
        if s == 'done':
            break
        number = int(s)
        total_count += 1
        total_sum += number

    print(f'numbers entered: {total_count}, sum: {total_sum}, mean: {total_sum / total_count}')

# interactive_number_adder()

# 14.29, 14.30
import random

def number_guesser():
    target = random.randint(0, 100)
    n_guesses = 0
    while True:
        input_str = input('Guess! ')
        if not input_str.isnumeric():       # for 14.30
            continue

        guess = int(input_str)
        n_guesses += 1
        if guess == target:
            print(f'Congratulations! You won in {n_guesses} guesses!')
            break
        if guess > target:
            print(f'{guess} is too high!')
        else:
            print(f'{guess} is too low!')

# number_guesser()

# 14.31
print('14.31')

for i in range(3, 50, 5):
    print(i, end=',')

print()

for i in range(100, 5, -3):
    print(i, end=',')

# The 3 arguments of range have the same meaning as the three integers when slicing: start, end, step

# 14.32
print('\n14.32', flush=True)

def countdown():
    for i in range(10, 0, -1):
        print(i, end=',')
    print('liftoff!')

countdown()

# 14.33
print('14.33')
def countdown2(start=10, step=-1):
    for i in range(start, 0, step):
        print(i, end=',')
    print('liftoff!')

countdown2()
countdown2(20, -2)

# 14.34
print('14.34')
def print_odd_even_pairs():
    for i in range(1, 11, 2):
        for j in range(0, 11, 2):
            print(f'{i}-{j}', end=', ')
    print()

print_odd_even_pairs()

def print_odd_even_pairs_alternative():
    for i in range(11):
        for j in range(11):
            if i % 2 == 1 and j % 2 == 0:
                print(f'{i}-{j}', end=', ')
    print()

print_odd_even_pairs_alternative()

# 14.35
print('14.35')

def print_pairs():
    """
    Print all pairs (in range(11)) i-j where j is bigger than i.
    """
    for i in range(11):
        for j in range(i + 1, 11):  # notice the i
            print(f'{i}-{j}', end=', ')
    print()

print_pairs()

# 14.36
print('14.36', flush=True)
def even_elements(l):
    """
    Return a list containing all elements that occurred at even indices in the original list.
    """
    result = []
    for i in range(0, len(l), 2):
        result.append(l[i])
    return result

    # Or with list comprehension instead:
    # return [l[i] for i in range(0, len(l), 2)]

print(even_elements([1, 2, 3, 4, 5, 6]))


# 14.37
print('14.37')
def nonoverlapping_pairs(l):
    """
    Return a list with all non-overlapping pairs of consecutive elements from the original list.
    """
    pairs = []
    for i in range(0, len(l) - 1, 2):   # note the - 1
        pairs.append((l[i], l[i+1]))
    return pairs

def nonoverlapping_pairs2(l):   # same but with list comprehension
    return [(l[i], l[i+1]) for i in range(0, len(l) - 1, 2)]

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(nonoverlapping_pairs(test_list))
print(nonoverlapping_pairs2(test_list))


# 14.38
def nonoverlapping_tuples(l, n):
    """
    Return a list with all non-overlapping tuples of n consecutive elements from the original list.
    """
    tuples = []
    for i in range(0, len(l) - (n - 1), n):
        t = tuple(l[j] for j in range(i, i + n))
        tuples.append(t)
    return tuples
    # With a single list comprehension it becomes quite hard to read:
    # return [ for i in range(0, len(l) - (n - 1), n)]

print(nonoverlapping_tuples(test_list, 2))
print(nonoverlapping_tuples(test_list, 3))
print(nonoverlapping_tuples(test_list, 4))
print(nonoverlapping_tuples(test_list, 1))  # Just curious :)


# 14.39
print('\n14.39')
# range(0.1)  # nope
# range(0, 10, 0.2)  # nope
for i in range(10):
    print(i / 10, end=', ')
print("Easy peasy :)")


# 14.40
def clock(ndays):
    for i in range(24 * ndays):
        print(i % 24, end='|')
    print()

clock(5)

# 14.41
list(range(100))    # yep
# range([1, 2, 3])   # nope
# it makes sense that Python does not implement this, becasue a list is not in general guaranteed to
# correspond to a particular range with unique, ordered elements and constant step size.

# 14.42
# A range only stores the start, end and step size, whereas a list actually contains all elements.
# Hence, a list grows with the number of elements (and creating it takes processing time), whereas
# the size and processing time of a range does not depend on the number of elements that fit in it.

# 14.43
print('14.43', flush=True)
import sys

print(sys.getsizeof(range(9)), sys.getsizeof(range(9999)))  # same!
print(sys.getsizeof(list(range(9))), sys.getsizeof(list(range(9999))))  # massive difference!

# 14.44
character_map = {'0': ' ', '1': '#'}

def decode(message):
    for i in range(len(message)):
        if i % 8 == 0:
            print()
        print(character_map[message[i]], end='')
    print()

decode('0000000000110110011111110011111000011100000010000000000000000000')  # aww :)

# 14.45
import keyword
print('Keywords:', keyword.kwlist)
# + Reflect on the purpose of the various keywords you already know.

# 14.46
# break = 'hello' # SyntaxError: invalid syntax

# 14.47
# print = 'bla'
# print('apple')  # str is not callable! We stored a string in the 'print' variable.

# 14.48
print(__builtins__)
print('Builtins:', dir(__builtins__))
# + Reflect on the purpose of the various builtins you already know.