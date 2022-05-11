
### Name: ________________

## Python for Linguists

### Mini-exam 10

Write a program that, given a path to some text file, counts the part-of-speech-bigrams' and writes these to a new file, _ordered from most to least frequent_. The created file should have lines like this:

---

```
DET,NOUN,521
NOUN,VERB,487
DET,ADJ,387
VERB,DET,321
...
```

---

This would represent that, in the analyzed text, determiners are followed 521 times by a noun, nouns 487 times by a verb, etc.

#### Suggested starting point:

---

```python
import spacy
import collections

input_path = 'some_text.txt'
output_path = 'pos_ngrams.csv'

test_text = 'The quick brown fox jumped.'
test_pos = ['DET', 'ADJ', 'ADJ', 'NOUN', 'VERB', 'PUNCT']

nlp = spacy.load('en_core_web_sm')
```

---

#### Advice:
If you cannot get something to work, comment-out your partial solution and continue with a simple substitute. For example:

- use `test_text` if you can't get reading from a file to work;
- use `test_pos` if you're not sure how to get parts of speech from spaCy;
- just `print` the resulting counts if you're not sure how writing to a file works.
