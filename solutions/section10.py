"""
10. Functions, parameters and arguments
"""

# 10.1
def print_spam():
    print('spam')

print(print_spam())   # this prints the result of calling the function (which is None, because it doesn't return anything)
    # note that this first prints 'spam' (printed as the function is called), and then None.
print(type(print_spam()))
print(print_spam)     # this prints the function itself
print(type(print_spam))

# 10.2
print('10.2')

shout_nonsense = print_spam

shout_nonsense() # yes, this works!

# 10.3
print('10.3')

def do_twice(func):
    """
    Takes a function as argument and calls it twice.
    """
    func()
    func()

do_twice(print_spam)

# do_twice(print_spam())
# TypeError: 'NoneType' object is not callable. This is because the result of print_spam() is None,
#    and passing None as argument to the function do_twice will result in 'calling' None as if it
#    is a function, which it isn't.

# 10.4
print('10.4')

def do_twice_with_argument(func, arg):
    """
    Takes a function and argument as arguments, and calls the function on the argument twice.
    """
    func(arg)
    func(arg)

do_twice_with_argument(print, 'test')

# 10.5
print('10.5')
do_twice_with_argument(do_twice, print_spam)

# 10.6
print('10.6')
def do_multiple(func, n):
    """
    Takes a function and an integer n, and calls the function n times.
    """
    for _ in range(n):  # we use the 'unnamed' variable _ to signify its value doesn't matter.
        func()

do_multiple(print_spam, 10)

def do_multiple_with_arg(func, arg, n):
    """
    Takes a function, an argument and an integer n, and calls the function on the argument n times.
    """
    for _ in range(n):
        func(arg)

do_multiple_with_arg(print, 'test', 10)

# 10.7
print('10.7')
print(print_spam.__name__)  # this just prints the name: print_spam
# print(print_spam().__name__)    # this prints 'spam' and then throws an error because the object None (returned
    # by print_spam()) does not have a __name__ attribute.

# 10.8
print('10.8')
print(shout_nonsense.__name__)  # it still has the old name! It's an actual property of the function object, not just a variable.

# 10.9
print('10.9')

print('apple')
print.__call__('apple') # same result

shout_nonsense()
shout_nonsense.__call__()   # this too

# 10.10
def print_diff(a, b):
    """
    Prints the difference a - b.
    """
    print(a - b)

print_diff(5, 2)
print_diff(a=5, b=2)
print_diff(b=2, a=5)
print_diff(2, 5)
print_diff(a=2, b=5)
print_diff(b=5, a=2)

# 10.11
# Arguments without keywords are matched to the function's parameters based on position: first argument sets the first
#     parameter, second argument sets the second parameter, etc. For keyword arguments, the position doesn't matter.

# 10.12
print_diff(5, b=2)      # fine; 5 is treated as positional argumente, hence mapped to the first parameter, a.
# print_diff(2, a=5)    # TypeError: print_diff() got multiple values for argument 'a'
# The second one crashes, because 2 (no keyword) is treated as a positional argument, hence it is used to set
#   the parameter a, but then the subsequent a=5 sets the same parameter, leaving b unspecified.

# 10.13
# print_diff(a=5, 2)  # SyntaxError: positional argument follows keyword argument.

# 10.14
print('apple', 'pear', 'banana', sep='-', end='.')
print()
print('apple', 'pear', 'banana', '-', '.')
# In the latter case the dash and point are simply printed, not treated as values for the parameters sep and end.

# 10.15
# Keyword arguments make explicit the role that the argument will play in the function (i.e., the parameter name),
#   whereas to understand the role of a positional argument (i.e., without parameter name) you need to remember or
#   look up the order of parameters of the function.

# 10.16
def some_weird_function(*a, b, c):
    print('a:', a)
    print('b:', b)
    print('c:', c)

# some_weird_function(1, 2, 3)     # will complain that `b` and `c` are not given values, as all positional arguments are eaten up by `*a`.
some_weird_function(1, b=2, c=3)    # this one works fine
some_weird_function(1, 2, 3, 4, b=5, c=6)   # this also works fine

# The asterisk *a makes the parameter a 'use up' all the positional arguments. They are stored in a tuple (about
#    which we will learn more later) and assigned to a.

# 10.17
# The asterisked parameter of the print function eats up all positional arguments; it enables the print function
# to be used with a variable number of positional arguments, each getting printed. It also means the later parameters,
# like sep and end, can only be specified using keyword arguments.

