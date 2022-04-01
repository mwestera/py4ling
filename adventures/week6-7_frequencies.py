import math

import seaborn as sns
from matplotlib import pyplot as plt

"""
Goals:
- Load a text
- Extract the vocabulary with frequencies
- Compute lexical diversity
- Plot word frequency as a function of frequency rank
    Zipf's law
"""

path_to_textfile = 'data/pg67352.txt'   # free plaintext book from Project Gutenberg, https://www.gutenberg.org/

def main():
    text = read_data(path_to_textfile)
    tokens = tokenize(text)
    explore_data(tokens)
    counts = count_tokens(tokens)
    plot_frequency_by_rank(counts)  # TODO


def explore_data(tokens):
    n_tokens = len(tokens)
    n_unique_tokens = len(set(tokens))
    print('n_tokens:', n_tokens)
    print('n_unique:', n_unique_tokens)
    print('lexical diversity:', n_unique_tokens / n_tokens)


def read_data(path):
    with open(path, 'r') as stream:     # context manager
        text = stream.read()

    return text


def tokenize(text):
    text = text.lower()
    tokens = text.replace('\n', ' ').split(' ')
    cleaned_tokens = [token.strip('.,:!;?“') for token in tokens]
    cleaned_nonempty_tokens = [token for token in cleaned_tokens if token != '']
    return cleaned_nonempty_tokens


def count_tokens(tokens):
    counts = {token: 0 for token in tokens}

    # In class we did the following, which is unnecessarily complex, as a dictionary already ensures all keys are unique:
    # unique_tokens = set(tokens)
    # counts = {token: 0 for token in unique_tokens}

    for token in tokens:
        counts[token] += 1
    return counts


def plot_frequency_by_rank(counts):

    counts = list(counts.items())

    # def get_sorting_key(t):
    #     return t[1]
    #
    # counts.sort(key=get_sorting_key)

    # more pythonic:
    counts.sort(key=lambda x: x[1], reverse=True)

    print(counts)

    tokens = [t[0] for t in counts]
    counts = [t[1] for t in counts]
    ranks = list(range(len(counts)))

    log_counts = [math.log(c) for c in counts]
    log_ranks = [math.log(r + 1) for r in ranks]    # I've put the +1 here, it felt cleaner.

    # We've seen this syntax based on dataframes:
    # sns.lineplot(data=dataframe, x='column1', y='column3')
    # You can also directly give it the x and y values as lists:
    sns.lineplot(x=log_ranks[:1000], y=log_counts[:1000])
    plt.show()


if __name__ == '__main__':
    main()
