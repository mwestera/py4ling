# Python for Linguists
### Mini-exam 3

1. What does the following program print (when run from a python file)?
2. Change (only) the `greet` function, so that what it prints will start with a capital letter.

----

```python
def create_greeting(language):
    if language == 'English':
        return 'hello'
    elif language == 'French':
        return 'bonjour'
    else:
        return 'I don\'t speak ' + language


def greet(language, emotion):
    greeting = create_greeting(language)
    if emotion == 'sad':
        greeting += '...'
    else:
        greeting += '!'
    print(greeting)


greet('French', 'sad')
greet('Dutch', 'angry')
print(create_greeting('English'))
print(greet('English', 'happy'))
```

----

(Don't forget the second task listed above, about capitalization!)