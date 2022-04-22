"""
17. Pattern matching
"""

import collections
import text_utils

# 17.1
import re
example_string = 'The famous Dr. Freud hastily acquired a magenta T-shirt and an old sweater for 24.95EUR. He then very very eagerly left the H&M at 1am... It was, as the doctor said, "a necessity".'
print(re.findall('[aeiou]+', example_string))
# The regular expression seems to match any lowercase vowel clusters.

# 17.2
# help(re)  #  https://docs.python.org/3/library/re.html

# 17.3
# Here's a trick to quickly copy-paste a list of items from somewhere, and turn it into an actual Python list :)
regexes = '''[a-z]+
[a-zA-Z]+
[a-zA-Z ]+
[^a-z]
[aeiou]
[aeiou]*
[^aeiou .]+'''.split('\n')

for regex in regexes:
    print(regex, re.findall(regex, example_string))

# These regexes represent, respectively:
#   - any maximal continguous stretches (+ means 'one or more') of lowercase alphabetical characters.
#   - same but case-independent
#   - same but permitting spaces as well (so cutting only at, e.g., punctuation)
#   - any single (no + sign) non-lowercase-alphabetical letter (so capitals, punctuation, spaces), since
#     ^ inside square brackets is negation.
#   - any single lowercase vowel
#   - any maximal stretch of zero or more (* means 'zero or more') lowercase vowels (hence it also matches empty strings everywhere).
#   - any maximal stretch (+) of anything that is not (^) a lowercase vowel, space or period.

# 17.4
def test_regexes(regex_list, string):
    print('Find matches in string:', string)
    for regex in regex_list:
        print(f'{regex:>20}  = ', re.findall(regex, string))

# 17.5
# Form your own predictions first!
regexes = """[0-9]
[0-9]+
\d+
[a-z]+
[A-Z]+
[A-Za-z]+
[a-zA-Z]+
[A-Z]+[a-z]+
[A-Z]+[a-z]*
[^A-Za-z]+
[A-Za-z0-9]+
\w+
\w+s
\w+ly
[^\w]+
The|the
[Tt]he""".split('\n')

test_regexes(regexes, example_string)

# 17.6
print('17.6')
# These result in special re-errors being raised.
# re.findall('[A-Z', example_string)   # unterminated character set
# re.findall('[A-', example_string)   # same
# re.findall('[a-z]++', example_string)   # multiple repeat
print(re.findall('A-Z', example_string))  # well-formed, but...
# ...it does not mean character range; it only matches a literal 'A-Z' string:
print(re.findall('A-Z', 'A-Z B-X QWKJSD'))


# 17.7
print('17.7')
regex = 'ab+c*d'
test_strings = """abbccd
abbbcd
accd
aabcd
abc
abbdd""".split('\n')
for s in test_strings:
    print(s, re.findall(regex, s))

# 17.8
print('17.8')
regexes = ['[ab]c+', 'a[bc]+', '[abc]+']
test_regexes(regexes, 'ac')   # all same match
test_regexes(regexes, 'abca')   # all different matches

# 17.9
print('17.9')
regexes = ['a+|b+', 'a+b+', '[ab]+']
# all same match is not possible (the first wants either only a, or only b; the second wants a mix)
test_regexes(regexes, 'aaa')    # 1 and 3 the same, 2 different
test_regexes(regexes, 'aaabbb')    # 2 and 3 the same, 1 different
test_regexes(regexes, 'bbaaabb')   # all different matches, in a sense

# 17.10
print('17.10')
first_attempt = 'an?'
improved = ' an? '  # you probably tried this too.
# To permit also capitalized A/An, one could do ' [Aa]n? '
test_regexes([first_attempt, improved], example_string)

# 17.11
# Other word boundaries are quotation marks (as in the example_string), punctuation, tabs, newlines...

# 17.12
print('17.12')
print('abc\bdef\b\bghij')
print('abc\\bdef\\b\\bghij')    # to compare

