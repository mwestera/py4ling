"""
Solution to mini-exam 4
"""

names = ['Ann', 'Bob', 'Chris']


def print_list_reverse(l):
    l_reversed = l[::-1]
    for name in l_reversed:
        print(name)

    # Also good variant:
    # for name in l[::-1]:
    #     print(name)

print_list_reverse(names) # should print Chris Bob Ann on separate lines.


def initials_to_string(l):
    result = ''
    for name in l:
        initial = name[0]
        # result = result + initial     # also works
        result += initial
    return result

    # via a list, also good solution:
    # result = []
    # for name in l:
    #     initial = name[0]
    #     result.append(initial)
    # return ''.join(result)

print(initials_to_string(names))