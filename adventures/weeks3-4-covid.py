import pandas as pd
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import textblob

"""
Code for the VaxSentimentizer3000©
Input: Tweets about COVID
Output: a plot of COVID vaccination sentiment trough time
"""


path_to_our_data = 'data/twitter_covid_001.csv'
max_n_tweets = 1000     # small is more convenient for quick testing


def main():
    dataset = load_data(path_to_our_data)
    compute_features(dataset)
    explore_data(dataset)
    analyze_sentiment_over_time(dataset)
    analyze_sentiment_before_and_after_approval(dataset)


def load_data(path):
    return pd.read_csv(path, nrows=max_n_tweets)


def compute_features(dataset):
    # These all use list comprehension (exercises about this in two weeks time)
    dataset['date'] = [extract_time(time) for time in dataset['created_at']]
    dataset['sentiment'] = [extract_sentiment(text) for text in dataset['full_text']]
    dataset['is_about_vaccine'] = [is_about_vaccine(text) for text in dataset['full_text']]

    # I added the following after class, in anticipation of next week
    date_of_vaccine_approval = datetime.date(2021, 8, 14)
    dataset['tweeted_after_approval'] = [d >= date_of_vaccine_approval for d in dataset['date']]


def explore_data(dataset):
    print(dataset)
    print(dataset.columns)
    print(dataset.dtypes)

    # do we have tweets for all dates?
    sns.histplot(data=dataset, x='date')
    plt.show()


def extract_sentiment(text):
    """
    Returns the sentiment float [-1, 1] of our text (tweet) according to textblob.
    """
    blobbed_text = textblob.TextBlob(text)
    return blobbed_text.sentiment.polarity


def is_about_vaccine(text):
    """
    Return a boolean indicating whether the text (tweet) is about the vaccine or not.
    """
    ...  # homework :)


def extract_time(time):
    """
    Read a date/time string with the format of our dataset, and turn it into a date object.
    """
    time = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
    return time.date()


def analyze_sentiment_over_time(dataset):
    ...


def analyze_sentiment_before_and_after_approval(dataset):
    ...


# This makes sure the function we called 'main' (could have called it 'blabla', doesn't matter)
# is only called if this file is run as a separate script, and NOT if this file is 'imported'
# into another file. Don't worry, we'll learn about this in later exercises.
if __name__ == "__main__":
    main()