further_improved = '\\ban?\\b'
test_regexes([further_improved], example_string)    # yep!

# 17.13
print('17.13')
regex1 = '\ban?\b'
regex2 = '\\ban?\\b'
regex3 = r'\ban?\b'

print(regex1 == regex3, regex2 == regex3)
print(regex1, regex2, regex3, sep='\n')

# 17.14
print('17.14')
regexes = [regex1, regex2, regex3]
test_regexes(regexes, example_string)
# Make sure to formulate your own explanation of the foregoing.

# 17.15
print('17.15')
indefinite_regex = r'\b[Aa]n?\b'
test_regexes([indefinite_regex], example_string)

# 17.16
print('17.16')
definite_regex = r'\b[Tt]he\b'
# definite_regex = r'\bThe\b|\bthe\b' # equivalent, but less clear
test_regexes([definite_regex], example_string)

# 17.17
print('17.17')

strings = [
    'ta\ta\ta',     # contains two tabs, no backslashes
    'ta\\ta\\ta',   # contains two backslashes (and three Ts)
    r'ta\ta\ta',    # contains two backslashes (and three Ts)
    r'ta\\ta\\ta'   # contains four backslashes (and three Ts)
]
for s in strings:
    print(s, len(s))

# 17.18
print('17.18')

articles_regex = indefinite_regex + '|' + definite_regex
test_regexes([articles_regex], example_string)
# matches all articles (indefinite or definite)

# 17.19
print('17.19')
# findall (and regular-expression searches in general) returns only the MAXIMAL
# matching substrings, non-overlapping when gathered left-to-right.
# It is greedy in the sense that it matches as much as it can get, and
# first come first serve.
test_regexes([r'a+', r'aaa'], 'aaaaaaa')

# 17.20
# No spoilers here ;) See, e.g., the Wikipedia page about Chomsky hierarchy.

# 17.21
print('17.21')
regexes = [r'\Aabc']
test_regexes(regexes, 'abc blabla')
test_regexes(regexes, 'bla abc bla')

regexes = [r'a\sb', r'a\s+b']
test_regexes(regexes, 'bla\tbla\nbla bla  \t bla!')

# 17.22
print('17.22')
maths_string = '1 + 3   5 + 3   6 + 2   1 + 5'
regexes = [
    r'\d + \d', # incorrect
    r'\d \+ \d'    # correct
]

test_regexes(regexes, maths_string)

# The reason is that + is a special character in regular expressions (meaning: one or more
#   repetitions of the previous group). To match the literal +, you need to escape it like \+.
#   Note that the un-escaped variant matches sequences of one or more spaces.

# 17.23
print('17.23')
maths_string = '1 + 3   5123 / 32   6 + 2   1*512   123-321'
regexes = [
    r'\d+ \+ \d+',  # multi-digit numbers
    r'\d+ [\+/\*\-] \d+',  # other operations
    r'\d+ ?[\+/\*\-] ?\d+',    # spaces optional
           ]
test_regexes(regexes, maths_string)
# Note that / is NOT a special character for regex, so no escape needed.

# 17.24
# It would likely look horrible, with many lines of nested loops and ifs.

# 17.25
print('17.25')
number = r'\d+'
operator = r'[\+/\*\-]'
maths_regex = fr'{number} ?{operator} ?{number}'
test_regexes([maths_regex], maths_string)

# 17.26
print('17.26')
regexes = [
    r'[.,!]',  # inside [ ], . matches the literal period.
    r'.+',  # one or more of any character (except newline)
    r'\.+', # one or more literal periods
    r'".+"',  # any sequence of characters (except newline) in quotation marks.
    r'...', # any sequence of three characters (except newline); though note the greediness
]
test_regexes(regexes, example_string)

