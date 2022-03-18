"""
File created in section 11, with text processing utilities.
"""

def tokenize(sentence):
    """
    Split the sentence into tokens, returning the list of tokens.
    """
    tokens = ['']
    for char in sentence:
        if char == ' ':
            tokens.append('')
        elif char in '.,:;?!':    # treat each punctuation mark as separate token as well
            tokens.append(char)
        else:
            tokens[-1] += char
    return tokens


def ngrams(sentence, n, as_strings=False):
    """
    Returns a list of n-grams of the sentence, each ngram either a list (default) or a string.
    """
    tokens = tokenize(sentence)
    ngrams = [tokens[i:i+n] for i in range(len(tokens) - (n - 1))]
    if as_strings:
        ngrams = [' '.join(ngram) for ngram in ngrams]  # change requested by client, from 11.12
    # Of course you can also achieve this without list comprehension, and without join, by using.
    # multi-line loops.
    return ngrams