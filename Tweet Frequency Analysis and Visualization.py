# pip install tweepy nltk matplotlib

import tweepy, nltk, matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

nltk.download("punkt")
nltk.download("stopwords")

# authentication
api = tweepy.API(tweepy.OAuth1UserHandler(
    "consumer_key",
    "consumer_secret",
    "access_token",
    "access_token_secret"
))

tweets = [
    "Learning Python is fun",
    "Coding makes life easier",
    "Practice improves programming",
    "Errors help us learn",
    "Technology changes the world"
]

def preprocess(text):
    sw = set(stopwords.words("english"))
    return [t for t in word_tokenize(text.lower()) if t.isalnum() and t not in sw]

counter = Counter(preprocess(" ".join(tweets)))

print("Top 10 Most Frequent Words in Tweets:")
for i, (w, f) in enumerate(counter.most_common(10), 1):
    print(f"{i}. {w} - {f}")

top = dict(counter.most_common(10))
plt.figure(figsize=(5, 5))
plt.bar(top.keys(), top.values(), color='purple')
plt.xlabel('Words'); plt.ylabel('Frequency')
plt.title('Top 10 Most Frequent Words in Tweets')
plt.xticks(rotation=45)
plt.show()
