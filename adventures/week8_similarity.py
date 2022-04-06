from nltk.corpus import brown, stopwords
from week67_frequencies import count_tokens
from operator import itemgetter
import pandas as pd

"""
1. load a big-ish text corpus
2. represent each word by some sort of mathematical object representative of the contexts in which it occurs
    compute a cooccurrence matrix ~ high-dimensional space
3. given these representations, how similar are two words?
    computing the distance between the words vector representations gi en the cooccurrence matrix
    'woman' 'man'    not so similar to 'car'
"""

N_TOKENS = 10


def main():
    tokens = [tok.lower() for tok in brown.words()]
    tokens_to_use = determine_words_we_will_use(tokens, N_TOKENS)
    matrix = cooccurrence_matrix(tokens, tokens_to_use)

    print(most_similar('young', matrix))
    print(most_similar('man', matrix))
    print(most_similar('woman', matrix))


def determine_words_we_will_use(tokens, nwords=None):
    # remove stopwords
    # restrict attention to the top 500 most frequent non-stopwords

    english_stopwords = stopwords.words('english')
    nonstop_tokens = [tok for tok in tokens if tok not in english_stopwords]

    counts = count_tokens(nonstop_tokens)

    counts = list(counts.items())
    counts.sort(key=itemgetter(1), reverse=True)      # functionally same as lambda x: x[1]

    if nwords:
        counts = counts[:nwords]

    return [tup[0] for tup in counts]




def cooccurrence_matrix(tokens, tokens_to_use, window=20):
    cooccurrence_counts = {tok: {tok2: 0 for tok2 in tokens_to_use} for tok in tokens_to_use}

    for i, token in enumerate(tokens):
        if token in tokens_to_use:
            neighbors = tokens[max(0, int(i-window/2)):i] + tokens[i+1:i+1+int(window/2)]
            for neighbor in neighbors:
                if neighbor in tokens_to_use:
                    cooccurrence_counts[token][neighbor] += 1

    matrix = pd.DataFrame(cooccurrence_counts).fillna(0)
    print(matrix)




def most_similar(word, matrix, n=10):
    pass


if __name__ == '__main__':
    main()