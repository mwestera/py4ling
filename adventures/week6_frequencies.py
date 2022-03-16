

"""
Goals:
- Load a text
- Extract the vocabulary with frequencies
- Compute lexical diversity
- Plot word frequency as a function of frequency rank
    Zipf's law
"""

path_to_textfile = 'data/pg67352.txt'       # from project Gutenberg

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
    unique_tokens = set(tokens)
    counts = {token: 0 for token in unique_tokens}
    for token in tokens:
        counts[token] += 1
    return counts


def plot_frequency_by_rank(counts):
    ...


if __name__ == '__main__':
    main()
