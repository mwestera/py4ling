import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import linear_model
from sklearn.metrics import precision_score, recall_score, f1_score
import wordcloud
import matplotlib.pyplot as plt

path_to_data = 'data/sentiment/sentiment.csv'
NROWS = None


def main():

    data = load_data(path_to_data)

    compute_features(data)

    data_train, data_test = train_test_split(data)

    # model_with_manual_features(data_train, data_test, ['n_pos', 'n_neg'])
    # feature engineering

    illustrate_countvectorizer()
    model_with_countvectorizer(data_train, data_test)


def load_data(path):
    return pd.read_csv(path, nrows=NROWS)


positive_words = ['good', 'best', 'great', 'superb', 'nice', 'fun', 'exciting', 'succeed', 'interesting', 'cunning', 'art', 'masterful']
negative_words = ['bad', 'worst', 'horrible', 'terrible', 'meh', 'boring', 'dull', 'fail', 'idiotic', 'lazy', 'garbage', 'amateur']

def compute_features(dataframe):
    dataframe['text_cleaned'] = [text.lower().split() for text in dataframe['text']]
    dataframe['is_positive'] = dataframe['sentiment'] == 'pos'
    dataframe['n_pos'] = [len([tok for tok in text if tok in positive_words]) for text in dataframe['text_cleaned']]
    dataframe['n_neg'] = [len([tok for tok in text if tok in negative_words]) for text in dataframe['text_cleaned']]


def model_with_manual_features(data_train, data_test, feature_names):

    X_train, y_train = data_train[feature_names], data_train['is_positive']
    X_test, y_test = data_test[feature_names], data_test['is_positive']

    model = linear_model.LogisticRegression(max_iter=500)
    model.fit(X_train, y_train)

    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    print('train:', compute_scores(y_train, y_train_pred))
    print('test:', compute_scores(y_test, y_test_pred))

    feature_analysis(model, feature_names)


def model_with_countvectorizer(data_train, data_test):

    vectorizer = CountVectorizer()
    vectorizer.fit(data_train['text'])

    X_train, y_train = vectorizer.transform(data_train['text']), data_train['is_positive']
    X_test, y_test = vectorizer.transform(data_test['text']), data_test['is_positive']

    model = linear_model.LogisticRegression(max_iter=500)
    model.fit(X_train, y_train)

    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    print('train:', compute_scores(y_train, y_train_pred))
    print('test:', compute_scores(y_test, y_test_pred))

    feature_analysis(model, vectorizer.get_feature_names_out())


def illustrate_countvectorizer():
    vectorizer = CountVectorizer()

    texts = ['the dog ate the cat',
             'the cat saw the other cat']
    vectorizer.fit(texts)
    print(vectorizer.get_feature_names_out())
    print(vectorizer.transform(texts).toarray())


def feature_analysis(model, feature_names):
    coefficients = model.coef_.squeeze()

    word_importances = list(zip(coefficients, feature_names))

    word_importances.sort()

    print("MOST NEGATIVE COEFS:")
    print(word_importances[:30])

    print("MOST POSITIVE COEFS:")
    print(word_importances[-1:-30:-1])

    weights = dict(zip(feature_names, -1 * coefficients))
    w = wordcloud.WordCloud(width=800, height=600, mode='RGBA', background_color='white', max_words=2000).fit_words(
        weights)
    plt.imshow(w)
    plt.axis("off")
    plt.show()



def compute_scores(true, pred):
    scores = {
        'precision': precision_score(true, pred),
        'recall': recall_score(true, pred),
        'f1': f1_score(true, pred),
    }
    return scores



if __name__ == '__main__':
    main()