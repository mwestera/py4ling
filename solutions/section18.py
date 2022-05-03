"""
18. Advanced text processing
"""

import collections
import spacy
import text_utils
import re
import random

# 18.1
# Chances are you found simple approaches to tokenization based on `str.split` or `re.split`,
# and more advanced approaches using libraries such as `NLTK`, `spaCy`, `TextBlob` (based
# on `NLTK`) and `Stanza`. Of these, `spaCy` is the most widely used (and in fact offers
# integration with `TextBlob` and `Stanza` through the libraries `spacytextblob` and `spacy-stanza`).

# 18.2
# Write your own answer.
# You probably found this: https://spacy.io/usage/spacy-101
# And possibly this, for a bit more info: https://spacy.io/usage/linguistic-features

# 18.3
# It says 66+ languages (https://spacy.io/usage/facts-figures) but
# the amount of support (e.g., quality of the models) can vary.
# The models page (https://spacy.io/usage/models) shows full 'pipelines'
# only for around 25 languages, with only basic 'language data' (used for
# e.g. tokenization) available for the others.
# The rest of the answer is up to you!

# 18.4
# Formulate your own answer, for instance based on: https://spacy.io/usage/spacy-101#pipelines
# Doc objects are created from a string by a spaCy tokenizer, and enriched with further
# linguistic annotations (e.g., named entities, parts of speech) by a spaCy pipeline.
# See also https://spacy.io/usage/spacy-101#architecture for the central datastructures.

# 18.5
print('18.5')
tricky_string = '''
Prof. Dr. Tricky wrote an exclamation mark "!" at the end of the line. And what about
a sentence containing a newline? Hmm... that seems to work.
Abbreviations, known like etc. and Mr. or unknown like Dutch a.u.b. meaning please?
'''

nlp = spacy.load('en_core_web_sm')
doc = nlp(tricky_string)
print([sent.text for sent in doc.sents])

# 18.6
print('18.6')
tricky_string2 = '''
Can Spacy deal with hyphen-
ated words? Nope :)
And what does it think of emoji? :( :S Only some.
Possessive: John's kids?
Parentheses like (un)attentive?
Abbreviations, known like etc. and Mr. or unknown like Dutch a.u.b.?
Or very weird quotation marks? Beth said „test“ and then ‟test” and ❮test❯.
'''

doc2 = nlp(tricky_string2)
print([tok.text for tok in doc2])

# 18.7
# There are various possible answers. Key component of any answer should be a
# comparison to a 'ground truth', say, expert human judgments. Given this, one could
# look, for instance, at 'precision' (what proportion of identified tokens correspond
# to an actual token in the text) or 'recall' (what proportion of actual tokens in the
# text is identified as such by the tokenizer). One should always check the quality
# of an algorithm for the target genre.

# 18.8
# Up to you.

# 18.9
# Up to you.

# 18.10
print('18.10')
print(doc[3])

# 18.11
print('18.11')
# print(doc.sents[3]) # does not work
print(list(doc.sents)[3])

# 18.12
print('18.12')

def print_tokens(doc):
    print(doc.text)
    for tok in doc:
        print(f'{tok} <{tok.lemma_}> ({tok.pos_}, {tok.dep_} of {tok.head}) [{tok.ent_type_}] {tok.morph}')
        # morph was added for 18.25

print_tokens(nlp('Bob thinks Mary likes him.'))

# 18.13
print('18.13')

def count_pos(doc):
    return collections.Counter(token.pos_ for token in doc)

gutenberg_path = '../adventures/data/gutenberg/sherlock_1661-0.txt'
text, meta_info = text_utils.read_from_gutenberg(gutenberg_path)
text = text[:64000]  # shorten this a bit to save time.

gutenberg_doc = nlp(text)

print(count_pos(gutenberg_doc).most_common(10))

# 18.14
print('18.14')
def count_named_entities(doc):
    return collections.Counter(ent.label_ for ent in doc.ents)

print(count_named_entities(gutenberg_doc).most_common(10))

# 18.15
# Up to you. Can you think of a procedure for (roughly) translating between the two representations?

# 18.16
print('18.16')

print_tokens(nlp('John sees Mary.'))
print_tokens(nlp('John snores loudly.'))
print_tokens(nlp('The donkey walks in the green field.'))

# 18.17
print('18.17')
print(list(nlp('John snores loudly.').sents)[0].root)
# Only a 'sentence' has a root node, not a 'Doc'; we can use list(...)[0] to access the
# first (and in this case only) sentence.

# 18.18
def spacy_sent(string):
    """
    Applies spacy to a string (intended to be a single sentence) and returns the spacy analysis
    for the first sentence only.
    """
    doc = nlp(string)
    # nlp is a global variable, not great for encapsulation! It would be safer,
    # but less convenient, to provide nlp as an argument to the function.
    first_sent = list(doc.sents)[0]
    # Arguably more Pythonic:
    # first_sent = next(doc.sents)
    # (Calling `next` on an iterator gets its next element, i.e., the first element if we do it only once.)
    return first_sent


# 18.19
print('18.19')

