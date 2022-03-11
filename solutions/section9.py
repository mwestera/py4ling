"""
9. More practice with lists and loops (also index, range)
NOTE: I've separated all solutions per section into different files, after all.
Seems more convenient that way, easier to search...
"""


# 9.1
def sum(numbers):
    """
    Returns the sum of all numbers. NOTE: This emulates the built-in function 'sum' (hence PyCharms gives you
    a warning (squiggle underneath the function name): it shadows the name of an existing function.
    """
    result = 0
    for num in numbers:
        result += num
    return result


def average(numbers):
    """
    Returns the average of the list of numbers.
    """
    return sum(numbers) / len(numbers)


import math  # this would normally be at the top of the file


def std(numbers):
    """
    Returns the unbiased sample standard deviation.
    NOTE: the exercise wasn't explicit about which notion of standard deviation to compute; see e.g. Wikipedia.
    Below is not the most efficient possible calculation, for the sake of exposition.
    """
    avg = average(numbers)
    squared_diffs = [(num - avg) ** 2 for num in numbers]  # you can also use a multi-line for-loop of course.
    uncorrected_variance = average(squared_diffs)
    # The uncorrected sample variance is a biased estimate of the true (population) variance; it's a little bit
    # too low: For N items in your sample, it is expected to be a factor 1 / N too low.
    # So we divide it by N-1, and multiply by N, to effectively increase it by a factor 1 / N.
    # This is called Bessel's Correction. See https://en.wikipedia.org/wiki/Bessel's_correction#Source_of_bias
    corrected_variance = uncorrected_variance * len(numbers) / (len(numbers) - 1)
    return math.sqrt(corrected_variance)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(average(numbers), std(numbers))

# 9.2
words = ['the', 'dog', 'is', 'in', 'the', 'garden']


def total_word_length(words):
    """
    Returns the total length of all words combined.
    """
    # Let's use our function sum from earlier (you would normally use the built-in sum).
    # You can also use an explicit for-loop to compute the sum, of course.
    return sum([len(word) for word in words])


print(total_word_length(words))
print(len('the dog is in the garden'))  # this also counts the spaces, hence the difference


# 9.3
def index_in_string(string, character):
    """
    Returns the first index in the string at which the character occurs.
    Note: this emulates the built-in string method index.
    """
    index = 0
    for char in string:
        if char == character:
            return index
        index += 1
    # note that it returns None if the character does not appear in the string


print(index_in_string('david', 'v'))

# It is the inverse of accessing a character by index, so we can go back and forth:
print('david'[index_in_string('david', 'v')] == 'v')


# 9.4
def index_in_list(l, element):
    """
    Returns the first index in the list at which the element occurs.
    Note: this emulates the built-in list method index.
    """
    return index_in_string(l, element)  # being extremely lazy, it just works already :)


print(index_in_list([1, 2, 3, 4, 5], 3))

# 9.5
print('david'.index('v'))
print([6, 4, 8, 6].index(8))

print(index_in_string('david', 'x'))  # this returns None


# print('david'.index('x'))   # this gives an error, so they don't quite behave the same.

# 9.6
def find_index_of_largest(l):
    """
    argmax function; not the most efficient implementation, because it it's (underneath the surface) looping
    through the list twice: once to find the maximum, once to find its index. Better do both at once.
    """
    return l.index(max(l))  # literally, the index of the max :)


print(find_index_of_largest([1, 2, 3, 4, 5, 4, 3, 2]))
print(find_index_of_largest(['a', 'b', 'c', 'b', 'a']))
print(find_index_of_largest('abcba'))


# 9.7
def count_words(s):
    """
    Return the word count, or actually, the number of spaces in the string.
    """
    # This solution relies on boolean True evaluating to 1, and False to 0, to be able to then sum them.
    num_spaces = sum([char == ' ' for char in s])
    # you can also a multi-line loop if you find that more readable.
    # and another variant:
    # num_spaces = len([char for char in s if char == ' '])
    return num_spaces + 1


print(count_words('The quick brown fox jumped over the lazy dog.'))


# 9.8
def vowels_to_y(s):
    """
    Returns a string that is like s but with all vowels replaced by 'y'.
    """
    result = ''
    for char in s:
        if char.lower() in 'aeiou':
            result += 'y'
        else:
            result += char  # note that this char has not been lower-cased!
    return result


print(vowels_to_y('banana'))
print(vowels_to_y('haha!'))
print(vowels_to_y(['b', 'a', 'n', 'a', 'n', 'a']))  # works too;
# for strings, the function cannot be defined to modify it in-place; for lists this would be possible.

# 9.9
for n in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(n)

