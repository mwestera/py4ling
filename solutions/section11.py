"""
11. Functions, parameters and arguments
"""

# 11.1
# print_spam()    # NameError: name 'print_spam' is not defined.

def print_spam():
    print('spam!')


# 11.2
print('bla')
print('bla')
print('bla')
print('bla')
# print(x)    # NameError appears ABOVE the printed 'bla' strings.

# 11.3
print('bla', flush=True)
# print(x)    # NameError now appears BELOW all the printed 'bla' strings.


# 11.4
def invert(s):
    return s[::-1]

def print_inverted(s):
    s = invert(s)
    print(s)

print_inverted('abc')

# The two function definitions can be in either order. The function call should be at the bottom or we get a NameError.
# Formulating a hypothesis is left to you :)

# 11.5
# The first program:

def print_sum(a, b):
    print(add_numbers(a, b), flush=True)

def add_numbers(a, b):
    return a + b

print_sum(1, 3)

# The second program (make sure you try the two programs separately):

# def print_sum(a, b):
#     print(add_numbers(a, b), flush=True)
#
# print_sum(1, 3)       # This gives a NameError: add_numbers is not defined.
#
# def add_numbers(a, b):
#     return a + b

# 11.6
# It all makes sense now! (I hope)

# 11.7
def time_to_secs(hours, minutes, seconds):
    total_seconds = 60 * 60 * hours + 60 * minutes + seconds
    return int(total_seconds)

# 11.8
def hours_in(seconds):
    return seconds // (60 * 60)

def leftover_minutes_in(seconds):
    seconds_without_hours = seconds % (60 * 60)
    return seconds_without_hours // 60

def leftover_seconds_in(seconds):
    return seconds % 60

# 11.9
def secs_to_time(seconds):
    return hours_in(seconds), leftover_minutes_in(seconds), leftover_seconds_in(seconds)

# Again, the order of the function definitions doesn't matter, as long as all functions are defined
# by the time they are called.

print(secs_to_time(30))
print(secs_to_time(120))
print(secs_to_time(3600))
print(secs_to_time(124124))

# 11.10
# Copied from 9.14:
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

def bigrams(sentence):
    """
    Return a list of all bigrams of the sentence.
    """
    return ngrams(sentence, 2)

def trigrams(sentence):
    """
    Returns a list of all trigrams of the sentence.
    """
    return ngrams(sentence, 3)

def quadrigrams(sentence):
    """
    Returns a list of all quadrigrams of the sentence.
    """
    return ngrams(sentence, 4)

def ngrams(sentence, n, as_strings=False):
    """
    Returns a list of n-grams of the sentence.
    """
    tokens = tokenize(sentence)
    ngrams = [tokens[i:i+n] for i in range(len(tokens) - (n - 1))]
    if as_strings:
        ngrams = [' '.join(ngram) for ngram in ngrams]  # change requested by client, from 11.12
    # Of course you can also achieve this without list comprehension, and without join, by using.
    # multi-line loops.
    return ngrams

print(bigrams('the quick brown fox jumped over the lazy dog'))
print(trigrams('the quick brown fox jumped over the lazy dog'))
print(quadrigrams('the quick brown fox jumped over the lazy dog'))
print(ngrams('the quick brown fox jumped over the lazy dog', 3, True))

# 11.11
# Repetition in code typically makes it take longer to read and understand; and harder to maintain (if you need to
# make a change, you often need to make the same change in multiple places); and the latter makes it more error-prone
# (it's easy to make a change in one place and forget to make the corresponding place in another).

# 11.12
# See above for the change. Advantage is we only needed to make the change in one place.

# 11.13
def filter_by_twos(l):
    """
    Return a new list containing only every second element.
    """
    return filter_by_n(l, 2)

def filter_by_threes(l):
    """
    Return a new list containing only every third element.
    """
    return filter_by_n(l, 3)

def filter_by_n(l,n):
    """
    Return a new list containing only every nth element.
    """
    return l[n-1::n]    # try what goes wrong without the n-1

print(filter_by_twos([1, 2, 3, 4, 5, 6]))
print(filter_by_threes([1, 2, 3, 4, 5, 6]))

# 11.14
directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

def turn_clockwise(start_direction, n_turns=1):
    """
    Takes a string representation of a direction and returns the new direction after
    turning n_turns 'steps' clockwise. Default is 1 step.
    """
    return turn(start_direction, n_turns)

def turn_counterclockwise(start_direction, n_turns=1):
    """Takes a string representation of a direction and returns the new direction after
    turning n_turns 'steps' counterclockwise. Default is 1 step."""
    return turn(start_direction, -n_turns)

def turn(start_direction, turns):
    """
    Takes a string representation of a direction and returns the new direction after turning the amount
    specified by turns. turns can be positive (clockwise) or negative (counterclockwise).
    """
    index = directions.index(start_direction)
    turned_index = (index + turns) % len(directions)
    return directions[turned_index]

print(turn_clockwise('W'))
print(turn_clockwise('NE', n_turns=2))
print(turn_counterclockwise('W'))
print(turn_counterclockwise('NW', n_turns=3))

