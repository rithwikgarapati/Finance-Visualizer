from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample data: phrases and their corresponding categories
data = [
    ("I love programming", "Personal Finances"),
    ("Basketball is my favorite sport", "Groceries"),
    ("The new movie is amazing", "Entertainment"),
    ("I enjoy cooking", "Eating Out"),
    ("Python is a powerful language", "Transportation"),
    ("Soccer is a great sport", "Education"),
    ("I like to watch movies", "Clothing"),
    ("I am experimenting with new recipes", "Online Payments"),
    ("I am experimenting with new recipes", "Miscellaneous"),
]

# Separate the data into features (X) and labels (y)
X, y = zip(*data)

# Vectorize the text data using CountVectorizer
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train a Multinomial Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_vectorized, y)

# Test the classifier with new phrases
new_phrases = [
    "I want to learn Python",
    "Football is a popular sport",
    "I love trying new dishes",
]

# Vectorize the new phrases
new_phrases_vectorized = vectorizer.transform(new_phrases)

# Predict the categories of the new phrases
predictions = classifier.predict(new_phrases_vectorized)

# Display the results
for phrase, category in zip(new_phrases, predictions):
    print(f"Phrase: {phrase} | Predicted Category: {category}")