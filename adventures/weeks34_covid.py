import pandas as pd
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import textblob

"""
Code for the VaxSentimentizer3000©
Input: Tweets about COVID
Output: a plot of COVID vaccination sentiment trough time (and more)

Make sure to download the data and update the path_to_data if necessary. 

Suggestions for further exploration:
- Look at a narrower time window (e.g., only the week before vs week after approval)
- Manually look at the tweets and sentiment values to assess the quality.
- Adopt a more sophisticated sentiment classifier.
- Compare emoji-based and TextBlob-based sentiment (e.g., correlation analysis).
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
    dataset['date'] = [extract_date(time) for time in dataset['created_at']]
    dataset['sentiment'] = [extract_sentiment(text) for text in dataset['full_text']]
    dataset['is_about_vaccine'] = [is_about_vaccine(text) for text in dataset['full_text']]
    date_of_vaccine_approval = datetime.date(2021, 8, 14)
    dataset['tweeted_after_approval'] = [d >= date_of_vaccine_approval for d in dataset['date']]


def explore_data(dataset):
    print(dataset)
    print(dataset.columns)
    print(dataset.dtypes)

    # do we have tweets for all dates?
    # plot separately for vaccine-related and other tweets.
    sns.histplot(data=dataset, x='date', hue='is_about_vaccine', multiple='stack')
    plt.show()


def extract_sentiment(text):
    """
    Returns the sentiment float [-1, 1] of our text (tweet) according to textblob.
    """
    blobbed_text = textblob.TextBlob(text)
    return blobbed_text.sentiment.polarity


vaccine_related_strings = ['vaccin', 'vax', 'jab', 'booster', 'moderna', 'pfizer', 'poison', ' rna', 'needle', 'fda']
# Warning: don't use too short sequences or they'll be in many other words too (or add spaces).

def is_about_vaccine(text):
    """
    Return a boolean indicating whether the text (tweet) is about the vaccine or not.
    """
    text = text.lower()
    for keystring in vaccine_related_strings:
        if keystring in text:
            return True
        # else:                # doesn't quite work as we want
        #     return False
    return False


def extract_date(time):
    """
    Read a date/time string with the format of our dataset, and turn it into a date object.
    """
    time = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
    return time.date()


def analyze_sentiment_over_time(dataset):
    sns.lineplot(data=dataset, x='date', y='sentiment', hue='is_about_vaccine')
    plt.show()


def analyze_sentiment_before_and_after_approval(dataset):
    sns.barplot(data=dataset, x='tweeted_after_approval', y='sentiment', hue='is_about_vaccine')
    plt.show()


# https://unicode.org/emoji/charts-12.0/emoji-ordering.html
# also interesting: https://www.nature.com/articles/s41598-021-04357-7
smiling = '😀 😃 😄 😁 😆 😅 🤣 😂 🙂 🙃 😉 😊 😇'.split()
affection = '🥰 😍 🤩 😘 😗 ☺ 😚 😙'.split()
tongue = '😋 😛 😜 🤪 😝 🤑'.split()
sceptical = '🤐 🤨 😐 😑 😶 😏 😒 🙄 😬 🤥'.split()
concerned = '😕 😟 🙁 ☹ 😮 😯 😲 😳 🥺 😦 😧 😨 😰 😥 😢 😭 😱 😖 😣 😞 😓 😩 😫 🥱'.split()
angry = '😤 😡 😠 🤬 😈 👿 💀 ☠'.split()

positive = smiling + affection + tongue
negative = sceptical + concerned + angry

def extract_sentiment_by_emoji(text):
    """
    Counts positive and negative emoji and returns a sentiment value between -1 and 1.
    """
    pos_count = 0
    for emoji in positive:
        pos_count += text.count(emoji)
    neg_count = 0
    for emoji in negative:
        neg_count += text.count(emoji)
    if pos_count == neg_count:
        return 0
    return (pos_count - neg_count) / (pos_count + neg_count)


# This makes sure the function we called 'main' (could have called it 'blabla', doesn't matter)
# is only called if this file is run as a separate script, and NOT if this file is 'imported'
# into another file. Don't worry, we'll learn about this in later exercises.
if __name__ == "__main__":
    main()