from nltk.corpus import brown, stopwords
from week67_frequencies import count_tokens
from operator import itemgetter
import pandas as pd
import math
import os
import gensim
import gensim.downloader as api

import random

"""
Here's the plan:
1. load a big-ish text corpus
2. represent each word by some sort of mathematical object representative of the contexts in which it occurs
    compute a cooccurrence matrix ~ high-dimensional space
3. given these representations, how similar are two words?
    computing the distance between the words vector representations gi en the cooccurrence matrix
    'woman' 'man'    not so similar to 'car
4. Now that we have an idea of the underlying mechanics, implement the same but via popular library gensim.
5. (Improvised) Implement the Semantle game.

Some things left to improve/explore:
- add dimensionality reduction to the manual implementation
- make Semantle work also with our own manual implementation
- use different/larger dataset to train word vectors to see the effect
- add proper docstrings :$
"""

N_TOKENS = 500
WINDOW = 20
REDO = False # Whether to recompute the cooccurrence counts if the file already exists
SAVE_PATH = 'cooccurrences.pkl'
USE_GENSIM = True
CUSTOM_WORD2VEC = False # only if USE_GENSIM; if False, uses Google's model.
PLAY_SEMANTLE_AFTERWARDS = True # only if USE_GENSIM
SEMANTLE_OPEN = False   # Set to True for Semantle to reveal the target word beforehand.

def main():
    if USE_GENSIM:
        gensim_variant()
    else:
        manual_variant()


def manual_variant():

    if REDO or not os.path.exists(SAVE_PATH):
        tokens = [tok.lower() for tok in brown.words()]
        tokens_to_use = determine_words_we_will_use(tokens, N_TOKENS)
        matrix = cooccurrence_matrix(tokens, tokens_to_use, WINDOW)
        matrix.to_csv(SAVE_PATH)
    else:
        matrix = pd.read_csv(SAVE_PATH, index_col=0)

    # wv = dimensionality_reduction(matrix)     # Not done yet; see class notes
    wv = matrix

    for word in ['young', 'man', 'woman', 'person', 'car', 'love', 'hand']:
        print(word, most_similar(word, wv))


def gensim_variant():
    if CUSTOM_WORD2VEC:
        wv = get_custom_word2vec()
    else:
        wv = get_google_word2vec()

    for word in ['young', 'man', 'woman', 'person', 'car', 'love', 'hand']:
        print(word, wv.most_similar(word))

    # Example of analogical reasoning, which Word2Vec is famous for (e.g., king is to man as queen is to woman):
    print(wv.most_similar('king'))
    print(wv.most_similar(positive=['king', 'woman'], negative=['man']))    # king - man + woman

    # Just to try if this makes a difference:
    print(wv.most_similar(positive=['king', 'woman', 'woman', 'woman'], negative=['man']))    # king - man + woman

    if PLAY_SEMANTLE_AFTERWARDS:
        semantle(wv)

def get_custom_word2vec():
    if REDO or not os.path.exists(SAVE_PATH):
        model = gensim.models.Word2Vec(sentences=brown.sents())
        model.save(SAVE_PATH)
    else:
        model = gensim.models.Word2Vec.load(SAVE_PATH)

    wv = model.wv

    return wv

def get_google_word2vec():
    wv = api.load('word2vec-google-news-300')  # 1.6 GB!
    return wv


def semantle(wv):
    while True:
        secret_word = random.choice(wv.index_to_key)
        if secret_word == secret_word.lower():
            break
    if SEMANTLE_OPEN:
        print(secret_word)
    n_attempts = 0
    while True:
        guess = input('Guess!').lower()
        n_attempts += 1
        if guess == secret_word:
            print(f'Wooohoooh! In {n_attempts} attempts!')
            break
        try:
            similarity = wv.similarity(secret_word, guess)
        except:
            print('Word not found.')
            continue
        print('   ', similarity)


def determine_words_we_will_use(tokens, nwords=None):
    """
    Returns a subset of the <nwords> most frequent tokens that are not stopwords.
    If nwords is not given, returns all words that are not stopwords.
    """

    english_stopwords = stopwords.words('english')
    nonstop_tokens = [tok for tok in tokens if tok not in english_stopwords]

    counts = count_tokens(nonstop_tokens)

    counts = list(counts.items())
    counts.sort(key=itemgetter(1), reverse=True)      # functionally same as lambda x: x[1]

    if nwords:
        counts = counts[:nwords]

    return [tup[0] for tup in counts]




def cooccurrence_matrix(tokens, tokens_to_use, window=3):
    """
    Returns a pandas dataframe representing the cooccurrences of the tokens_to_use,
    in the corpus represented by tokens, based on a neighborhood window.
    """
    cooccurrence_counts = {tok: {tok2: 0 for tok2 in tokens_to_use} for tok in tokens_to_use}

    for i, token in enumerate(tokens):
        if token in tokens_to_use:
            left_neighbors = tokens[max(0, int(i-window/2)):i]
            right_neighbors = tokens[i+1:i+1+int(window/2)]
            for neighbor in left_neighbors + right_neighbors:
                if neighbor in tokens_to_use:
                    cooccurrence_counts[token][neighbor] += 1

    matrix = pd.DataFrame(cooccurrence_counts).fillna(0)

    # Normalize the vectors (matrix rows); dividing each vector by the magnitude (or norm, or length) is only
    #    one of several possibilities.
    for word in matrix.index:
        matrix.loc[word] /= magnitude(matrix.loc[word])

    return matrix


def magnitude(vector):
    """
    Returns magnitude (norm) of the vector, Pythagoras style.
    """
    return math.sqrt(sum(a**2 for a in vector))


def most_similar(word, matrix, n=10):
    """
    Returns a list of top N words most similar to word, given a cooccurrence matrix.
    """
    vector1 = matrix.loc[word]
    distances = []
    for word2 in matrix.index:
        if word2 == word:
            continue
        vector2 = matrix.loc[word2]
        dist = distance(vector1, vector2)
        distances.append((word2, dist))
    distances.sort(key=itemgetter(1))
    return distances[:n]


def distance(vector1, vector2):
    """
    Euclidean distance between two vectors (as points) in space.
    TODO: Hmmm, we could define this in terms of the magnitude.
    """
    return math.sqrt(sum((a-b)**2 for a, b in zip(vector1, vector2)))


if __name__ == '__main__':
    main()