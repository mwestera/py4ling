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

# going back and forth more slowly:
# index_of_v = index_in_string('david', 'v')
# character_at_index_of_v = 'david'[index_of_v]
# index_of_character_at_index_of_v = index_in_string('david', character_at_index_of_v)
# print(index_of_character_at_index_of_v)


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
for n in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:    # not convenient!
    print(n)

# 9.10
for i in range(1000):   # convenient!
    print(i, end=' ')
print()

# 9.11
for i in range(len(words)):
    print(i, words[i])

# 9.12
# for i in range(words):  # TypeError: list object cannot be interpreted as an integer
#     print(i)
# for i in range(len(words - 1)):  # TypeError: unsupported operand type(s) for -: 'list' and 'int'
#     print(i)


# 9.13
for i in range(len(words)-1):   # without the -1 you'd get an error, because [i+1] below would be out of bounds.
    print(words[i], words[i+1])

# 9.14
def tokenize(sentence):
    """
    Split the sentence into tokens, returning the list of tokens.
    """
    tokens = ['']
    for char in sentence:
        if char == ' ':
            tokens.append('')
        elif char in '.,:;?!':    # treat each punctuation mark as separate token as well
            tokens.append(char)
        else:
            tokens[-1] += char
    return tokens

print(tokenize('the quick brown fox jumped, over the lazy dog.'))

# 9.15
def bigrams(sentence):
    """
    Return a list of all bigrams of the sentence.
    """
    tokens = tokenize(sentence)
    bigrams = [tokens[i:i+2] for i in range(len(tokens) - 1)]
    # Of course you can do this with a multi-line for-loop if you find that more readable.
    return bigrams

print(bigrams('the quick brown fox jumped over the lazy dog'))

# 9.16
def trigrams(sentence):
    """
    Returns a list of all trigrams of the sentence.
    """
    tokens = tokenize(sentence)
    trigrams = [tokens[i:i+3] for i in range(len(tokens) - 2)]
    return trigrams

print(trigrams('the quick brown fox jumped over the lazy dog'))

# 9.17
# 1. One could change the bigrams and trigrams functions to take already-tokenized text as arguments instead of a
#    plain string. That way you can first tokenize the text once and for all, in advance, separately from the
#    bigrams and trigrams functions, and then call the latter on the tokenized text.
# 2. Note the overlap between this function and the bigrams function. Clearly, a generalized 'ngrams' function,
#    with an integer argument n, would be preferable!

# 9.18
# The string method capitalize returns a new string, it does not change the original string (which is immutable, after
# all).

# 9.19
# Still doesn't change the list. Recall from section 2 that variables are assigned independently. Thus, assigning
# the new, capitalized string to the variable city DOESN'T automatically assign it to the corresponding
# index in the original list.

# 9.20
# You need to reassign something to the list index, hence you need to loop over list indices, and therefore use range.
cities = ['amsterdam', 'rotterdam', 'leiden', 'gouda', 'eindhoven']
for i in range(len(cities)):
    cities[i] = cities[i].capitalize()

print(cities)

# 9.21
for city1 in cities:
    for city2 in cities:
        print(city1 + '-' + city2)

print('----')

# 9.22
for city in cities:
    for city in cities:
        print(city)

# 9.23
for city1 in cities:
    # Note: you can put the first if-condition over here, so that the second loop
    # doesn't even begin if the first city doesn't start with a vowel. That would be more efficient
    # (in case you have many cities), but arguably a bit less readable.
    for city2 in cities:
        if city1[0].lower() in 'aeoui' and city2[0].lower() not in 'aeiou':
            print(city1, city2)

# 9.24
def chain(list_of_lists):
    """
    Takes a list of lists and chains them together, returning a single 'flattened' list.
    """
    result = []
    for inner_list in list_of_lists:
        for element in inner_list:
            result.append(element)
    return result

print(chain([[1, 2], [3, 4, 5], [6, 7]]))

# 9.25
determiners = ['a(n)', 'the']
nouns = ['tree', 'house', 'person', 'teacher']
intransitive_verbs = ['fall', 'sing']
transitive_verbs = ['hit', 'kiss']

def generate_all_sentences():
    """
    Print all sentences based on the above vocabulary.
    """
    for noun in nouns:
        for determiner in determiners:
            for verb_frame in ['transitive', 'intransitive']:
                if verb_frame == 'transitive':
                    for verb in transitive_verbs:
                        for determiner2 in determiners:
                            for noun2 in nouns:
                                print(f'{determiner} {noun} {verb}s {determiner2} {noun2}')
                else:
                    for verb in intransitive_verbs:
                        print(f'{determiner} {noun} {verb}s')

generate_all_sentences()

# 9.26
# This exercise is of course about the recursive nature of human languages and the -- in principle -- infinitude of
# sentences it can generate. How strongly you feel about this infinitude may depend on your stance toward the
# competence-performance distinction (do you see why?).

# 9.27
directions = ['N', 'E', 'S', 'W']

def turn_clockwise(start_direction):
    """
    Takes a string representation of a direction (NESW) and returns the new direction after
    turning one 'step' clockwise.
    """
    index = directions.index(start_direction)
    turned_index = (index + 1) % len(directions)
    return directions[turned_index]

print(turn_clockwise('W'))
print(turn_clockwise('N'))

# 9.28
# One is the type of the function itself, the other is the type of the result of calling the function.

# 9.29
def turn_counterclockwise(start_direction):
    """Takes a string representation of a direction (NESW) and returns the new direction after
    turning one 'step' counterclockwise."""
    index = directions.index(start_direction)
    turned_index = (index - 1) % len(directions)
    return directions[turned_index]

print(turn_counterclockwise('W'))
print(turn_counterclockwise('N'))

print(turn_counterclockwise(turn_clockwise('N')) == 'N')    # yes :)

# 9.30
# They are already pretty streamlined. However, note that there is still considerable overlap between the
# two functions, so perhaps you can try to streamline the code further... Later there will be an exercise about this.

# 9.31
# This is a matter of extending the directions list, and everything will just work. That is because
# the functions are programmed in a robust way (e.g., using % len(directions) instead of % 4).