# 17.27
# Just like we need to do, e.g., r'\+' to match '+', we need to do r'\\' to match '\'.
# In both cases we escape the character not for the Python parser (not needed, since we use raw strings),
# but for the regular expression parser itself, for whom (unescaped) + and \ are special characters.
# Indeed, if we didn't use a raw string, we would need quadruple backslashes '\\\\' to match a single, literal backslash!

# 17.28
print('17.28')
# Change this path if necessary, depending on where you put your files:
gutenberg_path = '../adventures/data/gutenberg/alice_pg35688.txt'

vowel_cluster_regex = r'[aeiou]+'
text, _ = text_utils.read_from_gutenberg(gutenberg_path)
text = text.lower()
vowel_clusters = re.findall(vowel_cluster_regex, text)

vowel_cluster_counts = collections.Counter(vowel_clusters)
print(vowel_cluster_counts.most_common(20))

# 17.29
print('17.29')
consonants = 'bcdfghjklmnpqrstvwxyz'
initial_cons_clust_regex = fr'\b[{consonants}]+'
final_cons_clust_regex = fr'[{consonants}]+\b'

# We still have the variable  text  from before:
initial_cons_clusters = re.findall(initial_cons_clust_regex, text)
final_cons_clusters = re.findall(final_cons_clust_regex, text)

initial_cons_cluster_counts = collections.Counter(initial_cons_clusters)
final_cons_cluster_counts = collections.Counter(final_cons_clusters)
print(initial_cons_cluster_counts.most_common(20))
print(final_cons_cluster_counts.most_common(20))

# 17.30
print('17.30')
adverbs = re.findall(r'\b\w+ly\b', text)
adverb_counts = collections.Counter(adverbs)
print(adverb_counts.most_common(20))

# 17.31
print('17.31')
print(re.sub(r'[aeiou]', 'a', example_string))
print(re.sub(r'\b\w+ly\b', 'badly', example_string))
print(re.sub(r'\d+', '<censored>', example_string))

print(re.split(r'[^\w]+', example_string))
print(re.split(r'[.!?]+', example_string))


# 17.32
print('17.32')
print(re.findall(r'the', example_string))
print(re.findall(r'(?i)the', example_string))
# (?i) makes it ignore case!

print(re.split(r'\.', example_string))
print(re.split(r'(?<!Dr)\.', example_string))
# Splits on periods, but NOT if preceded by 'Dr'.


# 17.33-17.37
# Up to you, be adventurous!

# 17.38
print('17.38')

print(re.finditer(articles_regex, example_string))  # It's an iterator
print(list(re.finditer(articles_regex, example_string)))    # So do this, or a loop like below

# 17.39
print('17.39')
for match in re.finditer(articles_regex, example_string):
    print(f'{match.span()[0]}-{match.span()[1]}: {match.group()}')

# 17.40
print('17.40', flush=True)

def contextualize_matches(matches):
    matches = list(matches)
    text = matches[0].string
    bracketed_text = []
    for i in range(len(text)):
        # if matches[0].span()[0] == i:  #  Fixed!
        if matches and matches[0].span()[0] == i:
            bracketed_text.append('[')
        bracketed_text.append(text[i])
        # if matches[0].span()[1] == i:  # Fixed!
        if matches and matches[0].span()[1]-1 == i:
            bracketed_text.append(']')
            matches.pop(0)
    return ''.join(bracketed_text)

matches1 = re.finditer(r'abc', 'abc abc abc')
print(contextualize_matches(matches1))

matches2 = re.finditer(r'abc', 'abc abc def')
print(contextualize_matches(matches2))

# 17.41
print('17.41')
matches3 = re.finditer(articles_regex, example_string)
print(contextualize_matches(matches3))

# 17.42
print('17.42')
for match in re.finditer(r'(\w+)ly', example_string):
    print(match.group())
    print(match.group(1))
    print('-----')

# Apparently group() is what matches the whole regex;
#    whereas group(1) is only what matches what's in the first round parentheses.

