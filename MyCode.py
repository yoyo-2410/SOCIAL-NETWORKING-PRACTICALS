import tweepy
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt

# Download NLTK resources (run once)
nltk.download("punkt")
nltk.download("stopwords")

# ===== Twitter API (Bearer Token) =====
bearer_token = "YOUR_BEARER_TOKEN_HERE"
client = tweepy.Client(bearer_token=bearer_token)

# Fetch tweets
def fetch_tweets(query, max_results=50):
    response = client.search_recent_tweets(
        query=query,
        max_results=max_results,
        tweet_fields=["text"]
    )
    return response.data

# Preprocess text
def preprocess_text(text):
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words("english"))
    filtered = [
        word for word in words
        if word.isalnum() and word not in stop_words
    ]
    return filtered

# Frequency analysis
def perform_frequency_analysis(tweets):
    combined_text = " ".join(tweet.text for tweet in tweets)
    processed_words = preprocess_text(combined_text)
    return Counter(processed_words)

# Visualization
def visualize_results(word_freq, top_n=10):
    common_words = dict(word_freq.most_common(top_n))
    plt.figure(figsize=(10, 5))
    plt.bar(common_words.keys(), common_words.values())
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.title(f"Top {top_n} Most Frequent Words in Tweets")
    plt.xticks(rotation=45)
    plt.show()

# ===== Main Execution =====
query = "python programming -is:retweet"
tweets = fetch_tweets(query)

if tweets:
    freq = perform_frequency_analysis(tweets)
    visualize_results(freq)
else:
    print("No tweets found")
