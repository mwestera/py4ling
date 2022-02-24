import pandas as pd


"""
Code for the VaxSentimentizer3000©
Input: Tweets about COVID
Output: a plot of COVID vaccination sentiment trough time
This is currently just a squib. It will be completed in class in week 4.
"""


path_to_our_data = 'data/twitter_covid.csv'  # NB. This was different in class (I moved the folder)

# NOTE: If you want to run this at home, uncomment this (twitter does not allow broad sharing of tweet contents):
# path_to_our_data = 'data/twitter_covid_sample.csv'


# Read the csv file
# 1. Can I solve this quite easily? No.
# 2. Is it likely that someone else has solved this? Very.
# Hence we google, e.g., 'how to read a csv file using python'

dataset = pd.read_csv(path_to_our_data)


# Preprocessing/cleaning the data, e.g.:
#   - do we have tweets from all time points?
#   - any non-covid tweets?
#   - filter out empty/weird/unanalyzable tweets
# 1. can we do this easily ourselves? Nope.
# 2. Is it likely that someone has solved this before us? Yes, very!
#      What should we google for?   [to be continued!]

print(dataset['created_at'].to_string())


# Take the text, compute its vaccine sentiment as a float, e.g., using:
# - keywords, keyphrases, syntax
# - hashtags
# - some machine learning
# - beware of sarcasm?


# Aggregate data for each time point (mean, std)



# Generate a plot