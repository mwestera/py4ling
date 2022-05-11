import spacy
import collections

input_path = '../../adventures/data/gutenberg/alice_pg35688.txt'
output_path = 'pos_ngrams.csv'

# test_text = 'The quick brown fox jumped.'
# test_pos = ['DET', 'ADJ', 'ADJ', 'NOUN', 'VERB', 'PUNCT']

nlp = spacy.load('en_core_web_sm')


with open(input_path, 'r') as file:
    text = file.read()

doc = nlp(text)
parts_of_speech = [tok.pos_ for tok in doc]
pos_bigrams = [(parts_of_speech[i], parts_of_speech[i + 1])
               for i in range(len(parts_of_speech)-1)]

# More Pythonic:
# pos_bigrams = list(zip(parts_of_speech, parts_of_speech[1:]))

pos_bigram_counter = collections.Counter(pos_bigrams)

with open(output_path, 'w') as file:
    for pos_pair, count in pos_bigram_counter.most_common():
        file.write(f'{pos_pair[0]},{pos_pair[1]},{count}\n')
    # for (pos1, pos2), count in pos_bigram_counter.most_common():
        # file.write(f'{pos1},{pos2},{count}\n')