# 11.15, 11.16
print('11.15')
b = 987 # added for 11.16

def some_function():
    b = 123
    print('inside the function, b =', b, flush=True)

some_function()
print('outside the function, after calling the function, b =', b)

# In 11.15 the last line gave a NameError: name 'b' is not defined.
#   It reflects encapsulation: b is assigned inside the function, hence only available in that 'local scope'.

# In 11.16, the last line prints 987, again showing that the variable b inside the function, while the same name,
    # is a different, 'local' variable.

# 11.17
# If you comment-out the b = 123 inside the function, what gets printed inside the function is the value 987.
# There is, therefore, an asymmetry: in the local scope (function) I can access the global variable b with value 987;
# but in the global scope (outside the function) I cannot access the local variable b with value 123.

# 11.18
# That code runs fine, so if-clauses do not create a 'local scope' like functions do.

# 11.19
# Yes, that's what it shows, as long as we recognize that the 'stepper' variable x is assigned 'inside' the for-clause.
# For a clearer example, you can add e.g. y = 123 inside the for-clause's body (indented), to show the same.

# 11.20
# No, it does not show that if-clauses create a local scope (because they don't). The error is due, instead, to
# the fact that the if-condition is always False, so the body of the if-clause is not executed, and that's why the
# variable is simply not assigned. Nothing to do with scope. (Note that PyCharm gives you a warning in the editor:
# the code inside the if-clause is 'unreachable'.)

# 11.21
# That question does not really make sense, because the individual clauses are necessarily mutually exclusive.
# Again, nothing to do with scope. (But, hypothetically, if they hadn't been mutually exclusive (impossible),
# one would expect them to share variables, because if-clauses do not create a local scope.)

# 11.22
print('11.22')

a = 3
b = 4

def my_function(c):
    d = 6
    e = 7
    print('inside my_function, locals = ', locals())
    print('inside my_function, globals =', globals())

my_function(5)

# 11.23
# The variable c is a parameter, to which the function assigns the value 5 when the function is called with argument 5.

# 11.24
# It shows that, in the global scope, locals and globals return the same dictionary.
# It also shows that c, d, e are missing, because they are encapsulated inside the function.
print('outside my_function, locals = ', locals())
print('outside my_function, globals =', globals())

# 11.25
# While the two variables have the same name, one is in locals() and the other in globals(); they are, therefore,
# technically distinct variables. Inside the function, only the local variable is affected. And it ceases to exist as
# soon as the function is done and we return to the global scope.

# 11.26
print('11.26')

students = ['ann', 'beth', 'gemma']
more_students = ['dale', 'ebba']
message = 'Hello'

def print_students(students):

    students = [name.capitalize() for name in students]
    # students (on the right) is a local variable, its value assigned by the function upon being called (parameter)
    #   (This variable is re-assigned a new value here, referenced below.)
    # local variable name was assigned (and reassigned) in this single line, by the for-loop in the list comprehension

    for student in students:
        # the local variable students was re-assigned its value above, when capitalizing all the names.
        print(message, student)
        # message was assigned in the global scope
        # student (local) was assigned (and reassigned) its value by the header of the for-loop.

students[1] = 'elisabeth'
# no reassignment to a variable here; rather, a change of the (mutable) list already stored in students from the initial line.

all_students = students + more_students
# the values of both students and more_students are still as assigned initially (even hough the exact contents of the value
#    (list object) assigned to students have changed in the meantime, it's still the same single list object.)

all_students.append('philip')
# again, no reassignment, but modifying a mutable object.

print_students(all_students)
# this was assigned its value two lines ago (all_students = ...), though the contents of its (mutable) value have changed.

if len(all_students) > 3:   # recall: if-clause creates no local scope
    message += ' everyone!'
    # this uses the old value of message, assigned near the start, and reassigns a new value to the same variable.
    print(message, flush=True)

# 11.27
print('11.27')
a = 5

def erroneous_function():
    # print(a)    # UnboundlocalError: local variable 'a' referenced before assignment
    a = 8

erroneous_function()

# The reason this gave an error is that a is assigned a value inside the function, meaning it is a local variable
# everywhere in that function, even before it is assigned.

# 11.28
# That code creates the same error as before. The reason is that incrementing with += 3 is an assignment operation too,
# shorthand for b = b + 3, hence b must be local throughout the function.

# 11.29
# A possible explanation is that it helps avoid programming errors. Inside a function, moving code around is pretty
# common. Without the all-or-nothing behavior with regard to local/global, moving code around inside a function
# could easily accidentally change a variable from local to global instead of raising an explicit error.
# It would introduce a 'silent' bug in your code (unintended behavior), hence potentially hard-to-discover.

# 11.30
print('11.30')
x = 6

print(x)    # 6

def first_function(x):
    print(x)

def second_function():
    print(x)

def third_function(y):
    x = y - 3
    print(x)

print(x)    # 6
first_function(3)  # 3
print(x)    # 6
second_function() # 6
print(x)    # 6
third_function(x) # 3
print(x)    # 6

# 11.31
# Formulate your own summary of this section! How does Python govern local vs. global scope?