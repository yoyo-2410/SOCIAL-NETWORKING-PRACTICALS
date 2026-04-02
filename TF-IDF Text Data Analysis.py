# pip install pandas matplotlib scikit-learn wordcloud

import pandas as pd, matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import WordCloud

docs = [
    "Artificial intelligence is transforming the world with new technology and innovation",
    "Data privacy is important in the age of artificial intelligence and digital technology",
    "Artificial intelligence and privacy concerns are growing with modern technology systems"
]

X = TfidfVectorizer(stop_words='english').fit_transform(docs)
df = pd.DataFrame(X.toarray(), columns=TfidfVectorizer(stop_words='english').fit(docs).get_feature_names_out())

print("\nTop Keywords:\n", df.sum().nlargest(10))

kw = ['artificial', 'privacy']
print("\nDocuments containing both:",
      df[(df[kw[0]] > 0) & (df[kw[1]] > 0)].index.tolist())

wc = WordCloud(width=800, height=400, background_color='white')
plt.imshow(wc.generate_from_frequencies(df.sum()))
plt.axis("off")
plt.title("WordCloud of Keywords")
plt.show()

print("\nTF-IDF Table:\n", df)
print("\nCommon Keywords:", df.columns[df.min() > 0].tolist())
