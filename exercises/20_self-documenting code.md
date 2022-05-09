# Python for linguists


## 20. Self-documenting code

**20.1.** A Python 'style guide' is kept in the eighth _Python Enhancement Proposal_, PEP8 (https://www.python.org/dev/peps/pep-0008/). Have a look at it! List some relevant guidelines that you were already familiar with, and some that you were unaware of.

**20.2.** Does the PyCharm editor warn you of violations of Python style? Construct some code examples to test/demonstrate this.

- - - - - -
**Something to keep in mind:** Adherence to the Python styleguide **PEP8** is not a goal in and of itself (...unless you write Python as an art form), but serves primarily to increase the **clarity** and thereby also **safety** of your code: it increases the verifiability (and likelihood) that your code is actually computing what you think it does.
- - - - -

**20.3.** Reflect on the importance of writing clear and safe code, comparing developing applications as well as research, individual as well as collaborative work.

**20.4.** Virtually every aspect of the Python language has been purposefully designed, even though we may not always understand the purpose. Should you find yourself frustrated with Python, just enter `import this` in the interpreter and feel your calm returning. The result is an 'easter egg' based on PEP20, that captures some of Python's design principles in poetic form.

**20.5.** From memory, make a list of the Python keywords and built-ins that you have learned about in this course so far. In line with PEP20, there is usually one preferred way of doing something. Becoming better at writing more readable (hence safer) Python code is, in large part, a matter of learning those ways.

**20.6.** So far you have been documenting your code with hashtag-comments (ignored by the Python interpreter) and with triple-quotation-marked strings. What do you believe is the purpose of each? What are differences?

**20.7.** Will the following two lists end up being equivalent? Why (not)?

```python
some_list1 = [
    'abc',
#    'def',
    'ghi',
    'jkl'
    ]

some_list2 = [
    'abc',
'''
    'def',
'''
    'ghi',
    'jkl'
    ]
```


**20.8.** When you were still unfamiliar with the Python syntax, you may have frequently added plain English translations as comments, as in the example below. Check whether you can find this type of comments in your own code from earlier sections.

```python
my_dict = {}   # create an empty dictionary
my_number = 5432   # assign integer to variable
```


**20.9.** Worse than comments that are redundant, are comments that _lie_. Identify the ways in which the following comments are unclear and/or misleading.

```python
n = input('Enter a number:')     # get an integer from the user
print(f'You entered {n}!')

my_list = ['abc', 'def', 'ghi']
my_list2 = [s[::-1] for s in my_list]   # invert the list

my_dict = {'a': 15, 'b': 20, 'c': 25}
# print each character
for x in my_dict.items():
    print(x)
```


**20.10.** Comments are easily overlooked (cf. their default color in the editor), so even if initially correct, they can easily _become_ false when modifying the code. Illustrate this, by modifying the following code for our client, who just called in to clarify what they need is the average length over token _occurrences_, not unique tokens.

```python
import re
text = 'Imagine this is some kind of text. Could be a lot longer.'
# Tokenize by finding all alphanumeric characters in between word boundaries:
tokens = re.findall(r'\b\w+\b', text)
# Print the vocabulary size:
vocabulary = set(tokens)
print(len(vocabulary))
# Print the average token length of the text:
average_length = sum([len(tok) for tok in tokens]) / len(tokens)
print(average_length)
```


**20.11.** It is clear that redundant comments (and certainly lying comments) ought to be avoided. But surprisingly often, comments can be _made_ redundant by choosing more transparent variable names. Can you change the variable name in the following snippet, so the comment can be deleted?

```python
d = {}  # will map place names to their inhabitant counts
```


**20.12.** By renaming variables, make the following code more self-documenting, and remove any comments thereby made redundant (you can make other code improvements too):

```python
mapping = {'John': '098124', 'Sue': '657317', 'Bob': '135809'}  # mapping from student names to their IDs
mapping2 = {a: b for b, a in mapping.items()}	# construct the inverse mapping

x = '657317'    # this is the student ID that I need to know the name for

if x in mapping2:
    print(new_mapping[x])	# print the student's name
```


**20.13.** For the same reason that variable names (when well-chosen) can be self-documenting, _auxiliary_ variables can increase code clarity. Improve the following code by assigning the computed value to a (meaningfully named) variable first, instead of printing it directly. Make other improvements too (including, but not limited to, using `math.pi`).

```python
c = [7, 4, 5, 8, 6, 9, 5]   # these are circle radii
for r in c:
    print(3.1415 * r**2)
```


**20.14.** Just like auxiliary _variables_, auxiliary _functions_ too can make code more self-documenting. Define a function for computing the thing that gets printed in the previous example. Having made this change, do you feel you still need the auxiliary variable introduced in the previous exercise, or can you call the function directly inside the print statement?

**20.15.** The foregoing examples show that _brevity_ is not the point, _readability_ is: The original code was shorter than either the auxiliary variable variant (1 extra line), or the auxiliary function variant (extra lines to define the function). Likewise, self-documenting variable names tend to be longer than uninformative `x` or `y`. Can you think of reasons why brevity as such is not the point?

- - - - - -
**Something to keep in mind:** Adequately named variables and functions make your code (more) **self-documenting** (why is that a good thing again?). As a rule of thumb, the greater the distance between variable assignment and variable use (or function definition and function call), the longer (i.e., more informative) its name should be.
- - - - -

**20.16.** Can you give a possible motivation for the above rule of thumb? Looking back at some of the exercise solutions for previous sections, did we generally follow this rule? In which circumstances might uninformative variable names such as `x` be acceptable?

**20.17.** Also bad for code safety are so called **magic numbers**, i.e., seemingly arbitary numbers that occur in the middle of the code. In some cases, magic numbers can be derived from existing objects instead of manually entered. Use this to improve the following code (and explain why it is an improvement):

```python
project_topics = ['sentiment analysis', 'zipf\'s law', 'collocations', 'distributional semantics']
students = ['Alf', 'Beth', 'Gemma', 'Dale', 'Ebba', 'Zod', 'Ethan', 'Philip']
team_size = 8 / 4
print(f'{team_size} students will work together on each project')
```


**20.18.** Sometimes a magic number cannot be 'derived' as in the preceding exercise, but instead it represents some type of configuration setting, to be chosen prior to running the script. This is illustrated below. First of all, can you make this more self-documenting?

```python
with open('some_existing_file.txt', 'r') as file:
    text = file.read()

text = text[:500]   # consider only first 500 characters just to test!
```


**20.19.** It is often a good idea to separate the _core program_ from the customizable _settings_ with which to run it (like the number above). Try to give several reasons, from different angles, on why such separation might be a good idea. Can you think of ways to achieve this?

**20.20.** Implement one of the ways you came up with for the above example. Improve the usability of the example further, so that choosing the value like `False` or `0` or `None` (instead of a number like `500`) will result in the entire text being used.

**20.21.** A number is 'magical' if, roughly, it hides the intent of the programmer in choosing that number (https://en.wikipedia.org/wiki/Magic_number_(programming)). Can you relate this to the concept of self-documenting code? Do you feel your earlier function for computing the area of a circle contains magic numbers?

**20.22.** Just like adequate variable and function names, the data structures used can (and should, where possible) communicate their purpose. Which Python data structures do you know by now? What are their purposes?

**20.23.** Make the following code more self-documenting (and more safe) by (with code) representing the data in a more suitable data structure before executing the query. Additional improvements are possible too. 

```python
# Names of students and the corresponding (!) student IDs.
# Warning, if you change one list make sure you change the other!
names = ['John', 'Sue', 'Bob', 'Chris']
ids = ['124987', '098513', '098122', '198732']

# find the student ID of Bob:
id = names.index("Bob")
x = ids[id]

print(x)
```


**20.24.** Do the same for the following code (explain what is less than ideal, then improve it):

```python
# student records consist of the fields name, age, id and major:
students = [
    ['John', 22, '1249871', 'linguistics'],
    ['Mary', 24, '4198712', 'psychology'],
    ['Bob', 32, '089123', 'mathematics'],
]

for x in students:
    if x[0] == 'Bob':
        print(x[2])
```


**20.25.** Make the following code more self-documenting (and again, more safe):

```python
unique_numbers = [1,6,3,2,5,7,9]

if 8 not in unique_numbers:    # check to ensure numbers remain unique
    unique_numbers.append(8)
```


**20.26.** Make the following code as clear and self-documenting as possible, taking into account all of the above considerations, about Python style, comments, variable names, auxiliary variables and functions, magic numbers, and appropriate datastructures (and the remarks about avoiding indexing, in section 19). You may have to change quite a bit!

```python
python = ['John', 'Sue', 'Bob', 'Chris', 'Peter', 'Pjotr', 'Maria']  # all students of the python for linguists class
pts = [80, 60, 43, 75, 27, 92, 94]  # points they earned for the exam
total = 100
g = [10 * i/95 for i in pts]   # only 95 because 5 points were bonus
p = [i > 5.5 for i in g]
# now print the results, followed by the number of failing students
print(list(zip(python, g)))
nf = 0
for b in p:
    if b:
        nf += 1
print(nf)
print([s for i, s in enumerate(python) if not p[i]])	# these failed the exam
```


**20.27.** Review one of the mini-adventures for which you implemented a (partial) solution, and where possible improve your code to make it more self-documenting.

