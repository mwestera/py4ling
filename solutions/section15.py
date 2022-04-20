
"""
15. Basic text processing
"""

import text_utils

# 15.1

print(dir(str))
print('testtest strip:', 'testtest'.strip('ts'))
print('TeStthisThing swapcase:', 'TeStthisThing'.swapcase()),
print('isalnum:')
print('  ABC:', 'ABC'.isalnum())
print('  1234:', '1234'.isalnum())
print('  ABC1234:', 'ABC1234'.isalnum())
print('  12.14:', '12.14'.isalnum())
print('  Haha!:', 'Haha!'.isalnum())
print('  1234'.center(30))

# 15.2
print('15.2')
print('abc abc abc abc abc abc abc'.split())
print('abc abc abc abc abc abc abc'.rsplit())   # no difference??
print('abc abc abc abc abc abc abc'.split(maxsplit=2))
print('abc abc abc abc abc abc abc'.rsplit(maxsplit=2)) # ah, splits from the right

# 15.3
print('\n15.3')
test_string = 'abcblablablaabc'
print(test_string.strip('abc'))
print(test_string.strip('cba'))
print(test_string.strip('a').strip('b').strip('c'))
print(test_string.strip('c').strip('b').strip('a'))
print(test_string.strip('bla'))

# 15.4
print('14.4')
list_of_strings = ['Alf', 'Beth', 'Gemma']
help(str.join)
print('-'.join(list_of_strings))

# 15.5
print('15.5')
s = """A multiline string
does the job
"""
print('before:', s)
print('after:', ' '.join(s.split()))

# 15.6
print('15.6')
print(' '.join(['a', 'b', 'c']))    # fine, for comparison
# print(' '.join(['a', 'b', 1, 2, 3]))    # nope
# print(' '.join([1, 2, 3]))    # nope

# 15.7
print('15.7')
names = ['john', 'sue', 'bob']
# names_joined = names.join('-')	# Doesn't work!
names_joined = '-'.join(names)   # fixed!
names_unjoined_again = names_joined.split('-')
print(names == names_unjoined_again)

# 15.8
# Suggestion: always read `x.join(y)` as "use _x_ to join _y_", and read `x.split(y)` as "split _x_ on _y_".
# The reason for this apparent asymmetry is quite simple (though ultimately just a design decision that could
#    have been made otherwise): joining is intended only for a list (or other type of collection) of strings
#    (not ints or other types of objects), but there is no designated class for 'collection of strings' in which
#    a join function could live; it fits more naturally in the string class, but that means it must be called on the
#    joiner (which is a string), not on the list (which isn't).

# 15.9, 15.10
print('\n15.9')
names = '''#*John#*
#*Mary# *,
*#*Suzy#*,
#*Bob#\t*;
#* Chris#\t*'''

def cleanup_from_pdf(string):
    corrections = {
        '0': 'O',
        '4': 'A',
        '5': 'S',
    }
    for key, target in corrections.items():
        string = string.replace(key, target)
    cleaned = [s.strip('#* \t,;') for s in string.split()]
    cleaned = [s for s in cleaned if not s == '']
    # Capitalize while respecting the dash (and two capitals) in Ann-Mary:
    cleaned = ['-'.join([s.capitalize() for s in n.split('-')]) for n in cleaned]
    return cleaned

print(cleanup_from_pdf(names))

# 15.10
worse_names = '''#*T0DD#*
#*0NA# *,
*#*SUE#*,
#*ANN-M4RY#\t*;
#* R0S5#\t*'''

print(cleanup_from_pdf(worse_names))

# 15.11
print('15.11')

print('abcdefabcdef'.replace('abc', '123'))
print('abcdefabcdef'.replace('qrs', '123'))
print('abcdefabcdef'.replace('abc', ''))    # Delete all occurrences of a certain substring
print('abc'.replace('', ' '))

# 15.12
def word_tokenize(text):
    return [w.strip('“”?!.,:;\'"') for w in text.split()]

test_string = '''
“Pray take a seat,” said Holmes. “This is my friend and colleague, Dr.
Watson, who is occasionally good enough to help me in my cases. Whom
have I the honour to address?”
'''

print(word_tokenize(test_string))

# Comparison: The one in text-utils treats punctuation as a separate token instead of getting rid of it. That is probably
#    more desirable, as punctuation carries meaning, but depending on the application this simple version could still be
#    useful.

# 15.13
# Up to you!

# 15.14
with open('test123.txt', 'w') as file:
    file.write('Hello!')

