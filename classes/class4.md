# Python for Linguists

## Class 4
1. Time spent on the homework this week?  ~3 hours
2. Mini-exam 3 + discussion
3. Discuss homework (6.25, 6.32, 6.34 + list/textblob)
---break---
4. Vaccine sentiment adventure (+ clarify purpose of adventures)
5. ~~Work on exercises, from 7.11~~ no time
6. Homework for next time: Exercises 7.11-8.10 (lists, loops)
  - Also look at the adventure, and try to come up with an **is_about_vaccine** function.
  - Exercises 7.24, 7.37, 8.9, 8.10 will be discussed in class.
  - For all other questions, see office hours/forum.

### Code squibs from class

```python
import textblob

def is_determiner(word):
    return word == 'the' or word == 'a' or word == 'an'

determiners = ['the', 'a', 'an', 'many', 'some']

# list comprehension
lowercased_determiners = [det.lower() for det in determiners]

def is_determiner2(word):
    return word.lower() in lowercased_determiners

print(is_determiner2('the'))
print(is_determiner2('there'))
print(is_determiner2('the man'))
print(is_determiner2('The'))

print('----------------')

def is_determiner_in_context(sentence, index):
    """
    Given a sentence, is the token at index a determiner?
    special case of POS-tagging (part of speech)
    """
    blobbed_text = textblob.TextBlob(sentence)  # maybe try a different pos_tagger=...
    return blobbed_text.pos_tags[index][1] == 'DT'

print(is_determiner_in_context('I am near the tree', 3))
print(is_determiner_in_context('I am near the tree', 2))
print(is_determiner_in_context('I am near an elephant', 3))

# Trying to trick it:
print(is_determiner_in_context('how is An doing today?', 2))
print(is_determiner_in_context('That tree has fallen', 0))
print(is_determiner_in_context('That is a good idea', 0))

```


### TextBlob

https://textblob.readthedocs.io/en/dev/

    Noun phrase extraction
    Part-of-speech tagging
    Sentiment analysis
    Classification (Naive Bayes, Decision Tree)
    Tokenization (splitting text into words and sentences)
    Word and phrase frequencies
    Parsing
    n-grams
    Word inflection (pluralization and singularization) and lemmatization
    Spelling correction
    Add new models or languages through extensions
    WordNet integration
   

