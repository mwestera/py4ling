import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr

"""
Our second adventure (week 5): analyze correlation between word length and concreteness.

Suggestions for further exploration:
- Restricting attention to the single words (because bigrams are probably longer, but not necessarily less concrete).
- Check if the correlation exists also in sub-segments, e.g., word lenghts between 2 and 10, between 10 and 20. 
- Check if particular characters, syllables or morphemes differ in concreteness.
"""


# Data from https://link.springer.com/article/10.3758/s13428-013-0403-5
path_to_data = 'data/concreteness/Concreteness_ratings_Brysbaert_et_al_BRM.txt'


def main():
    dataset = load_dataset(path_to_data)
    compute_features(dataset)
    explore_data(dataset)
    correlation_length_concreteness(dataset)


def load_dataset(path_to_data):
    return pd.read_csv(path_to_data, sep='\t', keep_default_na=False, na_values=['#N/A'])
    # When computing word lengths, we discovered the error where the word 'nan' was treated by
    # pandas as 'not a number'/'missing value'. We then fixed it by overriding pandas default
    # 'not a number' strings, in the function load_dataset, with the na-related arguments above.


def compute_features(dataset):
    dataset['Word_length'] = [len(word) for word in dataset['Word']]


def explore_data(dataset):
    sns.histplot(data=dataset, x='Word_length')
    plt.show()
    sns.histplot(data=dataset, x='Conc.M')
    plt.show()
    print(dataset)


def correlation_length_concreteness(dataset):
    # points overlap a lot because the x-axis are integer values;
    #   the jitter function gets rid of this by distorting the values on the x-axis.
    #   (In class there was a slight bug in jitter where it transposed the word lengths by 10, now fixed.)
    sns.scatterplot(data=dataset, x=jitter(dataset['Word_length']), y='Conc.M')
    plt.show()

    # compute the statistic
    result = pearsonr(dataset['Word_length'], dataset['Conc.M'])
    print('correlation (and p-value):', result)   # correlation coefficient and p-value



def jitter(values):
    """
    Adds a small random amount (normally distributed around 0) to each value and returns the new values.
    """
    return values + np.random.normal(0, 0.2, values.shape)


if __name__ == '__main__':
    main()