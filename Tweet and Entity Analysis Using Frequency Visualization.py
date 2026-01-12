import tweepy
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt

# Download NLTK resources (run once)
nltk.download('punkt')
nltk.download('stopwords')

# Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate with Twitter
auth = tweepy.OAuth1UserHandler(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
api = tweepy.API(auth)

# Fetch tweets
def fetch_tweets(query, count=100):
    tweets = api.search_tweets(q=query, count=count)
    return tweets

# Preprocess text
def preprocess_text(text):
    words = word_tokenize(text.lower())
    stopwords_set = set(stopwords.words('english'))
    filtered_words = [
        word for word in words
        if word.isalnum() and word not in stopwords_set
    ]
    return filtered_words

# Frequency analysis
def perform_frequency_analysis(tweets):
    text = ' '.join([tweet.text for tweet in tweets])
    processed_text = preprocess_text(text)
    word_freq = Counter(processed_text)
    return word_freq

# Visualization
def visualize_results(word_freq, top_n=10):
    top_words = dict(word_freq.most_common(top_n))
    plt.figure(figsize=(10, 5))
    plt.bar(top_words.keys(), top_words.values())
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.title(f"Top {top_n} Most Frequent Words in Tweets")
    plt.xticks(rotation=45)
    plt.show()

# Main execution
query = "python programming"
tweets = fetch_tweets(query)
word_freq = perform_frequency_analysis(tweets)
visualize_results(word_freq)
