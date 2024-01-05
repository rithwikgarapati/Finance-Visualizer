from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

data = [
    ("I love programming", "Personal Finances"),
    ("Basketball is my favorite sport", "Groceries"),
    ("The new movie is amazing", "Entertainment"),
    ("I enjoy cooking", "Eating Out"),
    ("Python is a powerful language", "Transportation"),

    ("Walmart Fruits Vegetables and Groceries", "Groceries"),
    ("Kroger Fred Meyer Ralphs groceries", "Groceries"),
    ("Albertsons Farmers Market ", "Groceries"),
    ("Costco Fruits and Vegetables", "Groceries"),
    ("Target Groceries Markets ", "Groceries"),
    ("Amazon Groceries", "Groceries"),
    ("Safeway Fruits and Vegetables and Groceries", "Groceries"),
    ("Trader Joe's Fruits and Vegetables", "Groceries"),
    ("Whole Foods Market Fruits and Vegetables", "Groceries"),

    ("Movies and Cinema ", "Entertainment"),
    ("Listening to Songs", "Entertainment"),
    ("Amusement and Trampoline Parks", "Entertainment"),
    ("Clubs and Parties", "Entertainment"),
    ("Online Streaming Services Subscriptions", "Entertainment"),
    ("New Movie At The Movie Theaters", "Entertainment"),
    ("Jazz Concert And Symphony shows and concerts", "Entertainment"),
    ("Board game purchase", "Entertainment"),
    ("Escape room experience", "Entertainment"),


    ("Mexican Taco Burrito Enchiladas Guacamole Quesadillas ", "Eating Out"),
    ("Fast Food Fries Chicken Beef Pork Burgers wings fire Hotdogs sauce juicy", "Eating Out"),
    ("Sandwiches Express Roasted Vegetables Salads Cheese", "Eating Out"),
    ("Italian Pasta Pizza Pepperoni Margherita Spaghetti soups stews Risotto", "Eating Out"),
    ("Blizzards Icecream Tiramasu Chocolate brownie cookie ", "Eating Out"),
    ("Thai curry PadThai Panang PadSeeEw  Rice", "Eating Out"),
    ("Chinese Takeout Noodles dimsum Fish Animals", "Eating Out"),
    ("Mediterranean Indian Naan Fried Roasted Toasted Grilled", "Eating Out"),
    ("Tea Boba Cocktail Mocktail Alcohol Soda Juice", "Eating Out"),
    ("Korean Donuts Sweets Creme Middle Eastern", "Eating Out"),

    ("Uber Lyft Taxis Traveling Shifting Moving", "Transportation"),
    ("Train Movement Plane Air Flying", "Transportation"),
    ("Bus Rides Carpools Venmo Payments", "Transportation"),
    ("Subways Metroes and Ferries Biking", "Transportation"),
    ("Shuttle Services Boats and Ferries", "Transportation"),
    ("Going out in a Car Moving in a car", "Transportation"),

    ("Rents House Payments Insurance Loan Payment Mortagage", "Personal Finances"),
    ("Water Electricity Bills Dividends Children", "Personal Finances"),
    ("House Repairs Apartment Repairs ", "Personal Finances"),
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