# 17.43
print('17.43')
for match in re.finditer(fr'[{consonants}]([aeiou]+)', example_string):
    print(match.group(1), end=' | ')
print()

# 17.44
print('17.44')
for match in re.finditer(r'[aeiou]+', example_string):
    print(match.group(0), end=' | ')
    # identical to match.group() with no integer argument
    # apparently 0 is its default value.
print()

# print(match.group(1))   # error, no such group

# 17.45
print('17.45')
for match in re.finditer(fr'[{consonants}]([aeiou]+)', example_string):
    print(match.span(1), end=' | ')
print()
# yes.

# 17.46
print('17.46')
regexes = [r'ab', r'(a)b', r'(a)(b)', r'((a)b)']
test_regexes(regexes, 'abab')
# If the regex contains groups, re.findall returns a list of tuples of strings,
# each tuple containing the matching substrings for all groups (and the expression as a whole).

# 17.47
print('17.47')
regexes = [
    r'(ab)+',   # one or more repetitions of ab
    r'a+b+',    # one or more a, then one or more b
    r'ab+',     # one a, then one or more b
    r'(ab+)',    # same as before
    r'a(b+)'    # same as before
]

test_text = 'aaabbbabababaaa'
for regex in regexes:
    matches = [match.group() for match in re.finditer(regex, test_text)]
    print(regex, matches)

# 17.48
print('17.48')
maths_string = '1 + 3   51.23 / 0.32   6 + 2   1*512   1.23-32.1   0.52.312 * 65.1543'
number = r'\d+'
floating = rf'({number}.)?{number}'
operator = r'[\+/\*\-]'
maths_regex = rf'{floating} ?{operator} ?{floating}'
matches = [match.group() for match in re.finditer(maths_regex, maths_string)]
print(regex, matches)
# This could be further improved with e.g. spaces, to prevent the final partial match.

# 17.49
print('17.49')
# Formulate your own expectation first!
for match in re.finditer(r'(\w)\1', example_string):
    print(match.group())

# 17.50
print('17.48')
for match in re.finditer(r'(h[aeio])\1+', 'haha, hihi, hohoho, hahiho, hahi, hehe'):
    print(match.group())
# Yes :)

# 17.51
print('17.51')
# It looks for all duplicated words:
for match in re.finditer(r'(\b\w+\b)\s\1', example_string):
    print(match.group())
# Greedy, so no overlapping matches, i.e., only one match:
for match in re.finditer(r'(\b\w+\b)\s\1', 'test test test'):
    print(match.group())

# 17.52
print('17.52')
# We still have the variable  text  from before.
matches = [match.group() for match in re.finditer(r'(\b\w+\b)\s\1', text)]
print(collections.Counter(matches).most_common(20))

# 17.53
print('17.53')
print(re.split(r'[.!?]+', example_string))
print(re.split(r'([.!?]+)', example_string))

# The version with the capture group keeps punctuation. This might be convenient if our
# research was concerned with the use/meaning of punctuation, e.g., if we wanted to
# estimate emotion, or speaker authoritativeness, or, say, count the number of questions
# vs. assertions in a text.

# 17.54
print('17.54')

questions = re.findall(r'[^.!?]+\?+', text)
print(questions)

# quite a bit of pollution from newlines; let's replace them by periods
text_slightly_cleaned = text.replace('\n', '.')
questions = re.findall(r'[^.!?]+\?+', text_slightly_cleaned)
print(questions)

def categorize_question(question):
    keys = ['who', 'what', 'where', 'why', 'how', 'when']
    for key in keys:
        if question.strip().lower().startswith(key):
            return key
    # print('No category for:', question)
    return None

categories = [categorize_question(q) for q in questions]
category_counts = collections.Counter(categories)
print(category_counts)

# It appears that unclassified questions (many of which are non-wh-questions) are the most common;
# the most common wh-question is 'what', then 'why', then 'how'.