# 10.18
def multiply_and_add(a, b, c=1):
    """
    Prints the product of a and b, plus c.
    """
    print(a * b + c)

multiply_and_add(2, 3)  # no third argument provided, so the third parameter is given its default value of 1
multiply_and_add(2, 3, 4)   # third argument provided, overrules the default value of the third parameter.

# 10.19
# Parameters with defaults do not need an argument in the function call in order to be given a value, and in that
# sense the corresponding argument is 'optional'; parameters with no defaults do need an argument in the function
# call in order to be given a value, hence those arguments are effectively 'mandatory'.

# 10.20
def subtract(a, b, absolute=False):
    """
    Returns a - b by default, or its absolute value if absolute is set to True.
    """
    diff = a - b
    if absolute and diff < 0:
        diff = -diff
    return diff
    # more Pythonic would be to use the built-in abs:
    # if absolute:
    #     diff = abs(diff)

print(subtract(3, 5))
print(subtract(3, 5, True))

# 10.21
def tokenize(sentence, keep_spaces=False):
    """
    Split the sentence into tokens, returning the list of tokens. (Based on 9.14)
    """
    tokens = ['']
    for char in sentence:
        if char == ' ':
            if keep_spaces:
                tokens[-1] += ' '
            tokens.append('')
        elif char in '.,:;?!':    # treat each punctuation mark as separate token as well
            tokens.append(char)
        else:
            tokens[-1] += char
    return tokens

print(tokenize('the quick brown fox jumped, over the lazy dog.'))
print(tokenize('the quick brown fox jumped, over the lazy dog.', keep_spaces=True))

# 10.22
print('10.22')
subtract(5, 3, absolute=True)
subtract(5, 3, True)
print(tokenize('the quick brown fox jumped, over the lazy dog.', keep_spaces=True))
print(tokenize('the quick brown fox jumped, over the lazy dog.', True))

# 10.23
print('10.23')
multiply_and_add(2, 3, 5)
multiply_and_add(a=2, b=3, c=5)
multiply_and_add(c=5, a=2, b=3)
multiply_and_add(2, b=3)
multiply_and_add(2, b=3, c=5)
multiply_and_add(a=2, b=3)
multiply_and_add(b=3, a=2)

# 10.24
# def my_function(a, b=1, c): # SyntaxError: non-default argument follows default argument
#     print('test')

# 10.25
multiply_and_add(c=5, a=2, b=3)
# That rule is about function definitions, but here we are dealing with a function call. How you specify your
# arguments (as positional or keyword arguments) is independent of whether the corresponding parameters have
# defaults or not.

# 10.26
def append_to(element, l=[]):       # note: the docstring is a lie
    """
    Appends the element to the provided list, returning it, or to an empty list if none was provided (resulting in [element]).
    """
    l.append(element)
    return l

print(append_to.__defaults__)   # from 10.28

print(append_to('cat', ['dog', 'horse']))
print(append_to('cat'))

print(append_to.__defaults__)   # from 10.28

print(append_to('cat', ['mouse']))
print(append_to('cat'))

print(append_to.__defaults__)   # from 10.28

# The first call that uses the default list, append_to('cat'), changes the default list, from the initial [] to
# the singleton list ['cat']. The second call that relies on the default list, append_to('cat') again, therefore
# does not start from an empty list, contrary to appearances.

# 10.27
# None is treated as a 'placeholder' for a default value, that is replaced by an empty list *each time the function
# is executed*. This is unlike the empty list in the previous version, which was created only once at the start, when
# the function was defined.

# 10.28
print('10.28')
print(append_to.__defaults__)   # (see also above)
print(multiply_and_add.__defaults__)

# 10.29
directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

def turn_clockwise(direction, n_turns=1):
    """
    Takes a string representation of a direction and returns the new direction after
    turning n_turns 'steps' clockwise. Default is 1 step.
    """
    index = directions.index(direction)
    turned_index = (index + n_turns) % len(directions)
    return directions[turned_index]

def turn_counterclockwise(direction, n_turns=1):
    """Takes a string representation of a direction and returns the new direction after
    turning n_turns 'steps' counterclockwise. Default is 1 step."""
    index = directions.index(direction)
    turned_index = (index - n_turns) % len(directions)
    return directions[turned_index]

print(turn_clockwise('W'))
print(turn_clockwise('NE', n_turns=2))
print(turn_counterclockwise('W'))
print(turn_counterclockwise('NW', n_turns=3))

# These two functions still contain a lot of duplicated code, so there is some 'refactoring' to be done.
# There will be an exercise about this later.