# 15.15
with open('test123.txt', 'w') as file:  # overwrites the previous content.
    file.write('Hello 2!')
    file.write('Hello 3!')      # both lines end up being written to the file.
    test = 'from within "with"-block'

print(test)  # Proves that the with-block does not create a local scope

# file.write('Hello 4!')  # ValueError: I/O operation on closed file.  (I/O = input/output)

# The latter error has nothing to do with local scope. After all, the error doesn't say the variable 'file' doesn't
# exist; it merely says it has been closed.

# 15.16
# with open('test123.txt') as file:     # without 'w', writing doesn't work
#     file.write('Hello!')

with open('test123.txt', 'a') as file:
    file.write('Hello again!')

# Check the file to see that with mode 'a' it appended it to the existing content, instead of overwriting it.

# 15.17
# help(open)
# In the documentation, 'truncating' refers to overwriting the contents of the file, starting from scratch, as
#    we observed earlier happens with mode 'w'.

# 15.18
with open('test123.txt', 'a') as file:
    for s in ['apple', 'pear', 'banana']:
        file.write(s + '\n')

# 15.19
print('15.19')
with open('test123.txt', 'r') as file:
    text = file.read()
print(text) # full file contents at once

# 15.20
print('15.20')
with open('test123.txt', 'r') as file:
    print('1:', file.read())
    print('2:', file.read())    # nothing left to read!

with open('test123.txt', 'r') as file:
    print('3:', file.read())    # now it works again

# 15.21
print('15.21')

# Formulate an expectation before you try this:

with open('test123.txt', 'r') as file:
    print('a:', file.read(5))
    print('b:', file.read(5))
    print('c:', file.read(3))

# The integer argument specifies the number of characters to read next from the file (continuing where you left off).
#    Omitting this argument leads to reading the entire file.

# 15.22
# Yes, it fits with our observations. And after reading the entire file, the pointer will be whatever the length (`len`)
#    of the file was. Let's test:
print('15.22')
with open('test123.txt', 'r') as file:
    text = file.read()
    print('pointer:', file.tell())
    print('len:', len(text))

# 15.23
print('15.23')
# Form your expectation before trying this:
with open('test123.txt', 'a') as file:
    print('start pointer a:', file.tell())
with open('test123.txt', 'w') as file:
    print('start pointer w:', file.tell())
    file.write('just write some lines\nso the file\nisn\'t empty for the next exercises')

# remember to write something to the file

# 15.24
print('15.24')
file = open('test123.txt', 'r')
text = file.read()
file.close()
print(text) # yep.

# 15.25
# Can you manually change the contents of the file in the editor? Yes.
# Do they show up if you subsequently read the file in Python? Yes (but of course not if your script itself resets the
#   file prior to reading it).
# And if you write something to the file through Python, does your view of the file in the editor update
#   automatically? Yes, but there can be some delay.

# 15.26
# If you move your entire project (including the referenced file) somewhere else, then the absolute paths will
# no longer work, while the relative paths keep functioning. On the other hand, if you move only your
# Python script (containing the path reference) to somewhere else on your file system (even within the project folder),
# then the absolute paths may keep functioning, while the relative paths no longer work (though for changes within
# the project, executed in PyCharm, the latter may offer some help updating them automatically). And of course if you
# move the target file someplace else, independently of your Python script, then both absolute and relative paths will
# break.

# 15.27
# Just try this.

# 15.28
# Just try this.

# 15.29
print('15.29')
# In a nutshell, the `input` and `print` functions take input from, and send output to, the Run window at the bottom.
# These suffice as a simple, direct user interface, but provide no access to, for instance, files on your disk.

# A bit more detail:
# input: Gets user input from the terminal/Run window in PyCharm, during execution of the script. By contrast, opening
#     a file and using .read() reads data from a file in storage.
# print: Sends strings to the standard output stream, which in PyCharm will show up in the terminal/Run window in
#     PyCharm. Something to keep in mind is that print by default prints a newline at the end, but the write method
#     of a file object does not:
print('one')
print('two')    # separate lines (unless you specify sep='')!
with open('test123.txt', 'w') as file:
    file.write('one')
    file.write('two')   # not on separate lines
#    file.write('one', 'two')    # not allowed, unlike print
#    file.write(123)            # non-str argument not allowed, unlike print

# import: Reads a Python script from a file, and INTERPRETS it as Python code, constructing a Module object (instead of
#     returning a plain string object like file.read()). Something to keep in mind when using import is that you don't
#     specify the file extension of the imported file (typically .py, if you import a single file).

