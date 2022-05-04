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


def ngrams(sentence, n, as_strings=False, word_tokenize=True):
    """
    Returns a list of n-grams of the sentence, each ngram either a list (default) or a string.
    """
    if word_tokenize:    # Changed to also work on character level, for section 16
        tokens = tokenize(sentence)
    else:
        tokens = list(sentence)  # use the characters as tokens
    ngrams = [tuple(tokens[i:i+n]) for i in range(len(tokens) - (n - 1))]   # Changed to return tuples, in section 16
    if as_strings:
        ngrams = [' '.join(ngram) for ngram in ngrams]  # change requested by client, from 11.12
    # Of course you can also achieve this without list comprehension, and without join, by using.
    # multi-line loops.
    return ngrams


def read_from_gutenberg(path):
    """
    A Gutenberg Project text-file reading function, coded for exercises 15.41-15.45.
    Returns both the text (string) and some meta-info (dictionary) extracted from the file.
    """
    meta_info = {}
    lines = []
    with open(path, 'r') as infile:
        main_content = False
        for line in infile:
            if line.startswith('*** START OF'):
                main_content = True
                continue
            if line.startswith('*** END OF'):
                break
            if main_content:
                lines.append(line)
            elif ':' in line:
                key, value = line.split(':')
                key = key.strip()
                value = value.strip()
                meta_info[key] = value

    text = ''.join(lines)
    text = text.replace('\n\n', '<NEWLINE>').replace('\n', ' ').replace('<NEWLINE>', '\n')
    return text, meta_info