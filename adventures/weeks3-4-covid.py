import pandas as pd


"""
Code for the VaxSentimentizer3000©
This is currently just a squib. We will start filling in more and more of this file in class in the weeks the come.
"""


# Read the csv file
# 1. Can I solve this quite easily? No.
# 2. Is it likely that someone else has solved this? Very.
# Hence we google, e.g., 'how to read a csv file using python'

path_to_our_data = '../data/twitter_covid.csv'  # move up, then down into data

# NOTE: This .csv file is not available here on github. Twitter does not allow broad sharing of tweet contents.

dataset = pd.read_csv(path_to_our_data)


# Preprocessing/cleaning the data, e.g.:
#   - do we have tweets from all time points?
#   - any non-covid tweets?
#   - filter out empty/weird/unanalyzable tweets

print(dataset['created_at'].to_string())

# 1. can we do this easily ourselves? Nope.
# 2. Is it likely that someone has solved this before us? Yes, very!
#      What should we google for?   [to be continued!]




# Take the text, compute its vaccine sentiment as a float, e.g., using:
# - keywords, keyphrases, syntax
# - hashtags
# - some machine learning
# - beware of sarcasm?


# Aggregate data for each time point (mean, std)



# Generate a plot