# 15.30
with open('testABC.txt', 'w') as file:
    for i in range(10):
        file.write(f'{i}\n')

for i in range(10):
    with open('testDEF.txt', 'a') as file:
        file.write(f'{i}\n')

# The first will in general be preferable, as it allows Python to buffer the various written strings and write them to
# disk all at once at the end, when the file is closed. The second version opens and closes the file many times,
# each time writing to disk, which will generally be slower. Disk access is generally a bottleneck; communication with
# the processor and working memory is quicker.
# The latter version might be preferable in some cases, e.g., for readability if the body of the for-loop becomes a lot
# more complex, or for a particular application, e.g., if the body of the for loop takes longer to compute yet you
# still want the output file to be updated in real time.

# 15.31
print('15.31')
with open('testABC.txt', 'r') as file:
    print(file.readline())
    print(file.readline())  # yes, it works!
    for _ in range(3):
        print(file.readline())  # wooh!

# 15.32
print('15.32')
with open('testABC.txt', 'r') as file:
    for line in file:
        print(line, end='') # fixed
# The empty lines are due to the fact that each line includes the final \n (read from the file),
# and then the print statement adds an additional \n.

# 15.33
print('15.33')
with open('testABC.txt', 'r') as file:
    print('loop 1:')
    for line in file:
        print(line, end='')
    print('loop 2:')
    for line in file:
        print(line, end='')
# The second time around it doesn't print anything.

with open('testABC.txt', 'r') as file:
    print('loop 3:')
    for line in file:
        print(line, end='')
# But now it does. Yes, this aligns with the fact that opening a file creates a pointer to the 'current line'.
# After reading an entire file the pointer is at the end, and trying to read again will result in the empty string.

# 15.34
print('15.34')
with open('test123.txt', 'r') as file:
    print(file)

# 15.35
# There are 2^8 different bytes, that is, 256, but there are MANY more characters than 256. Consider the many alphabets.

# 15.36
print('15.36')
with open('emojis.txt', 'w') as file:
    file.write('😀😃😄')
with open('emojis.txt', 'r', encoding='ASCII') as file:
    # print(file.read())   # UnicodeDecodeError!
    pass

# 15.37
# Change this path if necessary, depending on where you put your files.
gutenberg_path = '../adventures/data/gutenberg/alice_pg35688.txt'

def average(l):
    return sum(l) / len(l)

def extract_stats(path):

    base, extension = path.rsplit('/')[-1].rsplit('.', maxsplit=1)  # the 'os' module has more robust ways to achieve this
    outpath = f'output/{base}_stats.{extension}'

    nchars_per_line = []
    nwords_per_line = []
    nchars_per_word = []

    with open(path, 'r') as file:
        for line in file:
            nchars_per_line.append(len(line))
            words = text_utils.tokenize(line)
            nwords_per_line.append(len(words))
            nchars_per_word.extend(len(word) for word in words)

    avg_nchars_per_line = average(nchars_per_line)
    avg_nwords_per_line = average(nwords_per_line)
    avg_nchars_per_word = average(nchars_per_word)

    with open(outpath, 'w') as file:
        # using some funky f-string syntax we didn't learn about yet (of course there are other ways):
        file.write(f'{avg_nchars_per_line=}\n')
        file.write(f'{avg_nwords_per_line=}\n')
        file.write(f'{avg_nchars_per_word=}')

    # The reading and writing could probably be more cleanly split into different functions... Feel free to!

extract_stats(gutenberg_path)


# 15.38
# For conceptual clarity, but also for instance because it reduces the risk of accidental overwriting of your raw data (but always make backups, anyway).

# 15.39
# Line-by-line analysis would be preferable is the file is particularly big, and if the analysis does not require storing the
# full data in memory at any point (and perhaps that wouldn't even fit).

# 15.40
print('15.40')
with open(gutenberg_path, 'r') as file:
    first_chars = [l[0] for l in file]

with open(gutenberg_path, 'r') as file:
    line_lengths = [len(l) for l in file]

with open(gutenberg_path, 'r') as file:
    stripped_lines = [l.strip() for l in file]

with open(gutenberg_path, 'r') as file:
    tokenized_lines = [text_utils.tokenize(l) for l in file]

print(first_chars)
print(line_lengths)
print(stripped_lines)
print(tokenized_lines)

# 15.41-15.45
# The read_from_gutenberg function has been moved to text_utils.py

text, meta_info = text_utils.read_from_gutenberg(gutenberg_path)
print(text[:300])   # print just a snippet
print(meta_info)

