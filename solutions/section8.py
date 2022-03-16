"""
8. For-loops (for)
NOTE: I've separated all solutions per section into different files, after all.
Seems more convenient that way, easier to search...
"""


# 8.1
names = ['Alf', 'Beth', 'Chris', 'Dave', 'Esra']
for name in names:
    print(name)

# 8.2
# Yes, analogous to the initial exercises about if-clauses

# 8.3
print(name)  # it remains assigned to the last value assigned to it during the loop

# 8.4
print()
for name in names:
    print(name)
    print(name)

# Note how this is different:
print()
for name in names:
    print(name)
for name in names:
    print(name)
print()

# 8.5
name = 'Johnny'
for name in names:  # still works fine!
    print(name)


# 8.6, 8.8
def print_multiple(l, oneline):
    """
    Takes a list and a boolean oneline and prints all elements, either on one line or on separate lines.
    """
    if oneline:
        end = ''
    else:
        end = '\n'
    for element in l:
        print(element, end=end)
    if oneline:
        print()  # this is probably desirable


print_multiple(names, False)
print_multiple([1, 2, 3], True)
print_multiple([1, 2, 3], False)


# 8.7
def print_multiple_oneline(l):
    """
    Prints all elements of the list l on one line, concatenated by dashes.
    """
    for element in l[:-1]:
        print(element, end='-')
    print(l[-1])


print_multiple_oneline(names)


# 8.9
def sum_of_squares(numbers):
    """
    Computes and returns the sum of squares of the numbers in the list.
    """
    result = 0
    for number in numbers:
        result += number ** 2
    return result


print(sum_of_squares([2, 3, 4]))


# 8.10
def length(l):
    """
    'Manually' computes the length of the list l.
    """
    result = 0
    for element in l:  # more pythonic: for _ in l, because the element doesn't matter.
        result += 1
    return result


print(length([1, 2, 3, 4, 5, 6]))


# 8.11, 8.12
def concatenate(words, sep):
    """
    Returns a concatenation of a list of strings with seps in between
    NOTE: This function emulates the built-in string method 'join', e.g.,  '-'.join(words)  (read as: use '-' to join all words)
    """
    result = words[0]
    for word in words[1:]:
        result += sep + word
    return result


print(concatenate(names, '-'))


# 8.13
def count_odd(numbers):
    """
    Return the number of odd numbers in the list.
    """
    n_odd = 0
    for num in numbers:
        if num % 2 == 1:
            n_odd += 1
    return n_odd


print('number of odd numbers =', count_odd([1, 3, 5, 2, 4, 6, 5, 7, 9]))


# 8.14
def sum_even(numbers):
    """
    Returns the sum of all even numbers.
    """
    result = 0
    for num in numbers:
        if num % 2 == 0:
            result += num
    return result


print('sum of even numbers =', sum_even([1, 3, 5, 2, 4, 6, 5, 7, 9]))


# 8.15
def sum_negative(numbers):
    """
    Returns the sum of all negative numberes.
    """
    result = 0
    for num in numbers:
        if num < 0:
            result += num
    return result


print(sum_negative([1, 2, 3, -1, -2, -3, 0, -5]))


# 8.16
def tripled_list(numbers):
    """
    Returns a new list containing each original number times three.
    """
    result = []
    for num in numbers:
        result.append(num * 3)
    return result


print(tripled_list([1, 2, 3, 4, 5]))


# 8.17
def num_of_min_length(words, min_length):
    """
    Returns the number of words in the list that are at least of length min_length.
    """
    count = 0
    for word in words:
        if len(word) >= min_length:
            count += 1
    return count


print(num_of_min_length(['I', 'own', 'a', 'monkey'], 3))


# 8.18, 8.19
def sum_until_even(numbers, inclusive):
    """
    Sums all numbers until the first even number, inclusive or exclusive.
    """
    result = 0
    for num in numbers:
        if num % 2 == 0:
            if inclusive:
                result += num
            return result  # later we will learn about the 'break' statement, which could also work here.
        result += num
    # this is reached only if there is no even number:
    return result


print(sum_until_even([1, 1, 1, 2, 4, 6, 3, 5, 7], True))
print(sum_until_even([1, 1, 1, 2, 4, 6, 3, 5, 7], False))
print(sum_until_even([1, 1, 1, 3, 5, 7], False))  # this is why the second return statement is needed


# 8.20
def count_until_the(words):
    """
    Counts number of words occurring before 'the' (or all words if there is no 'the').
    """
    count = 0
    for word in words:
        if word == 'the':
            return count
        count += 1
    return count


print(count_until_the(['I', 'saw', 'the', 'fox']))


# 8.21
def even_vowel_count(word):
    """
    Returns true if word has even number of vowels, otherwise false.
    """
    vowel_count = 0
    for char in word.lower():
        if char in 'aeoui':
            vowel_count += 1
    return vowel_count % 2 == 0


print(even_vowel_count('monkey'))
print(even_vowel_count('APE'))
print(even_vowel_count('BANANA'))


# 8.23
def count_even_digits(number):
    """
    Returns the number of even digits in the number.
    """
    count = 0
    for digit in str(number):
        if int(digit) % 2 == 0:
            count += 1
    return count


print(count_even_digits(5671238))

# 8.24
numbers = [9, 5, 8, 3, 2, 6]
print([n for n in numbers if n > 4])
print([s[0] for s in names])  # initials
print([name[::-1] for name in names])
print([s for s in names if s[0].lower() in 'aeiou'])  # all names that start with a vowel

# 8.25
print([s.upper() for s in names])
# it demonstrates nothing: neither that strings are mutable (they aren't), nor that lists are mutable (though they are).
# both .upper() and list comprehension create a new object (a new string and a new list, respectively)

# 8.26
print([num ** 2 for num in numbers if num % 2 == 0])

# 8.27
print([name for name in names if len(name) >= 3])
print([len(name) for name in names])

# 8.28
print('----- 8.28 --------')
squared_evens = []
for num in numbers:
    if num % 2 == 0:
        squared_evens.append(num ** 2)
print(squared_evens)

names_3_or_longer = []
for name in names:
    if len(name) >= 3:
        names_3_or_longer.append(name)
print(names_3_or_longer)

name_lengths = []
for name in names:
    name_lengths.append(len(name))
print(name_lengths)


# 8.29
def filtered_list(source, filter):
    """
    Return a list of all elements of source that are also in filter.
    NOTE: The terminology 'filter' is arguably a bit weird; normally the filter will end up containing the stuff
    you remove; here, the filter contains all the things that won't be removed... Hmm.
    """
    return [element for element in source if element in filter]


print(filtered_list([1, 2, 3, 4, 5, 6, 7, 8], [0, 2, 4, 6, 8, 10, 12]))