def get_verb_frame(sentence):
    """
    Return the main verb and its nsubj and dobj arguments (if present).
    """
    arguments = [t for t in sentence.root.children if t.dep_ in ['nsubj', 'dobj']]
    # Alternative without children (less nice):
    # arguments = [t for t in sentence if t.dep_ in ['nsubj', 'dobj'] and t.head == sentence.root]
    return sentence.root, *arguments
    # Recall the asterisk means 'unpacking' a list into a sequence expression.
    # Its effect is that of returning a single tuple with the root and all children.
    # There are other, asterisk-free ways of achieving the same, of course.

test_sentences = 'Mary hit John with a broom in the attic. John noticed that Mary was sad.'

for sent in nlp(test_sentences).sents:
    print(sent, get_verb_frame(sent))


# 18.20 & 18.21
def print_dependency_tree(node, indent=''):
    print(indent, f'{node.dep_}: {node.text}')
    for child in node.children:
        print_dependency_tree(child, indent + '  ')

example_sentences = 'John saw Mary. John sleeps very noisily. Mary knows that John snores.'

doc = nlp(example_sentences)

for sent in doc.sents:
    print('\nSentence:', sent.text)
    print_dependency_tree(sent.root)

# There is no infinite loop because the recursion stops for any leaf node (i.e., that has no children).

# 18.22
print('18.22')
sentence = 'Sherlock Holmes hated Watson and me, as we went to the city. In London I saw Dr. S. Holmes\'s dad. I also saw Watson\'s brother\'s sister\'s mother. Running is nice. The act of running is nice. In the end everyone dies. He himself was happy.'
doc = nlp(sentence)
for chunk in doc.noun_chunks:
    print(chunk)

for tok in chunk:   # yes, can do.
    print(tok)

# 18.23
print('18.23')

# print(chunk.pos_)   # nope, error.
# print(chunk.dep_)   # nope, error.
print(chunk.root.dep_)  # yep!

# 18.24
print('18.24')
male_pronouns = ['he', 'him', 'his', 'himself']
female_pronouns = ['she', 'her', 'herself']

# Let's determine this by looking at noun chunks, not individual tokens. For pronouns,
# this doesn't matter, as they are single-token noun chunks anyway. But one could imagine
# a future extension of this research to e.g. proper names and common nouns...

def get_gender(noun_chunk):
    """
    Return gender of noun_chunk referent, currently only implemented for pronouns, otherwise None.
    """
    # To be extra safe, one could also check the POS of the noun_chunk.root,
    # to see if we are really dealing with a pronoun here...
    if noun_chunk.text in male_pronouns:
        return 'male'
    elif noun_chunk.text in female_pronouns:
        return 'female'
    else:
        return None  # not needed (remember why?), but better to be explicit about this case's existence

# Simple version:
genders = [get_gender(chunk) for chunk in gutenberg_doc.noun_chunks]
print(collections.Counter(genders))

# More flexible version, storing gender in the noun chunk spans themselves.
# Explanation here: https://spacy.io/usage/processing-pipelines#custom-components-attributes
# First tell spacy that we'll use 'gender' as an additional attribute on our spans (e.g., noun chunks)
spacy.tokens.Span.set_extension('gender', default=None)

# Then we can set the custom attribute like this:
for chunk in gutenberg_doc.noun_chunks:
    chunk._.gender = get_gender(chunk)

print(collections.Counter(chunk._.gender for chunk in gutenberg_doc.noun_chunks))

# 18.25
print('18.25')

chunks_to_count = [chunk for chunk in gutenberg_doc.noun_chunks if chunk.root.dep_ in ['nsubj', 'dobj']]

# Let's represent them slightly differently, for easy counting of the cases:
countable_pairs = [(chunk._.gender, chunk.root.dep_) for chunk in chunks_to_count]
# Note how the more flexible approach pays off, as gender has become simply another
# chunk attribute to check.

counts = collections.Counter(countable_pairs)
print(counts)

# Here is one way to quantify the 'subject-ness' of female vs male words:
female_subject_odds = counts[('female', 'nsubj')] / counts[('female', 'dobj')]
male_subject_odds = counts[('male', 'nsubj')] / counts[('male', 'dobj')]

print(f'male: {male_subject_odds:.2f}, female: {female_subject_odds:.2f}')

# Women seem slightly less subjecty in this text, but it is not a big difference, so probably not
# significant with so little data. Do you remember from statistics class how one might test for
# significance (refresher in the next section)?

# 18.26
# One would need word lists of gendered names, or at least of specific names in the domain of interest.
# For common nouns one would need a dictionary of gendered common nouns; a potential problem is that there
# may be more traditionally male than traditionally female jobs, hence fewer female common nouns to start
# with, regardless of the actual distribution of male/female in a text.

# 18.27
# Up to you; if you didn't use spaCy's 'morph' feature, this may end up being a substantial bit of code.
# If so, the next exercise will let you simplify it.

# 18.28
print('18.28')
doc = nlp('''I have seen you. I am going nowhere. I had wondered why. I was gone.''')
print_tokens(doc)

# The 'Aspect' feature is a list (maybe some verbs can have multiple aspects?), which isn't
# hashable, but it needs to be for the Counter. Hence: turn it into a tuple.
aspects = [(tuple(tok.morph.get('Aspect'))) for tok in gutenberg_doc if tok.pos_ == 'VERB']
print(collections.Counter(aspects))

# 18.29
print('18.29')

def get_path_to_root(sentence, node):
    """
    Take a sentence (not a full doc, for which root is not defined) and return path
    from node to root (including the node and root themselves).
    """
    path = [node]
    while node != sentence.root:
        node = node.head
        path.append(node)
    return path

sentence = spacy_sent('I wonder whether this function works for finding a path.')
print_dependency_tree(sentence.root)
print(sentence)
print(get_path_to_root(sentence, sentence[3]))
print(get_path_to_root(sentence, sentence[5]))
print(get_path_to_root(sentence, sentence[6]))

# 18.30
print('18.30')

# First some test sentences to familiarize ourselves with these types of clauses:
doc = nlp('''I know that the vacancy was filled. I wonder if the vacancy was truly filled.''')
print_tokens(doc)

# It appears that checking for ccomp is sufficient, though the resulting data do show a
# couple of imperfections perhaps worth ironing out:
num_prints = 0
max_prints = 3  # ugly, but just to stop this exercise from flooding the screen
for tok in gutenberg_doc:
    if num_prints > max_prints:
        break
    if tok.dep_ == 'ccomp':
        print(tok.sent)
        print(list(tok.subtree))
        num_prints += 1


# 18.31
print('18.31')

challenge_questions = [
    'And what product did you buy?',   # det of product, dobj of buy (= root)
    'And you bought what?',      # dobj of bought (= root); but for verbs like 'found' it gets ccomp instead...
    'What John did was bad?', # dobj of did (not root)
    'Did you like what you bought?',    # dobj of bought (not root)
    'Did you see who called?',  # nsubj of called (not root)
    'Who bought what?',  # nsubj and dobj of bought (root)
    'Which kids bought an airplane?',    # det of kids, nsubj of bought (root)
    'How big are you?', # advmod of big, acomp of are (root)
    'You went where?', # advmod of went (root)
    # You should probably add your own variations here, because even just changing
    # the verb can already trigger Spacy to come up with a different analysis...
    # Also consider expanding the range of wh-words.
]

for question in challenge_questions:
    print_tokens(nlp(question))
    print()

# A useful generalization seems to be: direct pathway to root (no verb in between).

wh_words = ['what', 'where', 'why', 'how', 'who', 'whom', 'when', 'which']

def extract_wh_word(sentence):
    """
    Extracts the wh-word(s) of a spacy-analyzed sentence, if any. Intended to return only
    'relevant' wh-words, i.e., that make the question a wh-question. Technically, it returns
    all the wh-words that are under the main verb, with no verb intervening. This is probably
    too simplistic (cf. island constraints on wh-movement in the syntax literature).
    """
    wh_words_found = []
    for tok in sentence:
        if tok.text.lower() in wh_words:
            for intermediate in get_path_to_root(sentence, tok)[1:-1]:
                if intermediate.pos_ == 'VERB':
                    break
            else: # executed when for-loop is not 'break'ed, i.e., when no intermediate VERB node found
                wh_words_found.append(tok)
    return wh_words_found

for question in challenge_questions:
    print(question, extract_wh_word(spacy_sent(question)))

# 18.32
print('18.32')

challenge_questions_nonwh = [
    'Did you run?',
    'You arrived yesterday?',
    'You arrive yesterday?',
    'That guy?',
    'Is that guy the famous artist you mentioned?',
]

def non_wh_question_type(sentence):
    ... # Up to you!
    return ()

# 18.33
print('18.33')
def categorize_question(question):
    sentence = spacy_sent(question)
    wh_words = extract_wh_word(sentence)
    if wh_words:
        return tuple(w.lemma_ for w in wh_words)
    else:
        return non_wh_question_type(sentence)

for question in challenge_questions:
    print(question, categorize_question(question))

# 18.34
print('18.34')

# Code from 17.54
text_slightly_cleaned = text.replace('\n', '.')
questions = re.findall(r'[^.!?]+\?+', text_slightly_cleaned)

random.seed(12345)  # Make sampling reproducible by setting the 'random seed' (not crucial)
categorized_questions = [(question, categorize_question(question)) for question in questions]

for question, category in random.sample(categorized_questions, k=10):
    print(question, '    ', category)

# Inspecting the accuracy is left to you.

# 18.35
counts = collections.Counter([category for _, category in categorized_questions])
print(counts)
# Plotting is left to you! It's a good exercise to search and adapt solutions from the web.

# 18.36
# Up to you! This might require changing extract_wh_word to extract entire phrases (such as
# 'how come' or 'for what reason', not just single words). So a first step would be to check how
# spaCy analyzes such constructions, to see if you can distill a suitable rule.

# 18.37
# There are probably some key constructions we could detect that are _almost always_ used
# to ask indirect questions (e.g., I'm wondering whether...) but for _most_ potential indirect
# questions, probably only context and pragmatics can tell us as to whether it was really used to
# indirectly ask a question or not.
